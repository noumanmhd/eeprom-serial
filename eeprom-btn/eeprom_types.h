#include "inc_libraries.h"

#define NUMBER_OF_PAGES 5

#define PAGE_MEMORY 85
#define FIRST_PAGE_MEMORY 95

#define TEXT_ADDR 1850
#define TEXT_LEN 9

#define P_ROWS 4
#define P_COLS 10

struct Page {
  byte value[P_ROWS][P_COLS];
};