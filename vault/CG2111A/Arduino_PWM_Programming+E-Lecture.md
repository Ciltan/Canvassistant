---
tags: [CG2111A, lecture-notes, academic]
---

# Arduino PWM Programming

## Overview
This lecture focuses on generating Pulse Width Modulation (PWM) signals using the Arduino platform, specifically through the Atmega microcontroller. PWM allows for the encoding of analog values by varying the duty cycle, which is the proportion of time a signal is high versus low. The lecture covers the configuration of timers, the calculation of prescaler values, and the implementation of phase-correct PWM for smoother motor control.

## Key Concepts & Definitions
- **PWM**: [[Pulse Width Modulation]] is a technique used to encode analog values into digital signals by varying the duty cycle.
- **Duty Cycle (D)**: The ratio of "on" time to the total time period, expressed as a percentage.
- **Atmega**: The microcontroller used in Arduino boards that supports PWM generation.
- **Prescaler**: A factor that divides the clock frequency to achieve the desired PWM frequency.
- **Timer/Counter Register (TCCR0B)**: A register used to configure the timer settings for PWM.
- **OCR0A Register**: The Output Compare Register that determines the duty cycle of the PWM signal.

## Detailed Technical Breakdown

### PWM Generation
- PWM is generated using timers on the Atmega microcontroller.
- Two modes of PWM:
  - **Fast PWM**: Allows higher frequencies.
  - **Phase Correct PWM**: Provides symmetric waveforms, ideal for motor control.

### Frequency and Prescaler Calculation
- Desired frequency example: 500 Hz.
- Formula for prescaler (N):
  - \( N = \frac{f_{clk}}{f_{PWM}} \)
- For \( f_{clk} = 16 \text{ MHz} \):
  - \( N = \frac{16,000,000}{500} = 32,000 \)
- Closest prescaler value: 64, resulting in \( f_{PWM} \approx 490 \text{ Hz} \).

### Timer Configuration
- The Timer/Counter can be clocked by an internal or external source.
- The clock source is selected by writing to the Clock Select bits in TCCR0B.
- The TCNTn register increments based on the desired frequency.

### Duty Cycle Calculation
- Duty cycle is determined by the value in the OCR0A register.
- Example for generating 3.5V in a 5V system:
  - Duty Cycle = \( \frac{3.5V}{5V} \times 100\% = 70\% \)
  - Corresponding OCR0A value for 70% duty cycle: 179.

### Interrupts
- The timer can generate interrupts for Output Compare or TCNT0 rollover.
- Example code to enable interrupts:
  ```c
  TIMSK0 |= 0b10; // Enables OCIE0A IRQ
  ```

### Phase Correct PWM Configuration
1. Load initial count:
   ```c
   TCNT0 = 0; // Set initial count to 0
   ```
2. Load desired value into OCR0A:
   ```c
   OCR0A = 128; // For 50% duty cycle
   ```
3. Configure WGM[2:0] bits in TCCR0A/B for PWM mode.
4. Set COM0A1:0 to 0b10 to control output behavior.

## Implementation/Examples
```c
// Example code for Phase Correct PWM
void setup() {
    // Set Fast PWM mode
    TCCR0A = 0b10000001; // Configure TCCR0A for Phase Correct PWM
    // Set prescaler to 64
    TCCR0B = 0b00000010; // Configure TCCR0B
    // Set OCR0A for desired duty cycle
    OCR0A = 128; // 50% duty cycle
    // Enable interrupts
    TIMSK0 |= 0b10; // Enable OCIE0A IRQ
}

void loop() {
    // Main loop code
}
```

> [!note] **Important Note**: Always ensure that the prescaler and frequency settings are compatible with your application to avoid unexpected behavior in PWM output.
> [!warning] **Caution**: Incorrect configurations of the Timer/Counter registers can lead to undesired PWM signals, potentially damaging connected components.

## Related
- [[Studio+GPIO_Programming_E+Lecture]]
- [[adc_handout_student]]
- [[Interrupts]]
- [[AY2122+Sem1+Homework+1(S)]]