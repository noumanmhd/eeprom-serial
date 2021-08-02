#include "inc_libraries.h"
#include "eeprom_types.h"
#include "custom_buttons.h"

/******************************************************************************/
#define CMD_HEX 1
#define ADDR_HEX 4
#define VALUE_HEX 4

/******************* Please Change the PINs ***********************************/
#define BTN_1_PIN PA7
#define BTN_2_PIN PA6
#define BTN_3_PIN PA5
#define BTN_4_PIN PA4
/******************************************************************************/
const unsigned long T_ADDR = 2048;  // Memory Limit
const unsigned int DATA_LEN = CMD_HEX + ADDR_HEX + VALUE_HEX;
/******************************************************************************/

bool gui_mode = false;

CustomButton btn_1(BTN_1_PIN);
CustomButton btn_2(BTN_2_PIN);
CustomButton btn_3(BTN_3_PIN);
CustomButton btn_4(BTN_4_PIN);

Page page;

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
  btn_1.loop(btn_1_a, btn_1_b, btn_1_c, btn_1_d, btn_1_e, btn_1_f, btn_1_g);

  btn_2.loop(btn_2_a, btn_2_b, btn_2_c, btn_2_d, btn_2_e, btn_2_f, btn_2_g);

  btn_3.loop(btn_3_a, btn_3_b, btn_3_c, btn_3_d, btn_3_e, btn_3_f, btn_3_g);

  btn_4.loop(btn_4_a, btn_4_b, btn_4_c, btn_4_d, btn_4_e, btn_4_f, btn_4_g);
}
/***************************** First Button ***********************************/
void btn_1_a() { 
  EEPROM.get(FIRST_PAGE_MEMORY, page);
  Serial.println(page.value[2][9]);
  Serial.println("Button 1 Stage 1"); }

void btn_1_b() { Serial.println("Button 1 Stage 2"); }

void btn_1_c() { Serial.println("Button 1 Stage 3"); }

void btn_1_d() { Serial.println("Button 1 Stage 4"); }

void btn_1_e() { Serial.println("Button 1 Stage 5"); }

void btn_1_f() { Serial.println("Button 1 Stage 6"); }

void btn_1_g() { Serial.println("Button 1 Stage 7"); }

/***************************** Second Button **********************************/
void btn_2_a() { Serial.println("Button 2 Stage 1"); }

void btn_2_b() { Serial.println("Button 2 Stage 2"); }

void btn_2_c() { Serial.println("Button 2 Stage 3"); }

void btn_2_d() { Serial.println("Button 2 Stage 4"); }

void btn_2_e() { Serial.println("Button 2 Stage 5"); }

void btn_2_f() { Serial.println("Button 2 Stage 6"); }

void btn_2_g() { Serial.println("Button 2 Stage 7"); }

/***************************** Third Button ***********************************/
void btn_3_a() { Serial.println("Button 3 Stage 1"); }

void btn_3_b() { Serial.println("Button 3 Stage 2"); }

void btn_3_c() { Serial.println("Button 3 Stage 3"); }

void btn_3_d() { Serial.println("Button 3 Stage 4"); }

void btn_3_e() { Serial.println("Button 3 Stage 5"); }

void btn_3_f() { Serial.println("Button 3 Stage 6"); }

void btn_3_g() { Serial.println("Button 3 Stage 7"); }

/***************************** Fourth Button **********************************/
void btn_4_a() { Serial.println("Button 4 Stage 1"); }

void btn_4_b() { Serial.println("Button 4 Stage 2"); }

void btn_4_c() { Serial.println("Button 4 Stage 3"); }

void btn_4_d() { Serial.println("Button 4 Stage 4"); }

void btn_4_e() { Serial.println("Button 4 Stage 5"); }

void btn_4_f() { Serial.println("Button 4 Stage 6"); }

void btn_4_g() { Serial.println("Button 4 Stage 7"); }
/******************************************************************************/
