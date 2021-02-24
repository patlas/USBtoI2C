#include <stdint.h>
#include <parser.h>



typedef struct cmd {
    uint8_t cmd;
    uint8_t addr;
    uint8_t reg;
    uint8_t size;
    uint8_t data[255];
} cmd_t;

typedef enum command {
    WRITE = 1,
    READ = 2
} commant_t;
