"""
IX-CrashOverride Core Module

Contains the primary logic to handle reasoning and decision-making,
delegating knowledge lookups to IX-Gibson via the GibsonAdapter.
"""

from .gibson_adapter import GibsonAdapter

class CrashOverrideCore:
    def __init__(self):
        self.gibson = GibsonAdapter()

    def process_input(self, question: str) -> str:
        """
        Sends input to Gibson and formats response.

        Args:
            question (str): Natural language query.

        Returns:
            str: Answer string or fallback message.
        """
        result = self.gibson.query_gibson(question)
        if "error" in result:
            return f"[CrashOverride Error] {result['error']}"
        return result.get("answer", "[CrashOverride] No answer found.")
