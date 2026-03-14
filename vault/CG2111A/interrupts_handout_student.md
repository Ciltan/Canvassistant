---
tags: [CG2111A, lecture-notes, academic]
---

# CG2111A Studio 2: Interrupts

## Overview
In this studio, we explore the critical concept of [[Interrupts]] in Computer Engineering, focusing on how they enable CPUs and MCUs to respond to hardware signals. By examining the ATmega328P microcontroller, students will learn to implement interrupt-driven programming, contrasting it with polling methods. The hands-on activities will enhance understanding of how to efficiently manage hardware events, such as button presses, to create responsive applications.

## Key Concepts & Definitions
- **Interrupt**: A special hardware signal that prompts the CPU to pause its current operations and address an event.
- **Polling**: A method where the CPU repeatedly checks the status of an input device to determine if it needs attention.
- **Interrupt-driven programming**: A programming paradigm where the CPU is alerted to events via interrupts, allowing for more efficient processing.
- **AVR**: A family of microcontrollers developed by Atmel, commonly used in embedded systems.
- **Arduino**: An open-source electronics platform based on easy-to-use hardware and software.

## Detailed Technical Breakdown

### Learning Objectives
1. Differentiate between polling and interrupt-driven programming.
2. Implement button-controlled LED flashing using a polling approach.
3. Utilize Arduino’s `attachInterrupt` function for handling interrupts.
4. Configure AVR interrupts at the bare-metal register level.

### Equipment Needed
| Item                     | Quantity |
|--------------------------|----------|
| Arduino UNO              | ×1       |
| LED, Red                 | ×1       |
| LED, Green               | ×1       |
| Resistor, 330 Ω, 0.25W   | ×2       |
| Resistor, 10K Ω, 0.25W   | ×1       |
| Pushbutton Switch         | ×1       |
| Breadboard                | ×1       |
| Jumper wires              | -        |

### Activities Overview
- **Activity 1**: Polling Using Arduino Wiring Language
- **Activity 2**: Interrupts Using the Arduino Wiring Language
- **Activity 3**: Interrupts Using Bare-Metal AVR Programming

## Implementation/Examples

### Activity 1: Polling Using Arduino Wiring Language
1. **Circuit Assembly**: 
   - Connect a Red LED to pin 11 with a 330Ω resistor.
   - Connect a Green LED to pin 12 with a 330Ω resistor.
   - Connect a Pushbutton switch to pin 2 with a 10kΩ pull-down resistor.

2. **Arduino Code**:
   ```cpp
   #define REDPIN 11
   #define GREENPIN 12
   #define SWITCHPIN 2
   #define LED_DELAY 100
   static volatile int turn=0;

   void setup() {
       pinMode(REDPIN, OUTPUT);
       pinMode(GREENPIN, OUTPUT);
       pinMode(SWITCHPIN, INPUT);
   }

   void flashGreen() {
       int counter=1;
       while(turn==0) {
           for(int i=0; i<counter; i++) {
               digitalWrite(GREENPIN, HIGH);
               delay(LED_DELAY);
               digitalWrite(GREENPIN, LOW);
               delay(LED_DELAY);
           }
           counter++;
           delay(1000);
       }
   }

   void flashRed() {
       int counter=1;
       while(turn==1) {
           for(int i=0; i<counter; i++) {
               digitalWrite(REDPIN, HIGH);
               delay(LED_DELAY);
               digitalWrite(REDPIN, LOW);
               delay(LED_DELAY);
           }
           counter++;
           delay(1000);
       }
   }

   void loop() {
       if(turn == 0)
           flashGreen();
       if(turn == 1)
           flashRed();
   }
   ```

> [!note] Ensure to demonstrate your program to your TA and explain your code modifications.

### Activity 2: Interrupts Using the Arduino Wiring Language
1. **New Sketch**: Create `part2.ino` with the following code:
   ```cpp
   #define buttonPin 2
   #define LEDPIN 12
   static volatile int onOff = 0;

   void switchISR() {
       onOff = 1 - onOff;
   }

   void setup() {
       attachInterrupt(digitalPinToInterrupt(buttonPin), switchISR, RISING);
       pinMode(LEDPIN, OUTPUT);
   }

   void loop() {
       if(onOff == 0)
           digitalWrite(LEDPIN, LOW);
       else
           digitalWrite(LEDPIN, HIGH);
   }
   ```

> [!important] Discuss the `attachInterrupt` function and its parameters, including the meaning of the `RISING` mode.

### Activity 3: Interrupts Using Bare-Metal AVR Programming
1. **Bare-Metal Code**:
   ```cpp
   #include <avr/io.h>
   #include <avr/interrupt.h>
   static volatile int onOff=0;

   void setup() {
       EICRA |= 0b00000011; // Set INT0 to trigger on RISING edge
       DDRB |= 0b00010000;  // Set LED pin to OUTPUT
       EIMSK |= 0b00000001; // Enable INT0
       sei();               // Enable global interrupts
   }

   ISR(INT0_vect) {
       onOff=1-onOff;
   }

   void loop() {
       if(onOff==0)
           PORTB &=0b11101111; // Turn off LED
       else
           PORTB |= 0b00010000; // Turn on LED
   }
   ```

## Summary
In this studio, students learned the differences between polling and interrupt-driven programming, how to use Arduino’s `attachInterrupt` function, and how to configure AVR interrupts at the register level. Understanding interrupts is crucial for developing responsive systems in embedded programming.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[adc_handout_student]]
- [[Studio+GPIO_Programming_E+Lecture]]
- [[Midterm+Briefing]]