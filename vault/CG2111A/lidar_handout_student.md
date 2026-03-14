---
tags: [CG2111A, lecture-notes, academic]
---

# CG2111A Studio 11: LIDAR Programming

## Overview
This studio focuses on integrating the SLAMTEC RPLidar A1M8 sensor with a Raspberry Pi to enhance remote sensing capabilities. Students will establish a remote connection, set up a Python programming environment, and utilize the LIDAR sensor to scan and visualize their surroundings. This hands-on experience is crucial for developing skills necessary for the final robot project.

## Key Concepts & Definitions
- **LIDAR**: [[Light Detection and Ranging]], a remote sensing technology that measures distances using laser pulses.
- **Raspberry Pi**: A small, affordable computer used for programming and interfacing with sensors.
- **USART**: [[Universal Synchronous/Asynchronous Receiver-Transmitter]], a communication protocol used for serial communication.
- **Python**: A high-level programming language known for its readability and ease of use.
- **SSH**: [[Secure Shell]], a protocol for securely accessing network services over an unsecured network.

## Detailed Technical Breakdown

### Learning Objectives
1. Establish a remote SSH connection to the Raspberry Pi.
2. Set up the Python programming environment for LIDAR interaction.
3. Understand LIDAR sensor operation and communication protocols.
4. Acquire and interpret LIDAR scan data using Python libraries.
5. Visualize LIDAR scan data as a 2D map.

### Equipment Needed
| Item                                         | Quantity |
|----------------------------------------------|----------|
| SLAMTEC RPLidar A1M8 + USB-to-Serial Adapter + USB Cable | ×1       |
| Raspberry Pi + Power Cable                   | ×1       |
| Laptops with Tailscale installed             | ×1       |

### Background Knowledge
- **Sensing with LIDARs**: LIDAR sensors measure distances using laser beams, providing faster and more accurate measurements compared to ultrasonic sensors.
- **Communicating with the LIDAR Sensor**: The Raspberry Pi communicates with the LIDAR via USB, using commands defined in the RPLidar Communication Protocol.
- **Processing LIDAR Output**: LIDAR outputs angles and distances, which can be processed to visualize the environment.

### Python Programming on the Raspberry Pi
- **Development Environments**: Use tools like `pip` for package management and `virtualenv` for isolating project dependencies.
- **Reading Source Code and Documentation**: Focus on high-level function interfaces when learning new libraries.

## Implementation/Examples

### Activity 1: Access the Raspberry Pi Remotely
```bash
ssh <USERNAME>@<IP_ADDRESS>
```
- Ensure Tailscale is running on both devices.

### Activity 2: Setup the Programming Environment
1. Transfer the `alex` folder:
   ```bash
   scp -r ./alex <USERNAME>@<IP_ADDRESS>:~/alex
   ```
2. Install dependencies:
   ```bash
   cd ~/alex
   chmod +x ./setup_environment.sh
   sudo ./setup_environment.sh
   source ./env/bin/activate
   ```

### Activity 3: LIDAR: Initial Connection
1. **Hardware Setup**:
   - Connect the LIDAR to the Raspberry Pi using the USB-to-Serial Adapter.
2. **Check LIDAR Status**:
   ```bash
   python ./labs/lidarLab/lidar_example_connect.py
   ```

> [!note] Ensure all connections are secure and the LIDAR is powered on before running the connection script.
> [!warning] Always activate the virtual environment before running Python scripts to avoid dependency issues.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[adc_handout_student]]
- [[Logic - Propositional Logic]]
- [[Matlab+for+Engineering]]