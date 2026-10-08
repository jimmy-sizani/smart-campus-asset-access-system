"""Usage-based maintenance monitoring."""
MAINTENANCE_THRESHOLD = 5


def maintenance_due(successful_access_count):
    return successful_access_count >= MAINTENANCE_THRESHOLD


def maintenance_message(successful_access_count):
    if maintenance_due(successful_access_count):
        return "MAINTENANCE REQUIRED"
    return f"Equipment status normal ({successful_access_count}/{MAINTENANCE_THRESHOLD} uses)"
