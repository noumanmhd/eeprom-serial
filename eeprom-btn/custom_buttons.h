#include "inc_libraries.h"

#define GAP_DELAY 500
#define TAP_MAX_DELAY 400
//////////////////////////////

#define SAMPLES_SIZE 20
#define SAMPLES_DELAY 1

class CustomButton {
 private:
  byte pin;
  unsigned long t;
  unsigned long dt;

  unsigned int tap;
  unsigned int hold;

 public:
  CustomButton(byte p) {
    t = 0;
    dt = 0;
    tap = 0;
    hold = 0;
    pin = p;
    pinMode(pin, INPUT_PULLUP);
  }
  bool readInput(byte pin) {
    double sum = 0;
    for (int i = 0; i < SAMPLES_SIZE; i++) {
      sum += digitalRead(pin);
      delay(SAMPLES_DELAY);
    }
    sum = round(sum / SAMPLES_SIZE);
    return (sum != 1);
  }

  unsigned long pressRoutine() {
    unsigned long hold_t = millis();
    while (readInput(pin))
      ;
    hold_t = millis() - hold_t;
    return hold_t;
  }

  void loop(void (*stage_1)(void), void (*stage_2)(void), void (*stage_3)(void),
            void (*stage_4)(void), void (*stage_5)(void), void (*stage_6)(void),
            void (*stage_7)(void)) {
    bool state = true;
    while (state) {
      dt = millis() - t;
      if (readInput(pin)) {
        unsigned int press_time = pressRoutine();
        if (press_time < TAP_MAX_DELAY) {
          tap++;
        } else {
          hold++;
        }
        t = millis();
        dt = 0;
        state = true;
      } else {
        state = false;
      }

      if (dt > GAP_DELAY) {
        state = false;
        if (tap > 0 || hold > 0) {
          if ((tap == 1) && (hold == 0))
            stage_1();
          else if ((tap == 2) && (hold == 0))
            stage_2();
          else if ((tap == 3) && (hold == 0))
            stage_3();
          else if ((tap == 4) && (hold == 0))
            stage_4();
          else if ((tap == 1) && (hold == 1))
            stage_5();
          else if ((tap == 2) && (hold == 1))
            stage_6();
          else if ((tap == 3) && (hold == 1))
            stage_7();

          tap = 0;
          hold = 0;
        }
      }
    }
  }
};
