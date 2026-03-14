---
tags: [CG2111A, lecture-notes, academic]
---

# CG2111A Tutorial 1: GPIO, Interrupts, PWM, and Timers

## Overview
This tutorial delves into the fundamental functionalities of the ATMega328P, focusing on [[GPIO]], [[Interrupts]], [[Timers]], and [[PWM]]. It prepares students for the first quiz of CG2111A by exploring practical applications and theoretical concepts. Key questions guide the exploration of these topics, emphasizing design considerations and power management.

## Key Concepts & Definitions
- **GPIO**: General Purpose Input/Output, a type of pin on a microcontroller that can be configured as either an input or output.
- **Interrupts**: Mechanisms that allow a microcontroller to respond to events asynchronously.
- **PWM**: Pulse Width Modulation, a technique used to control the amount of power delivered to an electronic device.
- **Timers**: Hardware components that can generate precise time delays or trigger events at specific intervals.

## Detailed Technical Breakdown

### Part 1: GPIO and Interrupts

#### Question 1: Freeing Up Pins
- Microcontroller pins can serve multiple functions; careful planning is essential.
- Example: PORT B pins are often used for LEDs and switches, but some are reserved for the external crystal oscillator.

#### Question 2: Active-Low LED
- **Active-Low Logic**: Setting a pin LOW turns the LED ON.
- **Sinking Current**: Current flows into the microcontroller pin, which has a specified limit to avoid damage.

#### Question 3: Power Consumption
- Minimizing power consumption is crucial for embedded systems.
- Implementing the 328P's Standby Mode can significantly reduce power usage.

#### Question 4: Overheads
- Polling vs. Interrupt-driven I/O: Analyze the efficiency of each method in data transfer scenarios.

#### Question 5: Overheads Part 2
- Compare the efficiencies of polling, interrupt-driven I/O, and DMA for smaller data blocks.

#### Question 6: Enabling and Disabling Interrupts
- Disabling interrupts can prevent race conditions during critical code execution.

#### Question 7: Interrupt Implementation
- Discuss the detection of hardware interrupts and the execution flow of Interrupt Service Routines (ISRs).

#### Question 8: Interrupt Order
- Analyze the execution order of functions when multiple interrupts are triggered.

#### Question 9: Interrupt Sources
- Identify which pins on the ATMega328P can trigger interrupts and their behaviors.

### Part 2: Timers and PWM

#### Question 10: Timer Uses and Types
- Timers can be used for event scheduling and generating precise time delays.
- Differences between 8-bit and 16-bit timers in terms of resolution and range.

#### Question 11: Timers and Signals
- Calculate the interval for interrupt triggers based on timer configurations.

#### Question 12: Choosing Timer Values
- Evaluate the best prescaler settings for achieving desired timer intervals.

#### Question 13: PWM Generation
- Discuss software-based PWM generation and its limitations.
- Explore methods for generating low-frequency PWM signals.

## Implementation/Examples
```c
// Example code for setting up an Active-Low LED
DDRB |= (1 << DDB1); // Set PORTB Pin 1 as output
PORTB &= ~(1 << PORTB1); // Turn ON LED (Active-Low)
```

> [!note] **Important Consideration**: Always refer to the ATMega328P datasheet for specific electrical characteristics and limitations when designing circuits.
> [!warning] **Caution**: Exceeding the maximum sinking current can damage the microcontroller.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[adc_handout_student]]
- [[Midterm+Briefing]]
- [[CS1231+TUTORIAL+3]]