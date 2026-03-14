---
tags: [CG2111A, lecture-notes, academic]
---

# CG2111A Studio 5: Analog-to-Digital Converter (ADC)

## Overview
In this studio, students will explore the functionality of the Analog-to-Digital Converter (ADC) in the ATmega328P microcontroller. Building on previous experiences with analog devices, participants will learn to configure the ADC for bare-metal programming, unlocking its full potential beyond the limitations of the `analogRead` function. The studio includes hands-on activities involving flex sensors and LED control, emphasizing both polling and interrupt-driven methods for ADC operation.

## Key Concepts & Definitions
- **Analog-to-Digital Converter (ADC)**: A device that converts continuous analog signals into discrete digital values.
- **Bare-metal programming**: Writing software that interacts directly with hardware without an operating system.
- **Polling**: A method where the program repeatedly checks the status of a device to determine if it is ready for action.
- **Interrupt-driven**: A method where the device signals the processor when it is ready, allowing the processor to perform other tasks in the meantime.
- **Flex Sensor**: A variable resistor that changes resistance based on bending, used to measure physical deformation.
- **Power Reduction Register (PRR)**: A control register that manages power consumption by enabling or disabling peripheral modules.
- **ADC Control and Status Register A (ADCSRA)**: The primary control register for the ADC, used to enable the ADC and configure settings.
- **ADC Multiplexer Selection (ADMUX)**: A register that selects the input channel and reference voltage for the ADC.

## Detailed Technical Breakdown

### 1. Introduction to ADC
- The ADC allows microcontrollers to interpret analog signals from the environment.
- It converts continuous signals (e.g., temperature, light) into digital values for processing.

### 2. Relationship Between ADC and PWM
- **PWM (Pulse Width Modulation)**: A technique to simulate analog output using digital signals.
- The ADC digitizes analog input, while PWM generates an analog-like effect from digital signals.

### 3. Power Management
#### 3.1 Power Reduction Register (PRR)
- Controls power to peripheral modules.
- To enable the ADC, clear the PRADC bit in the PRR.

#### 3.2 ADCSRA Register
- Enables the ADC and configures the prescaler for clock speed.
- Set the ADEN bit to enable the ADC.

### 4. Configuring the ADC
#### 4.1 ADMUX Register
- Selects the input channel and reference voltage.
- Input channels: ADC0 to ADC5 correspond to A0 to A5 on Arduino Uno.

#### 4.2 Reference Voltage Selection
- Common choice: AVCC (5V supply).
- Set REFS1 = 0 and REFS0 = 1 for AVCC reference.

### 5. Starting ADC Conversion
- Trigger conversion by setting the ADSC bit in the ADCSRA register.

### 6. Waiting for Conversion Completion
#### 6.1 Polling Method
- Continuously check the ADSC bit status.

#### 6.2 Interrupt-Driven Method
- Configure ADC to generate an interrupt upon conversion completion.

### 7. Reading the ADC Result
- Results are stored in ADCL (low byte) and ADCH (high byte).
- **Important**: Always read ADCL first to avoid overwriting data.

### 8. Summary of Registers Used
| Register | Purpose |
|----------|---------|
| PRR      | Power management: clear PRADC to power on the ADC module. |
| ADCSRA   | ADC control/status: enable ADC, start conversion, enable interrupt, check completion, set prescaler. |
| ADMUX    | ADC configuration: select reference voltage and input channel (e.g., ADC0/A0). |
| ADCL     | ADC data low byte. Read this first before ADCH. |
| ADCH     | ADC data high byte. Read after ADCL, then combine to form the full 10-bit ADC reading. |

## Implementation/Examples
```c
// Example code to initialize and read from ADC
void setup() {
    // Enable ADC
    PRR &= ~(1 << PRADC); // Clear PRADC to enable ADC
    ADCSRA |= (1 << ADEN); // Set ADEN to enable ADC
    ADMUX = (1 << REFS0); // Set reference voltage to AVCC
}

void loop() {
    // Start ADC conversion
    ADCSRA |= (1 << ADSC); // Set ADSC to start conversion
    while (ADCSRA & (1 << ADSC)); // Wait for conversion to complete

    // Read ADC result
    uint16_t result = ADC; // Combine ADCL and ADCH
}
```

> [!note] **Important**: Always read ADCL before ADCH to avoid data corruption.
> [!warning] **Caution**: Ensure the ADC is enabled before attempting to read values.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[adc_handout_student]]
- [[Logic - Propositional Logic]]
- [[Tutorial+1+Solution]]
- [[Midterm+Briefing]]