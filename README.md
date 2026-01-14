# security-log-analysis-2

This project was created as part of the Google Cybersecurity Certificate.

## Objective
Analyze authentication logs to identify failed login attempts and suspicious IP addresses.

## Tools
- Python
- Sample authentication logs

## What the script does
- Reads an authentication log file
- Detects failed login attempts
- Identifies possible brute-force behavior

## Example Use Case
A SOC analyst can use this script to quickly identify suspicious IPs in system logs.

## Skills Demonstrated
- Log analysis
- Basic Python scripting
- Security monitoring concepts
  
md 
I chose to flag an IP as suspicious if it has 3 or more failed login attempts,
including both "Failed password" and "Invalid user" events, because repeated failures may indicate brute-force attacks.
