import os

def block_ports():
    """
    Blocks all ports from 1 to 1024 using iptables.
    Requires root privileges to execute.
    """
    try:
        print("Blocking ports from 1 to 1024...")
        for port in range(1, 1025):
            # Construct the iptables command to block the port
            command = f"sudo iptables -A INPUT -p tcp --dport {port} -j DROP"
            os.system(command)
        print("All ports from 1 to 1024 have been blocked.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    confirmation = input("This script will block ports 1-1024 on your system. Are you sure? (yes/no): ").strip().lower()
    if confirmation == "yes":
        block_ports()
    else:
        print("Operation canceled.")
