import json
from scapy.all import IP, TCP, UDP

class RuleEngine:
    def __init__(self, rules_file):
        with open(rules_file, 'r') as file:
            self.rules = json.load(file)

    def check_packet(self, packet):
        """Checks the packet against predefined rules."""
        for rule in self.rules:
            if rule['protocol'] == 'TCP' and packet.haslayer(TCP):
                if packet[IP].dst == rule['destination']:
                    return f"Alert: Rule {rule['id']} triggered for {packet[IP].dst}"
            if rule['protocol'] == 'UDP' and packet.haslayer(UDP):
                if packet[IP].dst == rule['destination']:
                    return f"Alert: Rule {rule['id']} triggered for {packet[IP].dst}"
        return None
