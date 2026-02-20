#!/usr/bin/env python3

import os
import re
from datetime import datetime

LOG_PATHS = [
    "/var/log/auth.log",         # Debian/Ubuntu/Kali
    "/var/log/secure"            # RedHat/CentOS
]

def find_log_file():
    for path in LOG_PATHS:
        if os.path.exists(path):
            return path
    return None

def parse_auth_log(logfile):
    failed = {}
    success = {}
    sudo = {}

    with open(logfile, "r", errors="ignore") as f:
        for line in f:
            if "Failed password" in line:
                m = re.search(r"for\s+(\w+)\s+from\s+([\d\.]+)", line)
                if m:
                    user, ip = m.groups()
                    failed.setdefault(user, []).append(ip)

            if "Accepted password" in line:
                m = re.search(r"for\s+(\w+)\s+from\s+([\d\.]+)", line)
                if m:
                    user, ip = m.groups()
                    success.setdefault(user, []).append(ip)

            if "sudo" in line and "COMMAND" in line:
                m = re.search(r"(\w+)\s+sudo", line)
                if m:
                    user = m.group(1)
                    sudo.setdefault(user, 0)
                    sudo[user] += 1

    return failed, success, sudo


def print_report(failed, success, sudo):
    print("\n--- Authentication Audit Report ---\n")
    print(f"Report generated: {datetime.now()}\n")

    print("** Failed Login Attempts **")
    if failed:
        for user, ips in failed.items():
            print(f"{user} - {len(ips)} fails from {set(ips)}")
    else:
        print("None found.")

    print("\n** Successful Logins **")
    if success:
        for user, ips in success.items():
            print(f"{user} - {len(ips)} successes from {set(ips)}")
    else:
        print("None found.")

    print("\n** sudo Usage **")
    if sudo:
        for user, count in sudo.items():
            print(f"{user} used sudo {count} time(s)")
    else:
        print("None found.")

    print("\n--- End of Report ---\n")


def main():
    logfile = find_log_file()
    if not logfile:
        print("No authentication log found on this system.")
        return

    failed, success, sudo = parse_auth_log(logfile)
    print_report(failed, success, sudo)


if __name__ == "__main__":
    main()
