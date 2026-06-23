import re

def detect_security_risk(text):

    risky_patterns = [
        "password",
        "api key",
        "secret",
        "token",
        "credential",
        "ssh key",
        "private key",
        "gmail password"
    ]

    text = text.lower()

    for pattern in risky_patterns:
        if pattern in text:
            return "High Risk"

    return "Safe"