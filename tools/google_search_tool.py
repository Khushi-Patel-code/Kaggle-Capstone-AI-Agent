# tools/google_search_tool.py

import requests

class GoogleSearchTool:
    """Simulates a search engine tool, returning structured, stubbed results for 
    local testing and competition constraints (e.g., no live API calls)."""

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
