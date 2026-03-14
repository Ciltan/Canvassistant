---
tags: [CG2111A, lecture-notes, academic]
---

# CG2111A Studio 1: GPIO Programming

## Overview
In this studio, students will learn to manipulate the GPIO pins of the Arduino Uno using bare-metal programming techniques, directly interacting with the ATmega328P registers. This approach enhances performance by eliminating the overhead of high-level libraries, providing precise control over hardware. By the end of the studio, students will develop a deeper understanding of microcontroller operations and gain practical experience in embedded C programming.

## Key Concepts & Definitions
- **GPIO**: General Purpose Input/Output, a type of pin on a microcontroller used for digital signal input and output.
- **Bare-Metal Programming**: Directly manipulating hardware registers without the abstraction of high-level libraries.
- **ATmega328P**: The microcontroller used in the Arduino Uno, which features various GPIO pins.
- **Bit-Masking**: A technique used to manipulate specific bits within a byte or register.
- **BCD (Binary-Coded Decimal)**: A class of binary encodings of decimal numbers where each digit is represented by its own binary sequence.

## Detailed Technical Breakdown

### Learning Objectives
1. Develop low-level (bare-metal) code for the Atmel microcontroller.
2. Understand bit-masking techniques.
3. Create simple Embedded C programs that interact directly with GPIO registers.
4. Extract meaningful information from the microcontroller datasheet.

### Equipment Needed
| Item                          | Quantity |
|-------------------------------|----------|
| Laptop with Arduino IDE       | x1       |
| Arduino Uno                   | x1       |
| Breadboard                    | x1       |
| Wires                         | -        |
| Green LEDs                    | x2       |
| Red LEDs                      | x2       |
| 7447 Decoder                  | x1       |
| 7-segment Display             | x1       |
| 220 Ω resistor                | x4       |
| 1.2K Ω resistor               | x4       |
| 4-way DIP switch              | x1       |

### Activities
1. **Basic GPIO Toggling**
   - Assemble a simple LED circuit using 220 Ω resistors.
   - Connect LEDs to Arduino digital pins.
   - Code example:
   ```c
   #include "Arduino.h"
   void setup() {
       // configure PB4 and PB5 as outputs
       DDRB = B00110000;
   }
   void loop() {
       PORTB = B00100000; // Green LED on, Red LED off
       delay(1000);
       PORTB = B00010000; // Green LED off, Red LED on
       delay(1000);
   }
   ```

2. **Reading DIP Switch Inputs**
   - Connect a 4-way DIP switch and LEDs.
   - Map switch inputs to LED outputs.
   - Code example for mapping:
   ```c
   // Example code to map switches to LEDs
   ```

3. **Switch-Dependent LED Sequences**
   - Modify the previous code to create sequences based on switch states.
   - Implement behaviors for all switches ON/OFF.

4. **7447-Driven 7-Segment Counter**
   - Develop a counter using a 7447 BCD-to-7-segment decoder.
   - Code example for controlling the 7-segment display:
   ```c
   // Example code for 7447 control
   ```

> [!note] **Important**: Review the lecture material on Canvas before starting the activities to avoid confusion.

> [!warning] **Note**: Always color-code your wires to speed up debugging.

## Related
- [[adc_handout_student]]
- [[Studio+GPIO_Programming_E+Lecture]]
- [[Interrupts]]
- [[AY2122+Sem1+Homework+1(S)]]
- [[AY2122+Sem2+Homework+3(S)]]