# Infect - Questions
## 1. Analyze the code and identify the malicious behavior.
- Monitoring User Activity
- Accessing and Copying URLs
- Persistence via Daemon
- Silent Operations: Script doens't notify the user of its actions
- Insecure Clipboard Handling
## 2. List the potential assets susceptible to infection.
- User Privacy
- Clipboard Data
- System Resources
- Logs
- File system
## 3. Determine the method for verifying the success of the attack and the compromise of the system.
- Checking the history.txt File
- Monitoring Log Files
- Behavioral Signs
- Persistence Validation: Since the script runs as a daemon, the attacker can confirm the script's persistence by verifying if the process (url_recorder) remains active in the background after system reboots