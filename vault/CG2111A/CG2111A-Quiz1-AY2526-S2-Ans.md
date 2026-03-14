---
tags: [CG2111A, lecture-notes, academic]
---

# CG2111A Engineering Principles and Practices II - Quiz 1 Overview

## Overview
This document outlines the structure and content of Quiz 1 for the CG2111A module, which consists of fifteen questions covering various topics in engineering principles and practices. The quiz is designed to assess students' understanding of concepts related to [[GPIO]], interrupts, timers, and PWM on the ATMega328P microcontroller. It is a closed-book assessment, allowing only a single double-sided cheat sheet.

## Key Concepts & Definitions
- **GPIO**: General Purpose Input/Output, a type of pin on a microcontroller used for digital signal input and output.
- **Interrupts**: Mechanisms that allow a microcontroller to respond to events asynchronously.
- **Timers**: Hardware components that keep track of time and can trigger events at specified intervals.
- **PWM**: Pulse Width Modulation, a technique used to control the amount of power delivered to an electronic device by varying the width of the pulses in a signal.

## Detailed Technical Breakdown

### Quiz Instructions
- **Format**: 15 questions on 10 pages, including an appendix.
- **Answer Sheet**: Students must shade and write their Student ID; names are not allowed.
- **Materials**: Only 2B pencils and a single double-sided A4 cheat sheet are permitted.
- **Duration**: 45 minutes, worth 30 marks.
- **Restrictions**: Closed book; no electronic devices except for calculators.

### GPIO Configuration
1. **Question**: Configure PD2 and PD3 as outputs.
   - **Options**:
     - a. `DDRD &= (1 << 2) | (1 << 3);`
     - b. `DDRD ^= (1 << 2) | (1 << 3);`
     - c. `PORTD |= (1 << 2) | (1 << 3);`
     - d. 
       ```
       DDRD = (1 << 2);
       DDRD = (1 << 3);
       ```
     - e. 
       ```
       DDRD |= (1 << 2);
       DDRD |= (1 << 3);
       ```

2. **Question**: Maximum frequency of square wave on PB4.
   - **Given**: 20 MHz clock, toggling with `PORTB ^= (1 << 4);` in a loop taking 50 clock cycles.
   - **Options**: a. 0.1 MHz, b. 0.2 MHz, c. 0.3 MHz, d. 0.4 MHz, e. None.

3. **Question**: Effect of increasing loop execution time to 80 clock cycles.
   - **Options**: a. Increases frequency, b. Decreases frequency, c. Unchanged, d. No toggling, e. None.

### Interrupts, Timers, and PWM
- **Interrupts**: 
  - True statements include:
    - ii. Hardware support is required.
    - iii. More efficient than polling.
    - iv. Invoked like regular functions.

### Example Code Snippets
```c
#define PD2_MASK (1 << 2)
#define PD6_MASK (1 << 6)
int main(void) {
    DDRD &= ~PD2_MASK;
    DDRD |= PD6_MASK;
    PORTD &= ~PD6_MASK;
    while (1) {
        if (PIND & PD2_MASK) {
            PORTD |= PD6_MASK;
        } else {
            PORTD &= ~PD6_MASK;
        }
    }
}
```

> [!note] **Important**: Ensure to configure GPIO pins correctly before use to avoid unexpected behavior.

### Related
- For further reading, refer to [[Logic - Propositional Logic]], [[Chapter+2]], and [[Chapter+4+How+Designers+Think]] for foundational concepts that support the understanding of GPIO and interrupts.