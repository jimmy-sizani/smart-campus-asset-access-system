# Smart Campus Asset Access & Usage Logging System

A Raspberry Pi Pico/Pico W embedded prototype for controlling and monitoring access to shared campus equipment.

The system uses a 3 bit binary input to simulate user identification. Authorised codes can unlock a servo-controlled cabinet, while unauthorised attempts trigger denial feedback. Access attempts can be logged, equipment usage can be counted for maintenance monitoring, and the Pico W can provide a foundation for remote monitoring over Wi-Fi.

> **Portfolio note:** This repository presents the technical prototype and documentation in a project-focused format. It does not reproduce the original university assessment questions or marking material.

## Features

- 3-bit binary access code input
- Authorised/unauthorised user validation
- Servo-controlled cabinet lock
- Green LED for authorised access
- Red LED and buzzer for denied access
- Access-attempt logging
- Successful-access counter
- Maintenance threshold warning
- Pico W Wi-Fi connectivity foundation
- Basic HTTP monitoring page
- Modular MicroPython implementation
- Hardware prototype design and testing documentation

## System Flow

```text
3 Binary Buttons
       |
       v
Raspberry Pi Pico
       |
       v
Authentication
   /       \\
YES        NO
 |          |
 v          v
Unlock     Keep Locked
Servo      Red LED
Green LED  Buzzer
   \        /
    v      v
    Access Logging
         |
         v
Maintenance Monitoring
         |
         v
Wi-Fi Monitoring
```

## Example Access Codes

| Binary Code | User Type | Result |
|---|---|---|
| `100` | System Admin | Granted |
| `010` | Lecturer | Granted |
| `110` | Student/Lab User | Granted |
| `111` | Unknown User | Denied |

These are demonstration codes, not secure production credentials.

## Hardware

- Raspberry Pi Pico / Pico W
- 3 push buttons
- Servo motor
- Green LED
- Red LED
- Buzzer
- LCD display
- Breadboard
- Jumper wires

### Example GPIO allocation

| Component | GPIO |
|---|---:|
| Button 2 / MSB | GP13 |
| Button 1 | GP14 |
| Button 0 / LSB | GP15 |
| Green LED | GP16 |
| Red LED | GP17 |
| Buzzer | GP18 |
| Servo | GP19 |

## Software Structure

```text
src/
├── main.py
├── access_control.py
├── access_logging.py
├── maintenance.py
├── wifi_server.py
├── temperature_classifier.cpp
└── servo_demo.cpp
```

## Authentication

The three button states are combined as `button_2 + button_1 + button_0`. For example, `1 + 1 + 0 = 110`. The resulting code is compared against the authorised-user dictionary.

## Access Control

For an authorised code, the system activates the green LED, moves the servo to the unlocked position for a limited time, returns the servo to the locked position, and records the event.

For an unauthorised code, the cabinet remains locked and the red LED/buzzer provide feedback.

## Maintenance Monitoring

A configurable successful-access threshold demonstrates usage-based preventative maintenance. When the threshold is reached, the system reports `MAINTENANCE REQUIRED`.

## Wi-Fi Monitoring

The Pico W version includes a basic HTTP server foundation for displaying recent access information. A production implementation should use authenticated, encrypted communication and persistent storage.

## Testing

| Test | Expected result |
|---|---|
| Authorised binary code | Access granted |
| Unauthorised binary code | Access denied |
| Authorised access | Green LED |
| Unauthorised access | Red LED + buzzer |
| Authorised access | Servo temporarily unlocks |
| Access attempt | Log entry created |
| Usage threshold reached | Maintenance warning |
| Wi-Fi enabled | Monitoring page can be served |

## Limitations

- Temporary in-memory logs can be lost after power loss.
- Breadboard wiring is vulnerable to accidental disconnection.
- Demonstration authentication uses a small set of predefined codes.
- Wi-Fi functionality requires further hardening before deployment.
- Production communication should use encryption and authentication.
- The current prototype does not provide full user management.
- A real deployment should include secure packaging and power-failure handling.

## Future Improvements

- RFID/NFC authentication
- Persistent storage
- Encrypted network communication
- Secure user-management dashboard
- Brute-force lockout
- Real-time notifications
- Battery backup
- Secure enclosure
- Multiple Pico/Pico W nodes
- Central monitoring server
- Audit reports and analytics
- Role-based permissions

## Skills Demonstrated

Embedded systems, Raspberry Pi Pico/Pico W, MicroPython, C/C++, GPIO programming, servo control, hardware prototyping, access-control logic, data logging, Wi-Fi networking, HTTP basics, debugging, testing and system design.

## Project Status

**Prototype / educational embedded-systems project**

Core binary authentication, physical feedback, servo control, logging and maintenance-monitoring concepts are represented in the repository.
