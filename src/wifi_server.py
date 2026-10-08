"""Basic Pico W HTTP monitoring server.
Do not commit real Wi-Fi credentials to a public repository.
"""
import network
import socket
import time

WIFI_SSID = "YOUR_WIFI_SSID"
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"


def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    timeout = 10
    while not wlan.isconnected() and timeout > 0:
        time.sleep(1)
        timeout -= 1
    if wlan.isconnected():
        print("Wi-Fi connected:", wlan.ifconfig()[0])
        return wlan
    print("Wi-Fi connection failed.")
    return None


def build_webpage(logs, maintenance_status):
    rows = ""
    for entry in logs:
        rows += (
            "<tr>"
            f"<td>{entry['log_number']}</td>"
            f"<td>{entry['binary_code']}</td>"
            f"<td>{entry['user_type']}</td>"
            f"<td>{entry['result']}</td>"
            f"<td>{entry['successful_accesses']}</td>"
            f"<td>{entry['time']}</td>"
            "</tr>"
        )
    return (
        "<!DOCTYPE html><html><head><meta charset='UTF-8'>"
        "<title>Campus Asset Access Log</title></head><body>"
        "<h1>Campus Asset Access Log</h1>"
        f"<p>Maintenance: {maintenance_status}</p>"
        "<table border='1' cellpadding='6'>"
        "<tr><th>Log</th><th>Code</th><th>User</th><th>Result</th>"
        "<th>Successful Accesses</th><th>Time</th></tr>"
        f"{rows}</table></body></html>"
    )


def start_server():
    address = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(address)
    server.listen(1)
    server.settimeout(0.1)
    return server
