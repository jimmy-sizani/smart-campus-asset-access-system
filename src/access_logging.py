"""Simple in-memory access logging."""
import time

access_log_history = []
total_attempts = 0
successful_accesses = 0


def get_time():
    t = time.localtime()
    return f"{t[3]:02d}:{t[4]:02d}:{t[5]:02d}"


def log_attempt(binary_code, user_type, granted):
    global total_attempts, successful_accesses
    total_attempts += 1
    if granted:
        successful_accesses += 1
    entry = {
        "log_number": total_attempts,
        "binary_code": binary_code,
        "user_type": user_type,
        "result": "Granted" if granted else "Denied",
        "successful_accesses": successful_accesses,
        "time": get_time(),
    }
    access_log_history.append(entry)
    return entry


def recent_logs(limit=10):
    return access_log_history[-limit:]
