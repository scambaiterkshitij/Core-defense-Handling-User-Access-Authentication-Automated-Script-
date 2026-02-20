# Core Defense - Authentication Audit Toolkit

A lightweight, cross-distribution Linux authentication log auditing tool built for security monitoring and defensive analysis.

This toolkit scans system authentication logs, detects failed login attempts, successful logins, and sudo usage, and generates structured security reports.

Designed for:
- Kali Linux
- Ubuntu / Debian
- Fedora / CentOS / RHEL
- Any Linux distro using standard auth logs

---

## Features

- Automatic detection of authentication log file
- Failed login attempt detection
- Successful login tracking
- Sudo usage monitoring
- Structured report generation
- No external dependencies
- Lightweight and fast
- Modular architecture
- Cross-distribution compatibility

---

## Project Structure

```
Core-defense-Handling-User-Access-Authentication-Automated-Script/
│
├── main.py
├── log_parser.py
├── report.py
├── utils.py
├── config.py
├── banner.py
├── requirements.txt
├── logs/
│   └── (Generated reports)
└── README.md
```

---

## Requirements

- Python 3.x
- Linux system (Kali / Ubuntu / Debian / Fedora / etc.)
- Root privileges (required to read authentication logs)

No external Python libraries required.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/scambaiterkshitij/Core-defense-Handling-User-Access-Authentication-Automated-Script.git
cd Core-defense-Handling-User-Access-Authentication-Automated-Script
```

Make the script executable:

```bash
chmod +x main.py
```

---

## Usage

Run with root privileges:

```bash
sudo python3 main.py
```

OR

```bash
sudo ./main.py
```

---

## Output

The script automatically:

- Detects correct authentication log file
- Parses login activity
- Generates a timestamped report
- Saves report inside:

```
logs/
```

Example report filename:

```
report_20260220_153000.txt
```

---

## How It Works

The toolkit checks:

- `/var/log/auth.log` (Debian-based systems)
- `/var/log/secure` (RHEL-based systems)

It extracts:

- Failed password attempts
- Successful authentications
- Sudo command usage

Then generates a structured security audit report.

---

## Use Case

- Security auditing
- Blue team analysis
- Linux server monitoring
- Suspicious login investigation
- Learning system log analysis

---

## ⚠ Disclaimer

This project is intended strictly for defensive security analysis and educational purposes only.  
Do not use it for unauthorized monitoring of systems.

---

## Version

Current Version: 1.0.7

---

## Author

scambaiterKshitij

---

## Contribute

Pull requests are welcome.  
Feel free to fork and enhance the toolkit with additional defensive security features.

---

## License

This project is open-source and free to use under the MIT License.
