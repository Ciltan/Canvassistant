---
tags: [CG2111A, ADC, analog, ATmega328P, bare-metal]
---

# Analog-to-Digital Converter (ADC)

## Overview

The Analog-to-Digital Converter (ADC) built into the ATmega328P converts continuous analog voltage signals into discrete digital values that the microcontroller can process. The ADC is the complement to [[03_PWM]] -- while PWM produces analog-like **output** from digital signals, the ADC captures analog **input** from the environment (e.g., sensors for temperature, light, flex).

Previously, `analogRead()` was used in Arduino, but it is a **blocking** function. Bare-metal ADC programming unlocks polling and interrupt-driven approaches.

## Key Features

| Feature | Detail |
|---|---|
| Resolution | 10-bit (values 0--1023) |
| Type | Successive Approximation |
| Conversion time | 13 ADC clock cycles |
| Channels | 8 total (only **6 available** on Arduino Uno DIP package: ADC0--ADC5) |
| Input pins | A0--A5 on Arduino Uno |
| Voltage range | 0V to V_ref (typically 5V) |

## ADC Concepts

### Sampling

Sampling takes snapshots of a continuous analog signal at regular intervals.

> [!important] Nyquist Sampling Theorem
> You must sample at **at least twice** the highest frequency component of the signal.
> $$f_{sample} \geq 2 \times f_{max}$$
> Example: Human voice (20 Hz -- 4 kHz) requires sampling at minimum 8 kHz.

### Quantization and Encoding

The sampled analog voltage is mapped to one of $2^b$ discrete levels, where $b$ is the bit resolution.

$$\text{Resolution} = \frac{V_{ref\,high} - V_{ref\,low}}{2^b}$$

For the ATmega328P with 10-bit ADC and 5V reference:

$$\text{Resolution} = \frac{5V}{2^{10}} = \frac{5}{1024} \approx 4.88\text{ mV per level}$$

### ADC Value to Voltage Conversion

$$V_{in} = \frac{ADC\_value \times V_{ref}}{1024}$$

Or equivalently:

$$ADC\_value = \frac{V_{in} \times 1024}{V_{ref}}$$

## Registers

### Power Reduction Register (PRR) -- Address 0x64

| Bit | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|---|---|---|---|---|---|---|---|---|
| Name | PRTWI0 | PRTIM2 | PRTIM0 | -- | PRTIM1 | PRSPI0 | PRUSART0 | **PRADC** |
| Reset | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

- **PRADC (bit 0)**: Write `0` to power ON the ADC; write `1` to disable it (saves power)
- Must clear PRADC before using the ADC

```c
// Enable power to ADC
PRR &= 0b11111110;  // Clear bit 0 (PRADC)
```

### ADCSRA -- ADC Control and Status Register A (Address 0x7A)

| Bit | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|---|---|---|---|---|---|---|---|---|
| Name | **ADEN** | **ADSC** | ADATE | ADIF | **ADIE** | **ADPS2** | **ADPS1** | **ADPS0** |
| Reset | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

| Bit | Name | Description |
|---|---|---|
| 7 | ADEN | ADC Enable. Set to `1` to turn on ADC. Clearing it mid-conversion aborts. |
| 6 | ADSC | ADC Start Conversion. Set to `1` to begin. Automatically clears to `0` when done. |
| 5 | ADATE | ADC Auto Trigger Enable |
| 4 | ADIF | ADC Interrupt Flag. Set when conversion completes. |
| 3 | ADIE | ADC Interrupt Enable. Set to `1` to trigger ISR on conversion complete. |
| 2:0 | ADPS[2:0] | Prescaler select bits (see table below) |

#### Prescaler Selection

| ADPS2 | ADPS1 | ADPS0 | Division Factor |
|---|---|---|---|
| 0 | 0 | 0 | 2 |
| 0 | 0 | 1 | 2 |
| 0 | 1 | 0 | 4 |
| 0 | 1 | 1 | 8 |
| 1 | 0 | 0 | 16 |
| 1 | 0 | 1 | 32 |
| 1 | 1 | 0 | 64 |
| 1 | 1 | 1 | 128 |

The sampling frequency depends on the prescaler $P$:

$$F_{sample} = \frac{F_{clk}}{13 \times P}$$

