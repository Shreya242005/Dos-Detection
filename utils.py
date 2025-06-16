import re
from datetime import datetime

# Validate IP address format
def is_valid_ip(ip):
    pattern = re.compile(r"^\d{1,3}(\.\d{1,3}){3}$")
    return pattern.match(ip) is not None

# Format current timestamp
def get_current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Write a basic DoS detection report
def write_report(file_path, target_ip, syn_count, total_packets):
    with open(file_path, "w") as f:
        f.write("===============================\n")
        f.write("🚨 DoS Detection Report\n")
        f.write("===============================\n\n")
        f.write(f"🕒 Scan Timestamp: {get_current_timestamp()}\n")
        f.write(f"🖥️ Target IP: {target_ip}\n\n")
        f.write("---------------------------------------\n")
        f.write("🔍 Scanning Activity:\n")
        f.write(f"- Total packets analyzed: {total_packets}\n")
        f.write(f"- SYN packets detected: {syn_count}\n")
        f.write("\n")

        if syn_count > 500:
            f.write("⚠️ Suspicious Behavior Identified:\n")
            f.write("- High volume of SYN packets detected\n")
            f.write("- Behavior consistent with SYN flood (DoS attack)\n\n")
            f.write("🛡️ Detection Summary: Potential DoS Attack\n")
        else:
            f.write("✅ No suspicious activity detected.\n")

        f.write("\n📁 Log saved by: DoS Detection System v1.0\n")
