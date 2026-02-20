#!/usr/bin/env python3

from banner import show_banner
from utils import find_auth_log
from log_parser import parse_log
from report import generate_report

def main():
    show_banner()

    logfile = find_auth_log()

    if not logfile:
        print("No authentication log found on this system.")
        return

    print(f"[+] Using log file: {logfile}")
    print("[+] Parsing logs...")

    failed, success, sudo_usage = parse_log(logfile)

    report_file = generate_report(failed, success, sudo_usage)

    print("[+] Audit completed.")
    print(f"[+] Report saved to: {report_file}")

if __name__ == "__main__":
    main()