where 13 is the number of ADC clock cycles per conversion.

> [!note] Prescaler Selection Strategy
> - Smaller prescaler = higher sampling frequency (but more power)
> - Larger prescaler = lower sampling frequency (saves power)
> - Pick the **largest** prescaler that still meets the Nyquist requirement
> - ADC operates best with clock between **50 kHz and 200 kHz**

**Example**: Signal with max frequency 12 kHz requires $f_s \geq 24$ kHz.

$$P \leq \frac{16{,}000{,}000}{13 \times 24{,}000} = 51.28$$

Largest valid prescaler $\leq 51.28$ is **32** (ADPS = `101`).

Actual sampling frequency: $\frac{16{,}000{,}000}{13 \times 32} \approx 38.46$ kHz

**Common choice**: Prescaler 128 gives ADC clock = 125 kHz, sampling rate ~ 9.62 kHz.

```c
// Enable ADC, prescaler = 128
ADCSRA = 0b10000111;
// Enable ADC, prescaler = 32
ADCSRA = 0b10000101;
```

### ADMUX -- ADC Multiplexer Selection Register (Address 0x7C)

| Bit | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|---|---|---|---|---|---|---|---|---|
| Name | **REFS1** | **REFS0** | ADLAR | -- | MUX3 | **MUX2** | **MUX1** | **MUX0** |
| Reset | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

#### Reference Voltage Selection (REFS[1:0])

| REFS1 | REFS0 | Voltage Reference |
|---|---|---|
| 0 | 0 | AREF pin, internal V_ref off |
| 0 | 1 | **AVcc** with external capacitor at AREF pin (most common) |
| 1 | 0 | Reserved |
| 1 | 1 | Internal 1.1V reference with external capacitor at AREF |

> [!note]
> On the Arduino Uno, AVcc is connected to Vcc (5V) through a capacitor, so `REFS[1:0] = 01` is the standard choice.

#### Channel Selection (MUX[3:0])

| Channel | MUX3 | MUX2 | MUX1 | MUX0 | Arduino Pin |
|---|---|---|---|---|---|
| ADC0 | 0 | 0 | 0 | 0 | A0 |
| ADC1 | 0 | 0 | 0 | 1 | A1 |
| ADC2 | 0 | 0 | 1 | 0 | A2 |
| ADC3 | 0 | 0 | 1 | 1 | A3 |
| ADC4 | 0 | 1 | 0 | 0 | A4 |
| ADC5 | 0 | 1 | 0 | 1 | A5 |

```c
// AVcc reference, channel 0 (A0)
ADMUX = 0b01000000;
// AVcc reference, channel 2 (A2)
ADMUX = 0b01000010;
```

### ADC Data Registers (ADCL and ADCH)

**ADCL** -- Lower 8 bits (ADC7:ADC0), read-only.
**ADCH** -- Upper 2 bits (ADC9:ADC8) in bits 1:0, read-only.

> [!warning] Always Read ADCL First!
> Reading ADCH allows the ADC to overwrite **both** ADCL and ADCH with new values. If you read ADCH before ADCL, you may lose data.

```c
uint8_t loval = ADCL;   // Read low byte FIRST
uint8_t hival = ADCH;   // Then read high byte
uint16_t adcval = (hival << 8) | loval;
```

## Programming Procedure

### Step-by-Step (Polling)

1. **Power on the ADC**: Clear PRADC bit in PRR
2. **Enable ADC + set prescaler**: Configure ADCSRA (set ADEN, ADPS bits)
3. **Select channel and reference**: Configure ADMUX (set REFS, MUX bits)
4. **Start conversion**: Set ADSC bit in ADCSRA
5. **Wait for completion**: Poll ADSC bit until it returns to 0
6. **Read result**: Read ADCL first, then ADCH, combine into 10-bit value
7. Repeat from step 4 as needed

### Complete Polling Example

