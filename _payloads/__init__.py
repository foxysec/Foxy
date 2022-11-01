
from _payloads._discord.webhook_spammer import start_webhook_spammer

from _payloads._net.port_scanner import start_port_scanner

class discord:
    def webhook_spammer():
        start_webhook_spammer()

class network:
    def port_scanner():
        start_port_scanner()