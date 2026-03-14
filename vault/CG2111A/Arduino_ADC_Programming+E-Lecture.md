---
tags: [CG2111A, lecture-notes, academic]
---

# Arduino ADC Programming

## Overview
This lecture focuses on the implementation of analog input using the analog-to-digital converter (ADC) integrated into the Atmega328P microcontroller. Building on previous knowledge of digital input/output and PWM, we will explore the ADC's key features, programming procedures, and practical applications. Understanding these concepts is essential for effectively utilizing the ADC in various projects.

## Key Concepts & Definitions
- **Analog-to-Digital Converter (ADC)**: A device that converts an analog signal into a digital signal.
- **Sampling**: The process of taking snapshots of an analog signal over time to reconstruct the original signal.
- **Nyquist Sampling Rate**: The minimum sampling frequency required to accurately capture a signal, which is at least twice the highest frequency of the signal.
- **Quantization**: The process of mapping input voltage signals into discrete levels.
- **Resolution**: The smallest change in voltage that can be detected by the ADC.
- **Prescaler**: A circuit that divides the frequency of the ADC clock to set the sampling frequency.

## Detailed Technical Breakdown

### ADC Key Features
- **10-bit Successive Approximation ADC**: Provides 1024 discrete levels.
- **13 Cycle Conversion Time**: Time taken to convert an analog signal to a digital value.
- **8-Channel Analog Multiplexer**: Allows for eight single-ended voltage inputs, though only six are available on the DIP package for the Uno board.

### Sampling
- **Snapshot Process**: Capture the analog signal at specific intervals.
- **Frequency Considerations**: The rate of change of the signal determines the necessary sampling frequency.
- **Example**: For a human voice signal (20Hz – 4kHz), a minimum sampling rate of 8 kHz is required.

### Quantization & Encoding
- **Input Voltage Range**: Typically 0-5 volts.
- **Quantization Levels**: Determined by the number of bits (b) used, where 2^b levels are created.
- **Example**: A 2-bit representation in a 5-volt range results in a resolution of 1.25 volts.

### Programming Procedure
1. **Activate Power to the ADC**: Write a “0” to bit 0 (ADC) of the Power Reduction Register PRR.
2. **Switch on the ADC**: Write a “1” to bit 7 (ADEN) of the ADC Control and Status Register ADCSRA.
3. **Select Channel and Reference Voltage**: Configure in the ADC Multiplexer Register ADMUX.
4. **Start Conversion**: Write a “1” to bit 6 (ADSC) of ADCSRA.
5. **Wait for Conversion to End**: Poll bit 6 of ADCSRA until it becomes 0.
6. **Read Converted Value**: Combine bits from registers ADCL and ADCH.
7. **Repeat as Necessary**: Continue the process for the desired number of conversions.

### Power Reduction Register
- Used to conserve energy by turning off parts of the AT328P.
- To activate the ADC, write `PRR &= 0b11111110;`.

### Configuring the Prescaler
- The prescaler value affects the ADC's sampling frequency.
- For a maximum frequency component of 12 kHz, the minimal sampling frequency is 24 kHz.
- Choose the largest prescaler smaller than the calculated value (51.28), resulting in a prescaler of 32.

### Setting Up the ADMUX Register
- **Reference Voltage**: Set using REFS[1:0] bits.
- **Channel Selection**: Configure which channel to convert.
- Example for Channel 2: `ADMUX = 0b01000010;`.

### Starting the Conversion
- Set the ADSC bit in ADCSRA to initiate conversion: `ADCSRA |= 0b01000000;`.
- Loop until ADSC returns to 0, indicating the end of conversion.

### Reading the Result
- Read from ADCL and ADCH to obtain the converted value.
- **Important**: Always read ADCL first to avoid losing data.

## Implementation/Examples
```c
// Example code for ADC setup and reading
PRR &= 0b11111110; // Activate ADC
ADCSRA = 0b10000101; // Enable ADC and set prescaler
ADMUX = 0b01000010; // Set reference voltage and channel
ADCSRA |= 0b01000000; // Start conversion
while(ADCSRA & 0b01000000); // Wait for conversion to complete
loval = ADCL; // Read low byte
hival = ADCH; // Read high byte
adcval = (hival << 8) + loval; // Combine bytes
```

> [!note] Ensure to configure the ADC correctly to avoid erroneous readings.
> [!important] Always read ADCL before ADCH to prevent data loss during conversion.

## Related
- [[adc_handout_student]]
- [[Studio+GPIO_Programming_E+Lecture]]
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]