---
tags: [CG2111A, lecture-notes, academic]
---

# CG2111A Studio 3: Timers

## Overview
In this studio, students will explore the use of timers on the ATmega328P microcontroller to manage precise event triggering, such as handling interrupts and controlling servo motors. The session will cover two primary applications: debouncing mechanical switches to ensure clean signal transitions and generating pulse-width modulation (PWM) signals for servo control. By the end of the studio, students will gain hands-on experience with timer configurations and their practical applications in embedded systems.

## Key Concepts & Definitions
- **Timers**: Hardware counter blocks in the [[ATmega328P]] that increment based on a clock source, used for triggering events and measuring time.
- **Debouncing**: A technique to filter out false signals from mechanical switches caused by contact bounce.
- **Servo Control**: The process of using PWM signals to control the position of servos, which are actuators that provide precise positional control.
- **Prescaler**: A divisor that reduces the frequency of the timer clock, allowing for longer timing intervals.
- **CTC (Clear Timer on Compare)**: A mode where the timer resets upon reaching a specified compare value, useful for generating periodic interrupts.

## Detailed Technical Breakdown

### Timer Fundamentals
- **Clock Frequency**: The ATmega328P operates at a clock frequency of 16 MHz, resulting in a base clock period of 62.5 ns.
- **Prescaler Values**: Common prescalers include 1, 8, 64, 256, and 1024, which affect the timer tick duration.
  
| Prescaler | Time between ticks (μs) |
|-----------|-------------------------|
| 1         | 0.0625                  |
| 8         | 0.5                     |
| 64        | 4                       |
| 256       | 16                      |
| 1024      | 64                      |

### Timer Configuration Workflow
1. Select a timer (8-bit for short intervals, 16-bit for longer).
2. Choose a prescaler to control tick resolution.
3. Calculate the tick count \( V \) based on the desired interval \( T_{cycle} \) and tick duration \( T_{tick} \).
4. Program the timer:
   - Set mode bits (e.g., CTC).
   - Define compare value register.
   - Enable interrupts.
   - Reset the counter.
   - Start the timer by setting prescaler bits.

### Registers Interaction
- **TCNTx**: Timer counter value.
- **OCRxA / OCRxB**: Compare values for triggering interrupts.
- **TCCRxA / TCCRxB**: Timer control registers for mode and prescaler selection.
- **TIMSKx**: Interrupt mask for enabling timer-related interrupts.
- **TIFRx**: Interrupt flags set by hardware.

> [!note] 
> The choice of timer (8-bit vs. 16-bit) impacts the maximum count and thus the maximum interval that can be generated.

## Implementation/Examples

### Debouncing Algorithm
```c
currTime = millis();
if(currTime - lastTime > THRESHOLD) {
    lastTime = currTime;
    // Perform action on switch press
}
```

### Timer Setup Code
```c
void setupTimer() {
    // Set prescaler and mode for Timer2
    TCCR2A = (1 << WGM21); // CTC mode
    TIMSK2 = (1 << OCIE2A); // Enable Timer2 compare interrupt
    TCNT2 = 0; // Reset counter
    OCR2A = V - 1; // Set compare value
    TCCR2B = (1 << CS21); // Set prescaler
}
```

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[adc_handout_student]]
- [[Logic - Propositional Logic]]
- [[Interrupts]]
- [[Studio+GPIO_Programming_E+Lecture]]