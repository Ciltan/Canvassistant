---
tags: [CG2111A, lecture-notes, academic]
---

# CG2111A Engineering Principles and Practices II - Midterm Assessment Overview

## Overview
This document outlines the midterm assessment for CG2111A, consisting of fifteen questions covering various programming and engineering principles related to the ATMega328P microcontroller. The assessment is designed to evaluate students' understanding of interrupt handling, PWM signal generation, and data transmission protocols. It is an open-book exam, allowing the use of printed notes, and emphasizes practical coding scenarios.

## Key Concepts & Definitions
- **ATMega328P**: A microcontroller used in various embedded systems, known for its efficiency and ease of use.
- **PWM (Pulse Width Modulation)**: A technique used to encode a message into a pulsing signal.
- **Interrupts**: Mechanisms that allow a microcontroller to respond to events asynchronously.
- **OCR (Output Compare Register)**: A register used to set the timing for PWM signals.
- **UBRR (USART Baud Rate Register)**: A register that sets the baud rate for serial communication.

## Detailed Technical Breakdown

### Assessment Instructions
- **Format**: 15 questions on printed pages, including an appendix with register details.
- **Materials**: Use of 2B pencils and an OCR sheet for answers.
- **Duration**: 60 minutes, worth 30 marks.
- **Allowed Materials**: Open book; printed notes permitted, but no electronic devices except calculators.

### Sample Questions Breakdown
1. **Code Analysis**: 
   - Given code snippets manipulate registers to control I/O pins.
   - Example: `DDRB &= ~(1 << 5);` configures pin directions.

2. **PWM Signal Generation**:
   - Understanding the timing and duty cycle of PWM signals.
   - Example: Setting PD6 high every 100ms simulates a 20% duty cycle.

3. **Interrupt Handling**:
   - Sequence of operations for handling interrupts.
   - Importance of saving registers and program counter (PC).

4. **Data Transmission**:
   - Calculating the time taken to transmit data using specific baud rates.
   - Example: 2 KiB of data at 2400 bps.

### Example Code Snippet
```c
DDRB &= ~(1 << 5);
DDRD |= (1 << 4);
PORTD &= ~(1 << 4);
while(PINB & (1 << 5));
PORTD |= (1 << 4);
```

> [!note] **Important**: Ensure to read the questions carefully and understand the context of the code provided.

> [!warning] **Caution**: Misinterpretation of the code logic may lead to incorrect answers. Pay attention to the flow of control in the loops.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[adc_handout_student]]
- [[Logic - Propositional Logic]]
- [[CS1231+TUTORIAL+3]]