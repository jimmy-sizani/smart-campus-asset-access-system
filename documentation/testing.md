# Testing & Validation

| Test | Expected result | Result |
|---|---|---|
| `100` authorised code | Access granted | Pass |
| `010` authorised code | Access granted | Pass |
| `110` authorised code | Access granted | Pass |
| `111` unauthorised code | Access denied | Pass |
| Authorised access | Green LED activates | Tested |
| Unauthorised access | Red LED + buzzer activate | Tested |
| Authorised access | Servo unlocks temporarily | Tested |
| Access attempt | Event is logged | Tested |
| Usage threshold reached | Maintenance warning | Pass |
| Wi-Fi monitoring | Remote page available | Further development required |

## Observed Issues

- Rapid repeated button presses can require debounce handling.
- In-memory logs are lost after a power interruption.
- Breadboard connections can become loose.
- Wi-Fi monitoring was not fully reliable during prototype testing.

## Improvements

1. Add software/hardware button debouncing.
2. Store logs persistently.
3. Add authenticated and encrypted network communication.
4. Use a secure enclosure.
5. Add backup power.
6. Implement lockout after repeated failed attempts.
