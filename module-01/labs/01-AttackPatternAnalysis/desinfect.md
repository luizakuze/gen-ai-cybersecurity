# System Disinfection Guide for Malicious Code Infection

This guide outlines methods to disinfect a system in the event of an infection caused by malicious code, such as a monitoring script or daemon process. Follow these steps systematically to ensure a thorough cleanup and prevention of further harm.

---

## 1. Identify and Stop the Malicious Process

### Kill the Daemon Process:
1. Identify the process ID (PID) of the malicious script:
   ```bash
   ps aux | grep url_recorder
   ```
2. Terminate the process:
   ```bash
   kill -9 <PID>
   ```

3. If the process restarts automatically, investigate startup scripts (e.g., `cron`, `systemd`, or autostart files).

---

## 2. Remove Malicious Files

### Delete the Script and Associated Files:
1. Locate and delete the script file (e.g., `url_recorder.py`):
   ```bash
   rm /path/to/url_recorder.py
   ```
2. Remove related log files and artifacts:
   ```bash
   rm url_recorder.log history.txt url_recorder_error.log
   ```

### Check for Persistent Files:
1. Search and remove `.pid` or other hidden files:
   ```bash
   find / -name "*.pid" -exec grep "url_recorder" {} \; -delete
   ```

---

## 3. Disable Startup Persistence

### Systemd Services:
1. Check for the malicious `systemd` service:
   ```bash
   systemctl list-units --type=service | grep url_recorder
   ```
2. Disable and delete the service:
   ```bash
   systemctl disable url_recorder
   rm /etc/systemd/system/url_recorder.service
   ```

### Cron Jobs:
1. Inspect cron jobs for suspicious entries:
   ```bash
   crontab -l
   ```
2. Remove any identified malicious entries:
   ```bash
   crontab -e
   ```

### Autostart Directories:
1. Investigate startup directories:
   - **Linux**: `~/.config/autostart/`, `/etc/init.d/`
   - **Windows**: `shell:startup`, registry keys in `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`

---

## 4. Verify System Integrity

### Scan for Remaining Malicious Code:
Use antivirus or anti-malware tools to perform a system-wide scan:
- **Linux**:
  ```bash
  clamscan -r /
  ```
- **Windows**: Use Windows Defender or third-party tools like Malwarebytes.

### Verify System Files:
- For **Linux**:
  ```bash
  debsums -c  # Verify checksums of installed packages (Debian/Ubuntu)
  rpm -Va     # Verify installed packages (RHEL/CentOS)
  ```
- For **Windows**:
  Run:
  ```cmd
  sfc /scannow
  ```

---

## 5. Audit Clipboard and User Accounts

### Clear the Clipboard:
- **Linux**:
  ```bash
  echo -n "" | xclip -selection clipboard
  ```
- **Windows**:
  ```cmd
  echo off | clip
  ```

### Review User Accounts:
1. Inspect active accounts and permissions:
   ```bash
   cat /etc/passwd
   ```
2. Disable or remove unauthorized accounts.

---

## 6. Monitor Network Traffic

### Check for Suspicious Activity:
Use tools to detect outgoing connections or data exfiltration:
- **Linux**: `tcpdump`, `Wireshark`
- **Windows**: Resource Monitor or third-party tools.

Example:
```bash
tcpdump -i any | grep suspicious_domain
```

---

## 7. Educate Users

### Prevent Future Infections:
1. Avoid running unverified scripts.
2. Ensure downloaded files originate from trusted sources.
3. Use sandbox environments for testing unknown scripts.

---

## 8. Reinstall or Reset the System (If Necessary)

If the infection persists:
1. Backup important data.
2. Reinstall the operating system or reset it to factory defaults.

---

## 9. Update the System and Software

### Apply Security Updates:
Keep your system updated to mitigate vulnerabilities:
- **Linux**:
  ```bash
  sudo apt update && sudo apt upgrade -y
  ```
- **Windows**: Install all pending updates via Windows Update.

---

## 10. Harden System Security

### Enable Security Features:
1. **Linux**:
   - Enable SELinux/AppArmor.
   - Configure a firewall:
     ```bash
     sudo ufw enable
     ```

2. **Windows**:
   - Ensure Windows Defender is active.
   - Enable the built-in firewall.

### Set File Permissions:
Restrict access to sensitive files and directories.

---

By following these steps, the system can be effectively disinfected from malicious code and fortified against future infections.
