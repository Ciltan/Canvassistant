---
tags: [CG2111A, lecture-notes, academic]
---

# Timer Programming in CG2111A

## Overview
This lecture focuses on the significance of timers in real-time systems, particularly within the context of the Atmega AVR microcontroller. Timers facilitate precise control over sensor readings and actuator operations, ensuring that time-sensitive algorithms, such as the PID control algorithm, function correctly. The lecture also introduces the Clear Timer on Compare (CTC) mode for Timer 0, detailing its configuration and practical applications.

## Key Concepts & Definitions
- **Timers**: Essential components in real-time systems that manage timing for tasks and operations.
- **CTC Mode**: A timer mode that resets the timer upon reaching a specified value, allowing for regular interrupts.
- **Atmega328**: A microcontroller featuring multiple timers, including Timer 0, Timer 1, and Timer 2.
- **Prescaler**: A value that determines the frequency at which the timer increments.
- **OCR0A**: Output Compare Register for Timer 0, used to set the top value for the timer.
- **ISR (Interrupt Service Routine)**: A function that executes in response to a timer interrupt.

## Detailed Technical Breakdown

### Importance of Timers
- **Sensor and Actuator Control**: Timers enable precise timing for reading sensors and controlling actuators.
- **Multi-tasking**: Essential for task switching in multi-tasking operating systems.
- **Pulse Width Modulation (PWM)**: Timers are used to generate analog outputs.

### Timers in the Atmega AVR
- **Timer 0**: An 8-bit timer that counts from 0 to 255.
- **Timer 1**: A 16-bit timer that counts from 0 to 65535.
- **Timer 2**: Another 8-bit timer similar to Timer 0.

### CTC Mode Configuration
1. **Determine Time Period**: Decide the desired time period (e.g., 1 ms).
2. **Select Prescaler and Count Value**: Choose a prescaler value \( P \) and a count value \( V \) based on the I/O clock rate.
3. **Register Configuration**:
   - Set initial timer value in TCNT0.
   - Set the top value in OCR0A.

### Prescaler Selection
- The prescaler affects the timer's resolution, determining the time between increments.
- The prescaler frequency is calculated based on the clock rate and desired timing.

### Example Configuration
- **Setting Up Timer 0**:
  - Initial Timer Value: `TCNT0 = 0;`
  - Output Compare Register: `OCR0A = 249;` (for a 1 ms period)
  - Control Register: `TCCR0A = 0b01000010;`
  - Interrupt Mask Register: `TIMSK0 |= 0b10;`
  - Start Timer: `TCCR0B = 0b00000011;`

## Implementation/Examples

```c
#include <avr/io.h>
#include <avr/interrupt.h>

int count;

// Initialize Timer0
void InitTimer0(void) {
    TCNT0 = 0; // Set Initial Timer value
    OCR0A = 249; // Place TOP timer value to Output compare register
    TCCR0A = 0b01000010; // Set CTC mode and toggle OC0A on compare match
    TIMSK0 |= 0b10; // Enable interrupts
}

void StartTimer0(void) {
    TCCR0B = 0b00000011; // Set prescaler 64 and start timer
    sei(); // Enable global interrupts
}

void ledOn() {
    PORTB |= 0b00100000; // Turn LED on
}

void ledOff() {
    PORTB &= 0b11011111; // Turn LED off
}

// Toggle the LED
void toggleLED() {
    static int state = 1;
    if (state == 1) {
        ledOn();
        state = 0;
    } else {
        ledOff();
        state = 1;
    }
}

// Set up the ISR for TIMER0_COMPA
ISR(TIMER0_COMPA_vect) {
    count++;
    if ((count % 100) == 0) toggleLED(); // Toggle LED every 100 ms
}

int main(void) {
    DDRB |= 0b00100000; // Set LED pin for output
    count = 0;
    InitTimer0();
    StartTimer0();
    while (1) {
        // Do nothing
    }
}
```

> [!note] **Important**: Ensure that global interrupts are enabled using `sei();` to allow the ISR to function correctly.
> [!warning] **Caution**: When selecting prescaler values, ensure they align with the desired timing requirements to avoid timing inaccuracies.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[adc_handout_student]]
- [[Studio+GPIO_Programming_E+Lecture]]
- [[Midterm+Briefing]]