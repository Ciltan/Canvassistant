---
tags: [CG2111A, lecture-notes, academic]
---

# CG2111A Studio 9: Getting Started with Raspberry Pi

## Overview
This studio session provides a comprehensive guide to setting up the Raspberry Pi 4, including installing the Raspberry Pi OS, connecting to Wi-Fi, and configuring a VPN for remote access. Participants will also learn to utilize the Pi Camera for remote photography. By the end of this session, teams will be equipped to collaborate on their projects from anywhere in the world.

## Key Concepts & Definitions
- **Raspberry Pi**: A small, affordable single-board computer designed for educational purposes and hobbyist projects. 
- **Raspberry Pi OS**: The official operating system for Raspberry Pi devices.
- **VPN (Virtual Private Network)**: A technology that creates a secure connection over the internet, allowing remote access to devices.
- **Tailscale**: A user-friendly VPN service based on the [[WireGuard]] protocol, facilitating secure connections between devices.
- **SSH (Secure Shell)**: A protocol for securely accessing and managing devices over a network.

## Detailed Technical Breakdown

### Equipment Needed
| Item                                         | Quantity |
|----------------------------------------------|----------|
| Raspberry Pi 4                               | x1       |
| Raspberry Pi 4 Case (may not be issued)     | x1       |
| 16 GB microSD card with adapter              | x1       |
| Micro HDMI to HDMI cable                     | x1       |
| HDMI to USB video capture dongle            | x1       |
| USB-A to USB-C Power cable                  | x1       |
| Raspberry Pi Camera Module                   | x1       |
| Keyboard, Mouse, and Laptop (Your Own)      | x1       |
| Wi-Fi Access or Hotspot (Your Own)          | x1       |
| SD card reader (optional)                    | x1       |

### Setting Up the Raspberry Pi Case
- **Importance of the Case**: Protects the Raspberry Pi board from damage and dust accumulation.
- **Assembly Steps**:
  1. Place the Pi board into the bottom half of the case.
  2. Attach heatsinks to designated chips.
  3. Install case fans into the top half of the case.
  
> [!warning] **Caution**: Do not screw the case shut until all configurations are complete.

### Booting Up the Raspberry Pi
1. Insert the microSD card into the Raspberry Pi.
2. Connect peripherals (HDMI, keyboard, mouse).
3. Power the device using a USB-C power cable.

> [!note] **Troubleshooting**: If the Pi does not respond, check power connections and HDMI setup.

### First Time Boot Configuration
- Set Country, Timezone, and Language.
- Create a username and password.
- Connect to Wi-Fi and update software.

### Setting Up Your Own VPN
1. **Creating a Tailscale Account**:
   - Sign up on the Tailscale website.
   - Download and install the Tailscale client on your laptop.
   
2. **Installing Tailscale on Raspberry Pi**:
   - Open a terminal and run:
     ```bash
     sudo apt-get update
     sudo apt-get upgrade
     curl -fsSL https://tailscale.com/install.sh | sh
     sudo tailscale up
     ```
   - Authenticate your Raspberry Pi on the Tailscale dashboard.

> [!important] **Team Collaboration**: Ensure all team members create Tailscale accounts for remote access.

### Testing the Tailscale Connection via SSH
- Enable SSH on the Raspberry Pi:
  ```bash
  sudo raspi-config
  ```
- Obtain the Tailscale IP address from the dashboard and SSH into the Raspberry Pi from your laptop.

## Implementation/Examples
```bash
# Update and install Tailscale
sudo apt-get update
sudo apt-get upgrade
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up
```

## Related
- [[adc_handout_student]]
- [[Studio+GPIO_Programming_E+Lecture]]
- [[AY2122+Sem1+Homework+1(S)]]
- [[AY2122+Sem2+Homework+3(S)]]
- [[CS1231+TUTORIAL+3]]