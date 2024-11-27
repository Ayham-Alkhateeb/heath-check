#!/usr/bin/env python3
import  os
import sys

def check_reboot():
    """Return True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def main():
    if check_reboot():
        print("Pending reboot")
        sys.exit(1)
    print("everything is ok.")
    sys.exit(0)

main()
