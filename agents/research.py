# agents/research.py
from tools.google_search_tool import GoogleSearchTool

class Researcher:
    """Runs research queries using the GoogleSearchTool."""

    def __init__(self):
        self.search_tool = GoogleSearchTool()

    def research(self, query: str):
        """Return structured search result for ONE query."""
        results = self.search_tool.search(query)
        return {"query": query, "top_results": results}

    def research_topics(self, plan_steps: list):
        """Only research steps are processed."""
        structured_results = []

        for step in plan_steps:
            if isinstance(step, dict) and step.get("type") == "research":
                res = self.research(step["query"])
                structured_results.append(res)

        return structured_results
