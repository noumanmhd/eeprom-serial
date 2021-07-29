///////////////////////////////
// Please Change the PIN (PA7)
#define BTN_PIN PA7 
#define GAP_DELAY 500
#define TAP_MAX_DELAY 400
//////////////////////////////

#define SAMPLES_SIZE 20
#define SAMPLES_DELAY 1

unsigned long t = 0;
unsigned long dt = 0;

unsigned int tap = 0;
unsigned int hold = 0;


void setup() {
  Serial.begin(9600);
  pinMode(BTN_PIN, INPUT_PULLUP);
}

void loop() {
  dt = millis() - t;
  if(readInput(BTN_PIN)){
    unsigned int press_time = pressRoutine();
    if(press_time < TAP_MAX_DELAY){
      tap++;
    }
    else{
      hold++;
    }
    t = millis();
    dt = 0;
  }
 
  if(dt > GAP_DELAY){
    if (tap > 0 || hold > 0){
      Serial.print("TAP ");
      Serial.print(tap);
      Serial.print(" - ");
      Serial.print("HOLD ");
      Serial.println(hold);
      tap = 0;
      hold = 0;
    }
  }
}

bool readInput(byte pin){
  double sum = 0;
  for (int i=0; i<SAMPLES_SIZE; i++){
    sum += digitalRead(pin);
    delay(SAMPLES_DELAY);
  }
  sum = round(sum/SAMPLES_SIZE);
  return (sum != 1);
}

unsigned long pressRoutine(){
  unsigned long hold_t = millis();
  while(readInput(BTN_PIN));
  hold_t = millis() - hold_t;
  return hold_t;
}
