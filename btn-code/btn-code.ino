#include <Arduino.h>
#include <EEPROM.h>
#include <SPI.h>

#include "custom_buttons.h"

///////////////////////////////
/******************************************************************************/
#define CMD_HEX 1
#define ADDR_HEX 4
#define VALUE_HEX 4
/******************************************************************************/
// Please Change the PIN (PA7)
#define BTN_PIN PA7
#define GAP_DELAY 500
#define TAP_MAX_DELAY 400
//////////////////////////////

/******************************************************************************/
const unsigned long T_ADDR = 2048;  // Memory Limit
const unsigned int DATA_LEN = CMD_HEX + ADDR_HEX + VALUE_HEX;
/******************************************************************************/

bool gui_mode = false;

CustomButton btn1(BTN_PIN);

void setup() { Serial.begin(9600); }
/******************************************************************************/
/******************************* EEPROM CODE **********************************/
/******************************************************************************/
void loop() {
  char cmd[DATA_LEN];
  if (Serial.available() > 0) {
    int n_chars = Serial.readBytesUntil('\n', cmd, DATA_LEN + 1);
    if (n_chars == DATA_LEN) {
      if (cmd[0] == 'G') {
        send_value(&cmd[0]);
      } else if (cmd[0] == 'P') {
        put_value(&cmd[0]);
      } else if (cmd[0] == 'Y') {
        gui_mode = true;
        Serial.println("{\"status\": true}");
      } else if (cmd[0] == 'N') {
        gui_mode = false;
        Serial.println("{\"status\": true}");
      }
    }
  } else if (!gui_mode) {
    btn_code();
  }
}

unsigned long get_addr(char *cmd) {
  char addr[ADDR_HEX + 1];
  for (int i = 0; i < ADDR_HEX; i++) {
    addr[i] = cmd[i + 1];
  }
  addr[ADDR_HEX] = '\0';
  return (unsigned long)strtol(addr, 0, ADDR_HEX * 4);
}

unsigned long get_value(char *cmd) {
  char value[VALUE_HEX + 1];
  for (int i = 0; i < VALUE_HEX; i++) {
    value[i] = cmd[ADDR_HEX + i + 1];
  }
  value[VALUE_HEX] = '\0';
  return (unsigned long)strtol(value, 0, ADDR_HEX * 4);
}

void send_value(char *cmd) {
  unsigned long addr = get_addr(cmd);
  if (addr < T_ADDR) {
    Serial.print("{\"status\": true, \"value\": ");
    Serial.print(EEPROM.read(addr));
    Serial.println("}");
  } else {
    Serial.println("{\"status\": false, \"value\": 0}");
  }
}

void put_value(char *cmd) {
  unsigned long value = get_value(cmd);
  unsigned long addr = get_addr(cmd);
  if (addr < T_ADDR) {
    EEPROM.update(addr, value);
    Serial.println("{\"status\": true}");
  } else {
    Serial.println("{\"status\": false}");
  }
}
/******************************************************************************/
/***************************** Button Code ************************************/
/******************************************************************************/
void btn_code() {
  btn1.loop(stage_one, stage_two, stage_three, stage_four, stage_five,
            stage_six, stage_seven);
}

void stage_one() { Serial.println("Stage 1"); }

void stage_two() { Serial.println("Stage 2"); }

void stage_three() { Serial.println("Stage 3"); }

void stage_four() { Serial.println("Stage 4"); }

void stage_five() { Serial.println("Stage 5"); }

void stage_six() { Serial.println("Stage 6"); }

void stage_seven() { Serial.println("Stage 7"); }
