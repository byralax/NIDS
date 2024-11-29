import unittest
from rule_engine import RuleEngine
from scapy.layers.inet import IP, TCP

class TestRuleEngine(unittest.TestCase):
    def setUp(self):
        self.rule_engine = RuleEngine("config/rules.json")

    def test_check_packet(self):
        packet = IP(dst="192.168.1.10") / TCP()
        alert = self.rule_engine.check_packet(packet)
        self.assertIn("Alert: Rule 1 triggered", alert)

if __name__ == "__main__":
    unittest.main()
