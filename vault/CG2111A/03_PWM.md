---
tags: [CG2111A, PWM, timers, analog-output, ATmega328P, bare-metal]
---

# Pulse Width Modulation (PWM)

## Overview

Pulse Width Modulation (PWM) is a digital technique used to simulate analog output by rapidly toggling a signal between HIGH and LOW states at a controlled frequency. By adjusting the proportion of time the signal is HIGH (the **duty cycle**), different effective analog voltages can be approximated. PWM is the inverse of [[02_ADC]] -- while ADC converts analog input to digital, PWM produces analog-like output from digital signals.

Common uses: controlling LED brightness, motor speed, and servo position.

## PWM Concepts

### Key Parameters

| Parameter | Definition |
|---|---|
| **Period** | Total duration of one complete PWM cycle (seconds) |
| **Frequency** | $f = \frac{1}{\text{Period}}$ (Hz) |
| **Duty Cycle** | Percentage of time signal is HIGH within one period |
| **Pulse Width** | Duration of the HIGH state (ON time) |

$$\text{Duty Cycle (\%)} = \frac{\text{ON Time (s)}}{\text{Period (s)}} \times 100\%$$

### Equivalent Analog Voltage

An analog device (e.g., LED) perceives PWM as an average voltage:

$$V_{avg} = \text{Duty Cycle (\%)} \times V_{CC}$$

**Example**: 75% duty cycle at 5V produces an effective voltage of 3.75V.

## PWM on the ATmega328P

PWM is generated using the hardware **timers** on the ATmega328P. There are two PWM types:

| Type | Description | Use Case |
|---|---|---|
| **Fast PWM** | Single-slope counting (0 to TOP), higher frequencies | General purpose |
| **Phase-Correct PWM** | Dual-slope counting (0 to TOP to 0), symmetric waveforms | **Motors** (smoother) |

> [!important]
> In CG2111A, we use **Phase-Correct PWM** because it produces symmetric waveforms better suited for motor control in the final project.

### How Phase-Correct PWM Works

1. Timer counter (TCNT0) counts **up** from 0 to 255 (TOP)
2. Then counts **down** from 255 to 0
3. Total cycle = 510 clock ticks (2 x 255)
4. Output pin is **cleared** (LOW) when TCNT0 matches OCR0A on the way up
5. Output pin is **set** (HIGH) when TCNT0 matches OCR0A on the way down

This creates a symmetric waveform centered around the midpoint.

## Programming Procedure

### Step 1: Select Clock Source (TCCR0B)

The prescaler determines the PWM frequency.

#### TCCR0B Register

| Bit | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|---|---|---|---|---|---|---|---|---|
| Name | FOC0A | FOC0B | -- | -- | WGM02 | CS02 | CS01 | CS00 |

#### Clock Select (CS0[2:0])

| CS02 | CS01 | CS00 | Description |
|---|---|---|---|
| 0 | 0 | 0 | No clock (Timer stopped) |
| 0 | 0 | 1 | clk/1 (No prescaling) |
| 0 | 1 | 0 | clk/8 |
| 0 | 1 | 1 | clk/64 |
| 1 | 0 | 0 | clk/256 |
| 1 | 0 | 1 | clk/1024 |
| 1 | 1 | 0 | External T0 pin, falling edge |
| 1 | 1 | 1 | External T0 pin, rising edge |

#### Phase-Correct PWM Frequency Formula (8-bit timer, TOP = 255)

$$f_{PWM} = \frac{f_{clk}}{N \times 2 \times \text{TOP}} = \frac{f_{clk}}{N \times 510}$$

Where $N$ is the prescaler factor and $f_{clk}$ = 16 MHz for Arduino Uno.

**Example**: Desired frequency ~490 Hz:

$$N = \frac{16{,}000{,}000}{510 \times 490} \approx 64$$

Set CS0[2:0] = `011` for prescaler 64. Actual frequency:

$$f_{PWM} = \frac{16{,}000{,}000}{64 \times 510} \approx 490 \text{ Hz}$$

### Step 2: Set Duty Cycle (OCR0A)

The duty cycle is controlled by the value in the Output Compare Register:

$$\text{Duty Cycle (\%)} = \frac{\text{OCR0A}}{255} \times 100\%$$

#### OCR0A Register (8-bit, R/W)

| Bit | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|---|---|---|---|---|---|---|---|---|
| Name | OCR0A[7:0] ||||||||

#### Duty Cycle Reference Table

