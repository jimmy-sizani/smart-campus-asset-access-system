"""Main application for the Smart Campus Asset Access System."""
import time
import access_logging
from access_control import initialise_lock, read_binary_code, authenticate
from access_logging import log_attempt
from maintenance import maintenance_message


def main():
    initialise_lock()
    print("Smart Campus Asset Access System")
    print("System ready. Enter a binary access code.")
    last_code = "000"

    while True:
        code = read_binary_code()
        if code != "000" and code != last_code:
            granted, user_type = authenticate(code)
            entry = log_attempt(code, user_type, granted)
            print(f"#{entry['log_number']} | {entry['binary_code']} | {entry['user_type']} | {entry['result']}")
            print(maintenance_message(access_logging.successful_accesses))
        last_code = code
        time.sleep(0.1)


if __name__ == "__main__":
    main()
