/* Servo control reference for the cabinet lock.
   The final Pico implementation can use the selected SDK/PWM interface. */
const int LOCKED_ANGLE = 0;
const int UNLOCKED_ANGLE = 90;
const int UNLOCK_DELAY_MS = 3000;

// Sequence:
// moveServo(UNLOCKED_ANGLE);
// delay(UNLOCK_DELAY_MS);
// moveServo(LOCKED_ANGLE);
