import logging
from typing import List, Dict, Any

logger = logging.getLogger("coach")
logger.setLevel(logging.DEBUG)


class Coach:
    """Transform the orchestrator output into final guidance for the user."""

    def __init__(self, llm=None):
        self.llm = llm  # Optional, for LLM-generated coaching

    # -------------------------------------------------------------------------
    # REQUIRED METHOD → Orchestrator will call this
    # -------------------------------------------------------------------------
    def create_output(self, mission: str, plan: List[Dict[str, Any]], summary: str) -> Dict[str, Any]:
        logger.debug("Coach: creating final output for mission='%s'", mission)

        # Generate human-readable plan list
        explained_steps = []
        for i, step in enumerate(plan):
            readable = step.get("query") or step.get("type") or str(step)
            explained_steps.append(f"Step {i+1}: {readable}")

        # OPTIONAL: If using LLM coaching
        if self.llm:
            prompt = f"""
            Create a study-friendly output.

            User goal:
            {mission}

            Study Plan:
            {plan}

            Summary of research:
            {summary}

            Produce:
            - Study guidance
            - A helpful timetable suggestion
            - Motivation line
            - Important notes
            """
            coaching_message = self.llm(prompt)
        else:
            coaching_message = (
                f"For the mission '{mission}', follow the steps above. "
                "Focus on the important concepts from the summary. "
                "Stay consistent and track your daily progress!"
            )

        # FINAL STRUCTURED OUTPUT (sent back to main.py)
        return {
            "mission": mission,
            "summary": summary,
            "steps_explained": explained_steps,
            "coaching": coaching_message,
        }
