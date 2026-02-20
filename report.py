from datetime import datetime
import os

def generate_report(failed, success, sudo_usage):
    os.makedirs("logs", exist_ok=True)
    filename = f"logs/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w") as f:
        f.write("Authentication Audit Report\n")
        f.write(f"Generated: {datetime.now()}\n\n")

        f.write("Failed Login Attempts:\n")
        if failed:
            for user, ips in failed.items():
                f.write(f"{user} - {len(ips)} attempts from {set(ips)}\n")
        else:
            f.write("None\n")

        f.write("\nSuccessful Logins:\n")
        if success:
            for user, ips in success.items():
                f.write(f"{user} - {len(ips)} logins from {set(ips)}\n")
        else:
            f.write("None\n")

        f.write("\nSudo Usage:\n")
        if sudo_usage:
            for user, count in sudo_usage.items():
                f.write(f"{user} used sudo {count} time(s)\n")
        else:
            f.write("None\n")

    return filename
