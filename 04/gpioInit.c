#include "avr/io.h"    void Init_PORT_GPIO(void)    {
        DDRA = 0b01110101;
    }