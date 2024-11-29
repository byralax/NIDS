from scapy.all import sniff
from rule_engine import RuleEngine
from log_handler import LogHandler

def process_packet(packet):
    """Processes each captured packet."""
    rule_engine = RuleEngine("config/rules.json")
    log_handler = LogHandler("logs/alerts.log")

    alert = rule_engine.check_packet(packet)
    if alert:
        log_handler.log_alert(alert)

if __name__ == "__main__":
    print("Starting packet sniffer...")
    sniff(prn=process_packet, store=False)
