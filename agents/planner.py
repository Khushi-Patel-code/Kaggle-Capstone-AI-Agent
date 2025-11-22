"""
agents/planner.py
Creates a multi-step plan for the mission.

The Planner outputs a list of steps.
Each step is a dict with required keys:
  - step_id (str)
  - type ("research" or "summarize")
  - query (for research)
  - child_steps (for summarize)
"""

import logging
import uuid
from typing import List, Dict, Any

logger = logging.getLogger("planner")
logger.setLevel(logging.DEBUG)


class Planner:
    """Generate a structured plan for the orchestrator."""

    def __init__(self):
        pass

    def _new_step_id(self) -> str:
        return "s_" + uuid.uuid4().hex[:6]

    def plan(self, mission: str, previous_plan=None) -> List[Dict[str, Any]]:
        """
        Create a multi-step plan.
        Includes memory context if previous_plan is provided.
        """

        logger.debug("Planner: creating plan for mission: %s", mission)

        context_note = ""
        if previous_plan:
            context_note = " (using past session knowledge)"

        s1 = {
            "step_id": self._new_step_id(),
            "type": "research",
            "query": f"General overview and background for: {mission}{context_note}",
        }
        s2 = {
            "step_id": self._new_step_id(),
            "type": "research",
            "query": f"Important methods, techniques, challenges related to: {mission}{context_note}",
        }
        s3 = {
            "step_id": self._new_step_id(),
            "type": "summarize",
            "child_steps": [s1["step_id"], s2["step_id"]],
        }

        plan = [s1, s2, s3]
        logger.debug("Planner: plan created with %d steps", len(plan))

        return plan
