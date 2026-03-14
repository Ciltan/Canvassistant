---
tags: [CG2111A, lecture-notes, academic]
---

# CG2111A Studio 4: Pulse Width Modulation (PWM)

## Overview
In this studio, students will explore Pulse Width Modulation (PWM), a crucial technique in embedded systems for simulating analog signals using digital outputs. PWM is widely utilized for controlling devices such as LEDs, motors, and servos by varying the duty cycle and period of the signal. Participants will generate PWM signals using the ATmega328P timers, enhancing their understanding of signal manipulation in practical applications.

## Key Concepts & Definitions
- **Pulse Width Modulation (PWM)**: A method of controlling the width of pulses in a digital signal to simulate varying levels of power.
- **Duty Cycle**: The percentage of one period in which a signal is active (HIGH).
- **Period**: The total time taken for one complete cycle of the PWM signal.
- **ATmega328P**: A microcontroller used in Arduino boards, capable of generating PWM signals.
- **Analog Discovery (AD2/AD3)**: Tools used for analyzing and visualizing waveforms.

## Detailed Technical Breakdown

### 1. PWM Concepts
- **Digital Signal Generation**: PWM simulates analog signals by toggling between HIGH (1) and LOW (0) states.
- **Key Parameters**:
  - **Duty Cycle (%)**: 
    \[
    \text{Duty Cycle} = \left(\frac{\text{ON Time}}{\text{Period}}\right) \times 100
    \]
  - **Average Analog Signal (V)**:
    \[
    \text{Average Signal} = \text{Duty Cycle} \times V_{CC}
    \]

### 2. ATmega328P’s PWM Programming
- **Timer/Counter Configuration**: Utilize the 8-bit Timer/Counter to control PWM signal duration.
- **Clock Source Selection**: Configure the Timer/Counter Control Register (TCCRnB) to select the clock source.
- **Duty Cycle Setting**: Use the Output Compare Register (OCRnA) to define the duty cycle.

#### 2.1 Selecting the Clock Source (TCCRnB)
- Configure Clock Select bits to determine the PWM frequency.

#### 2.2 Setting the Duty Cycle (OCRnA)
- The duty cycle is set by comparing the TCNTn register with the OCRnx register.

#### 2.3 Generating Interrupts During PWM (TIMSKn)
- Enable interrupts for output compare events to adjust PWM signals dynamically.

#### 2.4 Selecting the Desired PWM Mode (TCCRnA)
- Choose between Fast PWM and Phase-Correct PWM; the latter is preferred for motor control.

### 3. Analyzing PWM Waveform using AD2/AD3
- Steps to set up the Waveforms Software for PWM analysis:
  1. Launch the software and select "Scope."
  2. Connect the AD2/AD3 to the PWM pin and ground.
  3. Adjust settings to visualize the PWM waveform.

## Implementation/Examples
```c
// Example code for generating PWM on Arduino
void setup() {
  pinMode(6, OUTPUT); // Set pin 6 as output
  TCCR0A = (1 << WGM00) | (1 << WGM01) | (1 << COM01); // Phase-Correct PWM
  TCCR0B = (1 << CS01); // Set prescaler to 8
  OCR0A = 191; // Set duty cycle to 75%
}

void loop() {
  // Main loop does nothing, PWM is handled by hardware
}
```

> [!note] **Important**: Ensure to read the ATmega328P datasheet for detailed register configurations and capabilities.
> [!warning] **Caution**: Incorrect settings in the Timer/Counter registers can lead to unexpected behavior in PWM signal generation.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[adc_handout_student]]
- [[lec04a]]
- [[ch2]]
- [[lec04b]]
- [[Logic - Propositional Logic]]
- [[Tutorial+1+Solution]]
- [[MA1508E+AY2122Sem1]]
- [[Midterm+Briefing]]