# Example scenario

## Assume an organization having Web Server IP address 92.168.1.102 has observed some suspicious activity. The log of the event is as follows:

```
Date/Time: 2023-12-20 18:45:22
Web Server: 192.168.1.102
Source IP: 203.0.113.42
Protocol: HTTP
Event Type: Suspicious Login Attempt
Username: admin
Status: Failed
Description: Multiple failed login attempts from external IP 203.0.113.42 to web server 192.168.1.102. The username 'admin' was targeted—possible brute-force attack. Immediate investigation and security measures are recommended.
```

## The organization's admin has also observed suspicious network traffic generated from the ten different users working in the organization. The log of the users are as follows:

```
1. Date/Time: 2023-12-20 09:15:30
   User: john_doe
   Source IP: 192.168.1.101
   Destination IP: 203.0.113.42
   Protocol: TCP
   Port: 443
   Traffic Volume: 500 MB
   Description: High outbound traffic observed from user john_doe\'s system (192.168.1.101) to IP address 203.0.113.42 on port 443.

2. Date/Time: 2023-12-20 09:20:45
   User: alice_smith
   Source IP: 192.168.1.102
   Destination IP: 203.0.113.42
   Protocol: UDP
   Port: 8080
   Traffic Volume: 700 MB
   Description: Unusually high UDP traffic from user alice_smith\'s system (192.168.1.102) to IP address 203.0.113.42 on port 8080.

3. Date/Time: 2023-12-20 09:25:10
   User: robert_jones
   Source IP: 192.168.1.103
   Destination IP: 203.0.113.42
   Protocol: TCP
   Port: 22
   Traffic Volume: 1.2 GB
   Description: Elevated outbound TCP traffic from user robert_jones\'s system (192.168.1.103) to IP address 203.0.113.42 on port 22.

4. Date/Time: 2023-12-20 09:30:22
   User: emily_wang
   Source IP: 192.168.1.104
   Destination IP: 203.0.113.42
   Protocol: ICMP
   Traffic Volume: 800 MB
   Description: Unusual ICMP traffic observed from user emily_wang\'s system (192.168.1.104) to IP address 203.0.113.42.

5. Date/Time: 2023-12-20 09:35:40
   User: michael_davis
   Source IP: 192.168.1.105
   Destination IP: 203.0.113.42
   Protocol: UDP
   Port: 53
   Traffic Volume: 600 MB
   Description: High outbound UDP traffic from user michael_davis\'s system (192.168.1.105) to IP address 203.0.113.42 on port 53.

6. Date/Time: 2023-12-20 09:40:55
   User: sarah_miller
   Source IP: 192.168.1.106
   Destination IP: 203.0.113.42
   Protocol: TCP
   Port: 80
   Traffic Volume: 900 MB
   Description: Elevated outbound TCP traffic from user sarah_miller\'s system (192.168.1.106) to IP address 203.0.113.42 on port 80.

7. Date/Time: 2023-12-20 09:45:12
   User: kevin_wilson
   Source IP: 192.168.1.107
   Destination IP: 203.0.113.42
   Protocol: UDP
   Port: 123
   Traffic Volume: 1.5 GB
   Description: Abnormally high UDP traffic from user kevin_wilson\'s system (192.168.1.107) to IP address 203.0.113.42 on port 123.

8. Date/Time: 2023-12-20 09:50:30
   User: lisa_jackson
   Source IP: 192.168.1.108
   Destination IP: 203.0.113.42
   Protocol: TCP
   Port: 8080
   Traffic Volume: 1.8 GB
   Description: Significantly elevated outbound TCP traffic from user lisa_jackson\'s system (192.168.1.108) to IP address 203.0.113.42 on port 8080.

9. Date/Time: 2023-12-20 09:55:45
   User: mark_taylor
   Source IP: 192.168.1.109
   Destination IP: 203.0.113.42
   Protocol: UDP
   Port: 514
   Traffic Volume: 1.2 GB
   Description: Unusually high UDP traffic from user mark_taylor\'s system (192.168.1.109) to IP address 203.0.113.42 on port 514.

10. Date/Time: 2023-12-20 10:00:00
   User: jessica_martin
   Source IP: 192.168.1.110
   Destination IP: 203.0.113.42
   Protocol: TCP
   Port: 443
   Traffic Volume: 2.5 GB
   Description: Extremely high outbound TCP traffic from user jessica_martin\'s system (192.168.1.110) to IP address 203.0.113.42 on port 443.
```

# Questions

## Identify the usernames associated with high outbound traffic from the provided log.

```
1. **john_doe** – 500 MB (TCP, Port 443)  
2. **alice_smith** – 700 MB (UDP, Port 8080)  
3. **robert_jones** – 1.2 GB (TCP, Port 22)  
4. **emily_wang** – 800 MB (ICMP)  
5. **michael_davis** – 600 MB (UDP, Port 53)  
6. **sarah_miller** – 900 MB (TCP, Port 80)  
7. **kevin_wilson** – 1.5 GB (UDP, Port 123)  
8. **lisa_jackson** – 1.8 GB (TCP, Port 8080)  
9. **mark_taylor** – 1.2 GB (UDP, Port 514)  
10. **jessica_martin** – 2.5 GB (TCP, PPortorta 443)  
```

## Identify any failed login attempts within the provided log data, detailing the user, source IP address, and timestamp associated with each attempt.

```
- **User:** `admin`  
- **Source IP:** `203.0.113.42`  
- **Timestamp:** `2023-12-20 18:45:22`  
- **Description:** Multiple failed login attempts from external IP 203.0.113.42 to the web server 192.168.1.102, suggesting a possible brute-force attack. 
`` 