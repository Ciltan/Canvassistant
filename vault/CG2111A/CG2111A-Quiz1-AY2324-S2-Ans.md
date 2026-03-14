---
tags: [CG2111A, lecture-notes, academic]
---

# CG2111A Engineering Principles and Practices II - Quiz 1 Overview

## Overview
This document outlines the key components and instructions for Quiz 1 of the CG2111A module. It includes essential guidelines for quiz administration, technical questions related to microcontroller programming, and concepts of interrupts and data transmission. The quiz assesses students' understanding of programming with the AT328P microcontroller, particularly in configuring LEDs and switches, as well as their knowledge of interrupts and data handling.

## Key Concepts & Definitions
- **AT328P**: A microcontroller used in Arduino boards, known for its versatility in handling various input/output operations.
- **PWM (Pulse Width Modulation)**: A technique used to control the amount of power delivered to electrical devices by varying the width of the pulses in a pulse train.
- **Interrupts**: Mechanisms that allow a microcontroller to respond to events asynchronously, pausing the current execution to handle the event.
- **IAT (Inter-Arrival Time)**: The time interval between the arrival of data packets over a communication channel.
- **Volatile Variables**: Variables that can be changed unexpectedly, often used in the context of interrupts to ensure the latest value is read.

## Detailed Technical Breakdown

### Quiz Instructions
- **Student ID Requirement**: Ensure your student ID is shaded and written on the OCR sheet; failure to do so results in a score of 0.
- **Shading Guidelines**: Use only 2B pencils and fully shade the correct answers to avoid misgrading.
- **Communication Policy**: Only communicate with invigilators; any other communication is considered cheating.

### Programming Questions
1. **LED Configuration**
   - **Pin Mapping**:
     - Arduino Pin 8 → Port B, Pin 0
     - Arduino Pin 7 → Port D, Pin 7
   - **Function**:
     ```c
     unsigned char MASK(unsigned char bit_position) {
         return (0x01 << bit_position);
     }
     ```
   - **Correct Configuration Code**: 
     - Option (c): 
       ```c
       DDRB |= MASK(0);
       DDRD |= MASK(7);
       ```

2. **LED Control Logic**
   - **Variable Declaration**:
     ```c
     unsigned char data = 0x7E;
     ```
   - **Correct Code to Turn ON LEDs**: 
     - Option (e):
       ```c
       PORTB = ~data;
       PORTD = data << 1;
       ```

3. **Switch Configuration**
   - **Correct Code**: 
     - Option (b):
       ```c
       DDRB &= ~MASK(5);
       ```

4. **Switch Logic for LED Control**
   - **Correct Code**: 
     - Option (a):
       ```c
       if ((PINB & MASK(5)) != 0x00) {
           LED_On();
       } else {
           LED_Off();
       }
       ```

### PWM Signal Generation
- **Duty Cycle Calculation**:
   - For PD6 and PD5:
     - Option (e): 
       - PD6 = 50%
       - PD5 = 25%

### Interrupts and Data Handling
- **True Statements about Interrupts**:
   - Option (d): The Atmega328P, by default, does not support nested interrupts.

### Data Transmission Questions
1. **Inter-Arrival Time Calculation**:
   - Correct Answer: 
     - Option (c): 10^-6 seconds

2. **Maximum Instructions Executed**:
   - Correct Answer: 
     - Option (d): 640 instructions

3. **Wasted Instructions During Polling**:
   - Correct Answer: 
     - Option (b): Around 760 thousand instructions

### Additional Questions
- **Parity System Example**: 
   - Correct Data Sent: 
     - Option (A) or (C)

- **USART Configuration**:
   - Correct UBRR Values: 
     - Option (D): UBRR0H = 2, UBRR0L = 112

- **Transmission Time for 256 Characters**:
   - Correct Answer: 
     - Option (C): 0.64 seconds

## Implementation/Examples
```c
// Example of LED configuration
DDRB |= MASK(0); // Set PB0 as output
DDRD |= MASK(7); // Set PD7 as output

// Example of PWM signal generation
#include "Arduino.h"
#include <avr/io.h>
#include <avr/interrupt.h>
unsigned char val = 0x01;
void setup() {
    TCNT0 = 0;
    TCCR0A = 0b10100001; // Configure Timer
    OCR0A = (val << 7); // Set duty cycle
    OCR0B = (val << 6);
    TCCR0B = 0b00000011; // Start Timer
    DDRD |= (val << 6) | (val << 5); // Set PD6 and PD5 as output
}
void loop() {
    // Main loop
}
```

> [!important] Ensure to follow all quiz instructions carefully to avoid penalties.
> [!note] Review the concepts of interrupts and PWM as they are crucial for understanding microcontroller operations.

## Related
- [[Logic - Propositional Logic]]
- [[Chapter+2]]
- [[Chapter+4+How+Designers+Think]]
- [[Midterm+Briefing]]
- [[Tutorial+1+Solution]]