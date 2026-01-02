# 1. Storing information (Variables)
system_user = "admin"
password_attempts = 3

# 2. Creating a list of suspicious IP addresses (Lists)
blocked_ips = ["192.168.0.1", "10.0.0.50", "172.16.0.5"]

# 3. Checking a condition (if/else)
current_ip = "10.0.0.50"

print(f"Checking IP address: {current_ip}...")

if current_ip in blocked_ips:
    print("ALERT: Access denied! This IP address is blacklisted.")
else:
    print("Access granted. Welcome to the system.")
