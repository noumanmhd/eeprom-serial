#include "inc_libraries.h"

#define NUMBER_OF_PAGES 5

#define PAGE_MEMORY 85
#define FIRST_PAGE_MEMORY 95

#define TEXT_ADDR 1850
#define TEXT_LEN 9

#define P_ROWS 4
#define P_COLS 10

const char *presetText[6] = {"INTRO", "VERSE", "CHORUS",
                             "SOLO",  "OUTRO", "BRIDGE"};

char pageLabel[TEXT_LEN];

struct Page {
  byte value[P_ROWS][P_COLS];
  byte presetLabel[P_COLS];
  byte onoffState[P_ROWS - 1][P_COLS];
  byte program_scene;
};

char *getPreset(byte index) {
  if (index > 5) index = 5;
  return (char *)presetText[index];
}