| Desired Duty Cycle | Desired Voltage (5V) | OCR0A Value | Actual Voltage |
|---|---|---|---|
| 0% | 0V | 0 | 0V |
| 25% | 1.25V | 64 | ~1.255V |
| 50% | 2.5V | 128 | ~2.51V |
| 75% | 3.75V | 191 | ~3.745V |
| 100% | 5V | 255 | 5V |

To compute OCR0A for a desired voltage:

$$\text{OCR0A} = \frac{V_{desired} \times 255}{V_{CC}}$$

**Example**: For 3.5V output: $\text{OCR0A} = \frac{3.5 \times 255}{5} = 178.5 \approx 179$

### Step 3: Select PWM Mode (TCCR0A)

#### TCCR0A Register (Address 0x44)

| Bit | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|---|---|---|---|---|---|---|---|---|
| Name | COM0A1 | COM0A0 | COM0B1 | COM0B0 | -- | -- | WGM01 | WGM00 |

#### Waveform Generation Mode (WGM[2:0])

| Mode | WGM02 | WGM01 | WGM00 | Operation | TOP |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | Normal | 0xFF |
| **1** | **0** | **0** | **1** | **PWM, Phase Correct** | **0xFF** |
| 2 | 0 | 1 | 0 | CTC | OCRA |
| 3 | 0 | 1 | 1 | Fast PWM | 0xFF |
| 5 | 1 | 0 | 1 | PWM, Phase Correct | OCRA |
| 7 | 1 | 1 | 1 | Fast PWM | OCRA |

> [!note] Mode 1 vs Mode 5
> - **Mode 1**: TOP = 0xFF (255), fixed frequency, duty cycle via OCR0A
> - **Mode 5**: TOP = OCRA, allows variable frequency but OCR0A sets the period

#### Compare Output Mode (Phase-Correct PWM)

| COM0A1 | COM0A0 | Description |
|---|---|---|
| 0 | 0 | Normal port operation, OC0A disconnected |
| 0 | 1 | Toggle OC0A on Compare Match (WGM02=1 only) |
| **1** | **0** | **Clear OC0A on up-count match, Set on down-count match** |
| 1 | 1 | Set OC0A on up-count match, Clear on down-count match (inverted) |

> [!note] COM0A[1:0] = `10` is the standard choice.
> - Counting UP past OCR0A: output goes LOW
> - Counting DOWN past OCR0A: output goes HIGH
> - To generate the **complement** waveform, use COM0A[1:0] = `11`

### Step 4: (Optional) Enable Interrupts (TIMSK0)

#### TIMSK0 Register (Address 0x6E)

| Bit | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|---|---|---|---|---|---|---|---|---|
| Name | -- | -- | ICIE | -- | -- | OCIEB | **OCIEA** | TOIE |

- **OCIEA** (bit 1): Output Compare A Match Interrupt Enable
- **TOIE** (bit 0): Timer Overflow Interrupt Enable

```c
TIMSK0 |= 0b10;  // Enable OCIE0A interrupt
sei();            // Enable global interrupts
```

> [!note] Why no ISR needed for basic PWM?
> The hardware automatically generates the PWM waveform on the OC0A pin. An ISR is only needed if you want to **change** the duty cycle dynamically (e.g., fade effect).

## PWM Output Pin Mapping

The PWM output appears on the **OCnx** pins. Check the ATmega328P pinout:

| Timer | Output | ATmega Pin | Arduino Pin |
|---|---|---|---|
| Timer 0A | OC0A | PD6 (pin 12) | **Pin 6** |
| Timer 0B | OC0B | PD5 (pin 11) | Pin 5 |
| Timer 1A | OC1A | PB1 (pin 15) | **Pin 9** |
| Timer 1B | OC1B | PB2 (pin 16) | Pin 10 |
| Timer 2A | OC2A | PB3 (pin 17) | Pin 11 |
| Timer 2B | OC2B | PD3 (pin 5) | Pin 3 |

> [!warning]
> The OC0A pin **must** be set as an output using DDR for PWM to appear on the physical pin.
> ```c
> DDRD |= (1 << PD6);  // Set Pin 6 as output for OC0A
> ```

## Complete Code Example (Timer 0, Phase-Correct PWM)

