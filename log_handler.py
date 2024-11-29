import logging

class LogHandler:
    def __init__(self, log_file):
        logging.basicConfig(filename=log_file, level=logging.INFO,
                            format='%(asctime)s - %(message)s')

    def log_alert(self, message):
        """Logs an alert message."""
        logging.info(message)
        print(message)  # Print to console for real-time monitoring
