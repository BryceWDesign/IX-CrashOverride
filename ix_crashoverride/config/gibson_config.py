"""
Gibson Configuration — IX-CrashOverride

Defines parameters for connecting to the IX-Gibson API from this specialist node.
"""

# IX-Gibson endpoint (local or remote depending on deployment)
GIBSON_API_URL = "http://localhost:9000/api/query"

# Request timeout duration (in seconds)
REQUEST_TIMEOUT_SECONDS = 5

# Retry logic for unstable connections
RETRY_ATTEMPTS = 3
RETRY_BACKOFF_SECONDS = 2
