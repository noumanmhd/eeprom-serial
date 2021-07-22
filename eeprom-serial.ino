#include <SPI.h>
#include <EEPROM.h>

#define CMD_HEX 1
#define ADDR_HEX 4
#define VALUE_HEX 4

const unsigned long T_ADDR = 2048; // Memory Limit
const unsigned int DATA_LEN = CMD_HEX + ADDR_HEX + VALUE_HEX;

void setup()
{
    Serial.begin(9600);
}

void loop()
{
    char cmd[DATA_LEN];
    if (Serial.available() > 0)
    {
        int n_chars = Serial.readBytesUntil('\n', cmd, DATA_LEN + 1);
        if (n_chars == DATA_LEN)
        {
            if (cmd[0] == 'G')
            {
                send_value(&cmd[0]);
            }
            else if (cmd[0] == 'P')
            {
                put_value(&cmd[0]);
            }
        }
    }
}

unsigned long get_addr(char *cmd)
{
    char addr[ADDR_HEX + 1];
    for (int i = 0; i < ADDR_HEX; i++)
    {
        addr[i] = cmd[i + 1];
    }
    addr[ADDR_HEX] = '\0';
    return (unsigned long)strtol(addr, 0, ADDR_HEX * 4);
}

unsigned long get_value(char *cmd)
{
    char value[VALUE_HEX + 1];
    for (int i = 0; i < VALUE_HEX; i++)
    {
        value[i] = cmd[ADDR_HEX + i + 1];
    }
    value[VALUE_HEX] = '\0';
    return (unsigned long)strtol(value, 0, ADDR_HEX * 4);
}

void send_value(char *cmd)
{
    unsigned long addr = get_addr(cmd);
    if (addr < T_ADDR)
    {
        Serial.print("{\"status\": true, \"value\": ");
        Serial.print(EEPROM.read(addr));
        Serial.println("}");
    }
    else
    {
        Serial.println("{\"status\": false, \"value\": 0}");
    }
}

void put_value(char *cmd)
{
    unsigned long value = get_value(cmd);
    unsigned long addr = get_addr(cmd);
    if (addr < T_ADDR)
    {
        EEPROM.update(addr, value);
        Serial.println("{\"status\": true}");
    }
    else
    {
        Serial.println("{\"status\": false}");
    }
}
