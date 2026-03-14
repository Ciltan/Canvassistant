---
tags: [CG2111A, lecture-notes, academic]
---

# Interrupts in I/O Programming

## Overview
This lecture explores the concept of [[Interrupts]] in the context of I/O programming, particularly focusing on their implementation in the Arduino environment. Interrupts allow a CPU to respond to events without constant polling, enhancing efficiency in handling I/O operations. We will discuss the differences between polling and interrupt-driven I/O, and provide examples of how to implement interrupts in Arduino programming.

## Key Concepts & Definitions
- **Interrupts**: Mechanisms that allow the CPU to respond to events asynchronously, enabling multitasking.
- **Polling**: A method where the CPU continuously checks the status of an I/O device.
- **Interrupt Service Routine (ISR)**: A special function that executes in response to an interrupt.
- **Vector Table**: A data structure that maps interrupt requests to their corresponding ISRs.
- **Volatile**: A keyword in C/C++ that indicates a variable may be changed unexpectedly, requiring the compiler to reload its value.

## Detailed Technical Breakdown

### I/O Programming Methods
1. **Polling**
   - The CPU actively checks the status of devices.
   - Example: Printing a string to a printer involves checking if the printer is ready for each character.
   - **Issues**: Inefficient as it wastes CPU cycles during busy-waiting.

2. **Interrupt-Driven I/O**
   - The CPU can perform other tasks while waiting for an I/O operation to complete.
   - The device signals the CPU via an interrupt request (IRQ) when it is ready.
   - The CPU executes an ISR to handle the event.

### Interrupt Programming on Arduino
- **Using `attachInterrupt`**:
  ```cpp
  attachInterrupt(digitalPinToInterrupt(pinnum), function, mode);
  ```
  - `pinnum`: Pin number (2 or 3 for Arduino UNO).
  - `function`: The ISR to call.
  - `mode`: Triggering condition (LOW, CHANGE, RISING, FALLING).

### Bare-metal AVR Interrupt Programming
- **ISR Declaration**:
  ```c
  ISR(vector) {
      // ISR Code
  }
  ```
  - `vector`: Specifies which interrupt to handle.

### Interrupt Masking
- **Disabling/Enabling Interrupts**:
  - Arduino: `noInterrupts()` to disable, `interrupts()` to enable.
  - Bare-metal: `cli()` to disable, `sei()` to enable.

### Importance of Volatile Variables
- Global variables modified by ISRs must be declared as `volatile` to ensure the main program sees the latest value.
- Example:
  ```c
  static volatile int onOff;
  ```

## Implementation/Examples
### Example Code for Interrupts
```cpp
#define outputPin 13
#define inputInterrupt 0

volatile unsigned char flag;

void setup() {
    pinMode(outputPin, OUTPUT);
    attachInterrupt(digitalPinToInterrupt(inputInterrupt), readAnalog, CHANGE);
}

void loop() {
    if (flag) {
        processData(data);
        flag = 0;
    }
}

void readAnalog() {
    data = analogRead(0);
    flag = 1;
}
```

> [!important] **Efficiency of Interrupts**: Using interrupts allows the CPU to perform other tasks rather than waiting for I/O operations, significantly improving overall system performance.

> [!warning] **Volatile Variables**: Always declare global variables modified by ISRs as volatile to prevent infinite loops and ensure correct program behavior.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[adc_handout_student]]
- [[Studio+GPIO_Programming_E+Lecture]]
- [[Interrupts]] 
- [[CG2111A-Quiz1-AY2425-S2]]