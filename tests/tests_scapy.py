# from scapy.all import IP, TCP, sr1
#
# target_ip = "127.0.0.1"
# packet = IP(dst=target_ip) / TCP(dport=80, flags="S")
# response = sr1(packet, timeout=1)
#
# if response:
#     print(response.summary())
# else:
#     print("No response")

import os

max_threads = os.cpu_count()
print(max_threads)
