"""Access-control logic for the Smart Campus Asset Access System."""
from machine import Pin, PWM
import time

BTN_2 = Pin(13, Pin.IN, Pin.PULL_DOWN)
BTN_1 = Pin(14, Pin.IN, Pin.PULL_DOWN)
BTN_0 = Pin(15, Pin.IN, Pin.PULL_DOWN)
GREEN_LED = Pin(16, Pin.OUT)
RED_LED = Pin(17, Pin.OUT)
BUZZER = Pin(18, Pin.OUT)
SERVO = PWM(Pin(19))
SERVO.freq(50)

LOCKED_ANGLE = 0
UNLOCKED_ANGLE = 90
UNLOCK_TIME_SECONDS = 3

AUTHORIZED_USERS = {
    "110": "Student/Lab User",
    "010": "Lecturer",
    "100": "System Admin",
}


def set_servo_angle(angle):
    duty = int(1000 + (angle / 180) * 8000)
    SERVO.duty_u16(duty)


def read_binary_code():
    return str(BTN_2.value()) + str(BTN_1.value()) + str(BTN_0.value())


def authenticate(code):
    """Validate a code and return (granted, user_type)."""
    if code in AUTHORIZED_USERS:
        user_type = AUTHORIZED_USERS[code]
        GREEN_LED.value(1)
        set_servo_angle(UNLOCKED_ANGLE)
        time.sleep(UNLOCK_TIME_SECONDS)
        set_servo_angle(LOCKED_ANGLE)
        GREEN_LED.value(0)
        return True, user_type

    RED_LED.value(1)
    BUZZER.value(1)
    time.sleep(1.5)
    RED_LED.value(0)
    BUZZER.value(0)
    return False, "Unknown"


def initialise_lock():
    GREEN_LED.value(0)
    RED_LED.value(0)
    BUZZER.value(0)
    set_servo_angle(LOCKED_ANGLE)
