"""
agents/summarizer.py
Summarizes research results.
"""

from tools.summarizer_tool import SummarizerTool


class Summarizer:
    def __init__(self):
        self.summarizer = SummarizerTool()

    def summarize(self, research_results: list) -> str:
        """Summarizes all research results into one combined text."""
        combined = ""

        for p in research_results:
            if "top_results" in p and len(p["top_results"]) > 0:
                combined += f"Research for query: {p['query']}\n"
                for r in p["top_results"]:
                    combined += f"- {r}\n"
                combined += "\n"

        if not combined.strip():
            combined = "No meaningful research found."

        return self.summarizer.summarize(combined)

    def summarize_research(self, research_results: list) -> str:
        return self.summarize(research_results)