```c
#define PB5MASK  0b00100000
#define ADSCMASK 0b01000000

void setup() {
    // Step 1: Power on ADC
    PRR &= 0b11111110;

    // Step 2: Enable ADC, prescaler = 32
    ADCSRA = 0b10000101;

    // Step 3: AVcc reference, channel 0
    ADMUX = 0b01000000;

    // Set LED pin (PB5 / pin 13) as output
    DDRB |= PB5MASK;
}

void toggleLED() {
    static int flag = 1;
    if (flag) {
        PORTB |= PB5MASK;
    } else {
        PORTB &= ~PB5MASK;
    }
    flag = 1 - flag;
}

void loop() {
    // Step 4: Start conversion
    ADCSRA |= ADSCMASK;

    // Step 5: Wait for conversion to complete
    while (ADCSRA & ADSCMASK);

    // Step 6: Read the result
    int loval = ADCL;
    int hival = ADCH;
    int adcval = (hival << 8) + loval;

    toggleLED();
    delay(adcval);
}
```

### Interrupt-Driven Approach

Instead of polling, the ADC can trigger an interrupt when conversion completes. This frees the CPU to do other work.

**Setup differences**:
- Set **ADIE** (bit 3) in ADCSRA to enable ADC interrupt
- Call `sei()` to enable global interrupts
- Set ADSC to start conversion
- Define `ISR(ADC_vect)` to handle the result

```c
void setup() {
    PRR &= 0b11111110;

    // Enable ADC, interrupt enable, prescaler = 128
    ADCSRA = 0b10001111;  // ADEN=1, ADIE=1, ADPS=111

    ADMUX = 0b01000000;   // AVcc, channel 0

    sei();  // Enable global interrupts

    // Start first conversion
    ADCSRA |= 0b01000000;
}

ISR(ADC_vect) {
    // Read ADC result
    int loval = ADCL;
    int hival = ADCH;
    int adcval = (hival << 8) | loval;

    // Process adcval (e.g., control LED)
    // ...

    // Start next conversion
    ADCSRA |= 0b01000000;
}

void loop() {
    // CPU is free to do other work here
}
```

> [!important] Polling vs Interrupt-Driven
> - **Polling**: CPU busy-waits during conversion (~104 us at prescaler 128). Simpler but blocks execution.
> - **Interrupt**: CPU is free during conversion. The ISR fires automatically when the result is ready. Preferred for real-time systems.
> - Interrupt-driven produces **different LED frequencies** than polling because the CPU does not waste cycles waiting.

## Studio Activities Summary

### Flex Sensor Circuit

The flex sensor is a variable resistor (resistance changes when bent). In a voltage divider with a fixed resistor $R_{fixed}$:

$$V_{A0} = \frac{R_{flex}}{R_{flex} + R_{fixed}} \times V_{cc}$$

| Resistor Value | Effect |
|---|---|
| 1.2 k | Very low compared to flex sensor (~25k--100k), so voltage barely changes |
| 12 k | Moderate range |
| **22 k** | Good range -- **recommended for activities** |
| 39 k | Narrower range at higher voltages |

> [!note] Why 1.2k gives poor results
> When $R_{fixed}$ is much smaller than $R_{flex}$, the voltage divider output stays close to Vcc regardless of flex, giving minimal ADC range.

### Activity 4: ADC + PWM Integration

Combine ADC reading with PWM to control LED brightness based on flex sensor bending:
1. Read 10-bit ADC value (0--1023)
2. Remap to 8-bit PWM range (0--255) for OCR0A
3. Expand the range based on actual sensor min/max readings

```c
// Example mapping: scale ADC range to full 0-255
uint8_t pwm_val = map(adcval, adc_min, adc_max, 0, 255);
OCR0A = pwm_val;
```

## Register Summary Table

| Register | Address | Purpose |
|---|---|---|
| PRR | 0x64 | Power management -- clear PRADC (bit 0) to power on ADC |
| ADCSRA | 0x7A | Control/status -- enable ADC, start conversion, prescaler, interrupt |
| ADMUX | 0x7C | Configuration -- reference voltage and input channel selection |
| ADCL | -- | Data low byte (read first!) |
| ADCH | -- | Data high byte (read second) |

## Related Notes

- [[01_GPIO]] - Digital I/O using DDRx, PORTx, PINx registers
- [[03_PWM]] - Analog output via Pulse Width Modulation (inverse of ADC)
- [[04_Timers]] - Timer modules used for PWM generation and prescaler concepts
- [[05_Interrupts]] - Interrupt-driven ADC uses the ISR mechanism
