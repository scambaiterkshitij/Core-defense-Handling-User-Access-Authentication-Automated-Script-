import re

def parse_log(logfile):
    failed = {}
    success = {}
    sudo_usage = {}

    with open(logfile, "r", errors="ignore") as f:
        for line in f:
            if "Failed password" in line:
                match = re.search(r"for\s+(\w+)\s+from\s+([\d\.]+)", line)
                if match:
                    user, ip = match.groups()
                    failed.setdefault(user, []).append(ip)

            if "Accepted password" in line:
                match = re.search(r"for\s+(\w+)\s+from\s+([\d\.]+)", line)
                if match:
                    user, ip = match.groups()
                    success.setdefault(user, []).append(ip)

            if "sudo" in line and "COMMAND" in line:
                match = re.search(r"(\w+)\s+sudo", line)
                if match:
                    user = match.group(1)
                    sudo_usage[user] = sudo_usage.get(user, 0) + 1

    return failed, success, sudo_usage
