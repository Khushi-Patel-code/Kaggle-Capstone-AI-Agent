"""
agents/research.py
Handles searching using GoogleSearchTool.
Returns structured results, not raw strings.
"""

from tools.google_search_tool import GoogleSearchTool


class Researcher:
    """Runs research queries using the google search tool."""

    def __init__(self):
        self.search_tool = GoogleSearchTool()

    def research(self, query: str):
        """Return structured search result for ONE query."""
        results = self.search_tool.search(query)

        return {
            "query": query,
            "top_results": results,
        }

    def research_topics(self, plan_steps: list):
        """
        Takes a plan (list of steps), runs research only for 'research' steps,
        and returns a LIST of structured dicts.
        """

        structured_results = []

        for step in plan_steps:
            if step["type"] == "research":
                res = self.research(step["query"])
                structured_results.append(res)

        return structured_results
