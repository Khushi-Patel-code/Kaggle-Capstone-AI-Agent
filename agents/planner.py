# agents/planner.py
from datetime import datetime, timedelta
from typing import List, Dict, Any

class Planner:
    """Creates a practical, real-world study plan with research steps."""

    def plan(self, goal: str, previous_plan=None) -> List[Dict[str, Any]]:

        plan = []

        # 1. Extract exam date from goal if given
        exam_date = None
        for word in goal.split():
            if word.isdigit() and len(word) <= 2:
                try:
                    exam_date = datetime(datetime.now().year, datetime.now().month, int(word))
                except:
                    pass

        # 2. Determine total days for preparation
        days_diff = 7 # Default to 7 days
        if exam_date and exam_date > datetime.now():
            
            # Calculate difference, ensuring we count the current day as prep time.
            days_diff = (exam_date - datetime.now()).days + 1
        
        total_days = max(days_diff, 7)

        subjects = ["Maths", "Reasoning", "English", "GK"]

        # 3. Generate daily study tasks
        for i in range(total_days):
            day_plan = {
                "day": f"Day {i + 1}",
                "tasks": [
                    f"Study {subjects[i % len(subjects)]} for 2 hours",
                    "Practice 20 questions",
                    "Revise notes for 30 minutes",
                ]
            }
            plan.append(day_plan)

        # 4. Add final revision day
        plan.append({
            "day": "Final Revision",
            "tasks": [
                "Give full mock test",
                "Analyze mistakes",
                "Revise weak topics"
            ]
        })

        # 5. Add separate research steps
        research_steps = [
            {"type": "research", "query": f"Best way to prepare for {goal} exam"},
            {"type": "research", "query": f"Important topics for {goal} exam"},
            {"type": "research", "query": f"Revision plan for {goal} exam"}
        ]

        plan.extend(research_steps)
        return plan
