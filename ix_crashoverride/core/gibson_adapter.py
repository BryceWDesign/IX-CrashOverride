"""
IX-CrashOverride Gibson Adapter

Enables secure communication between IX-CrashOverride and the centralized
IX-Gibson knowledge system.
"""

import requests
import time
from config.gibson_config import GIBSON_API_URL, REQUEST_TIMEOUT_SECONDS, RETRY_ATTEMPTS, RETRY_BACKOFF_SECONDS

class GibsonAdapter:
    def __init__(self):
        self.api_url = GIBSON_API_URL
        self.timeout = REQUEST_TIMEOUT_SECONDS
        self.retries = RETRY_ATTEMPTS
        self.backoff = RETRY_BACKOFF_SECONDS

    def query_gibson(self, question: str) -> dict:
        """
        Submit a question to IX-Gibson and return structured response.

        Args:
            question (str): Query string to submit.

        Returns:
            dict: Parsed response or error details.
        """
        payload = {
            "domain": "crashoverride",
            "question": question,
            "from": "ix-crashoverride"
        }
        for attempt in range(1, self.retries + 1):
            try:
                response = requests.post(self.api_url, json=payload, timeout=self.timeout)
                if response.status_code == 200:
                    return response.json()
                else:
                    print(f"[Gibson HTTP {response.status_code}] {response.text}")
            except requests.RequestException as e:
                print(f"[CrashOverride] Gibson request error (attempt {attempt}): {e}")

            if attempt < self.retries:
                time.sleep(self.backoff)

        return {"error": "Failed to connect to IX-Gibson after retries."}