```c
void setup() {
    // Set OC0A (PD6 / Arduino Pin 6) as output
    DDRD |= 0b01000000;

    // Phase-Correct PWM Mode 1, Clear OC0A on up-count match
    TCCR0A = 0b10000001;  // COM0A1=1, COM0A0=0, WGM01=0, WGM00=1

    // Prescaler = 64, WGM02 = 0
    TCCR0B = 0b00000011;  // CS0[2:0] = 011

    // Initial counter value
    TCNT0 = 0;

    // Set 75% duty cycle
    OCR0A = 191;

    // Optional: enable interrupt for dynamic duty cycle changes
    // TIMSK0 |= 0b10;
    // sei();
}

void loop() {
    // PWM runs automatically in hardware
    // No code needed here for static duty cycle
}
```

## Using Timer 1 (16-bit) for Servo Control

An 8-bit timer cannot produce 50 Hz PWM because the lowest achievable frequency with prescaler 1024 is:

$$f = \frac{16{,}000{,}000}{1024 \times 510} \approx 30.6 \text{ Hz (too low)}$$

And with prescaler 256:

$$f = \frac{16{,}000{,}000}{256 \times 510} \approx 122.5 \text{ Hz (too high)}$$

Neither is close to 50 Hz, so we use the **16-bit Timer 1** which allows a configurable TOP value.

### Timer 1 Phase-Correct PWM Formula

$$\text{TOP} = \frac{f_{clk}}{N \times 2 \times f_{PWM}}$$

For 50 Hz with prescaler $N = 8$:

$$\text{TOP} = \frac{16{,}000{,}000}{8 \times 2 \times 50} = 20{,}000$$

The TOP value is loaded into the **ICR1** register.

### Servo Pulse Width to OCR1A

Servos require specific pulse widths within a 20 ms period:

| Position | Pulse Width | OCR1A Value |
|---|---|---|
| 0 degrees | ~1.0 ms | $\frac{1.0}{20} \times 20000 = 1000$ |
| 90 degrees (mid) | ~1.5 ms | $\frac{1.5}{20} \times 20000 = 1500$ |
| 180 degrees | ~2.0 ms | $\frac{2.0}{20} \times 20000 = 2000$ |

```c
void setup() {
    // Set OC1A (PB1 / Arduino Pin 9) as output
    DDRB |= (1 << PB1);

    // Phase-Correct PWM, TOP = ICR1
    // COM1A1=1 (clear on up-count match)
    TCCR1A = 0b10000010;  // COM1A1=1, WGM11=1, WGM10=0

    // WGM13=1, WGM12=0, Prescaler = 8
    TCCR1B = 0b00010010;  // WGM13=1, CS1[2:0]=010

    // Set TOP for 50 Hz
    ICR1 = 20000;

    // Set servo to middle position (1.5 ms)
    OCR1A = 1500;

    TCNT1 = 0;
}

void loop() {
    // Sweep servo from 0 to 180 degrees
    for (int pos = 1000; pos <= 2000; pos += 10) {
        OCR1A = pos;
        delay(20);
    }
    for (int pos = 2000; pos >= 1000; pos -= 10) {
        OCR1A = pos;
        delay(20);
    }
}
```

## LED Fade Effect with ISR

To create a fade in/fade out effect, change OCR0A inside the ISR:

```c
volatile int brightness = 0;
volatile int direction = 1;

ISR(TIMER0_COMPA_vect) {
    brightness += direction;
    if (brightness >= 255) {
        brightness = 255;
        direction = -1;
    } else if (brightness <= 0) {
        brightness = 0;
        direction = 1;
    }
    OCR0A = brightness;
}
```

> [!note] Slowing Down the Fade
> Change the prescaler to a larger value (e.g., from 64 to 1024) to reduce the ISR frequency, making the fade slower.

## Register Summary

| Register | Purpose |
|---|---|
| TCCR0A | PWM mode selection (WGM bits), compare output mode (COM bits) |
| TCCR0B | Clock source / prescaler selection (CS bits), WGM02 bit |
| TCNT0 | Timer counter value (initialize to 0) |
| OCR0A | Output Compare Register A -- sets the duty cycle |
| OCR0B | Output Compare Register B -- second PWM channel |
| TIMSK0 | Timer interrupt mask (enable OCIEA for compare match interrupt) |
| ICR1 | Input Capture Register (used as TOP for Timer 1 PWM) |

## Related Notes

- [[01_GPIO]] - Digital I/O pins, DDR configuration needed for PWM output pins
- [[02_ADC]] - Analog input (inverse of PWM); ADC + PWM together enable sensor-driven actuator control
- [[04_Timers]] - Timer architecture that underlies PWM generation
- [[05_Interrupts]] - ISR mechanism used for dynamic duty cycle changes
