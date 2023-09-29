#!/usr/bin/python3
import os

portID = input("Enter the port you wish to manipulate: \n").capitalize()

register = [] 

for i in range(0, 8) :
    value = input(f"Enter pin {i} value: ")
    register.append(value)

# print(register) #<<<<<<<

register = ''.join(str(e) for e in register) #convert list to string

print(register)

TempData = "DDR" + portID + " = " + "0b" + register

print(TempData)

try:
    gpioInit = open('gpioInit.c', 'x')

    GPIO = f'#include "avr/io.h"\n\
    void Init_PORT_GPIO(void)\n\
    {{\n\
        {TempData};\n\
    }}'
    gpioInit.write(GPIO)
    print('File created successfully')

except FileExistsError:
    print('The File already exists')