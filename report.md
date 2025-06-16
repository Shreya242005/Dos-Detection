
===============================
🚨 DoS Detection Report
===============================

🕒 Scan Timestamp: 2025-06-16 18:23:01
🖥️ Target IP: 192.168.1.10

---------------------------------------
🔍 Scanning Activity:
- Total packets analyzed: 1420
- SYN packets detected: 982
- ACK packets detected: 321
- Unique source IPs: 1
- High request rate detected from IP: 192.168.1.50

⚠️ Suspicious Behavior Identified:
- 850+ SYN packets in under 15 seconds
- Repeated identical request patterns from the same IP
- Normal TCP handshake incomplete in many cases

🛡️ Detection Summary:
✔️ This behavior is consistent with a SYN flood (DoS attack).
✔️ Immediate inspection and firewall rules are recommended.

📁 Log saved by: DoS Detection System v1.0
