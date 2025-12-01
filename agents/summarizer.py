# agents/summarizer.py
from tools.summarizer_tool import SummarizerTool

class Summarizer:
    def __init__(self):
        self.tool = SummarizerTool()

    def summarize_research(self, research_results):
        """Combine all snippets from research results and summarize them."""
        collected_text = ""

        for item in research_results:
            if isinstance(item, dict) and "top_results" in item:
                for result in item["top_results"]:
                    snippet = result.get("snippet", "")
                    if snippet:
                        collected_text += snippet + " "

        if not collected_text.strip():
            return "No content to summarize."

        return self.tool.summarize(collected_text)

    def summarize(self, research_results):
        return self.summarize_research(research_results)
