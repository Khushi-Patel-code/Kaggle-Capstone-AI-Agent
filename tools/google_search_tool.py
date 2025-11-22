# tools/google_search_tool.py

import requests

class GoogleSearchTool:
    """
    A simple fallback search tool that returns STRUCTURED results.
    We DO NOT call Google API (Kaggle does not allow).
    Instead, we simulate search by returning stubbed structured results.
    """

    def search(self, query: str):
        """
        Always returns a LIST of dictionaries.
        Each item contains:
         - title
         - snippet
        """

        # --- SIMULATED SAFE STRUCTURED RESULT ---
        return [
            {
                "title": f"Background information about {query}",
                "snippet": f"Overview and background research related to {query}.",
            },
            {
                "title": f"Key insights for {query}",
                "snippet": f"Important strategies, concepts, and techniques for {query}.",
            }
        ]
