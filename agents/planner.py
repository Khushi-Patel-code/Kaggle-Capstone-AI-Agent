# agents/planner.py

from datetime import datetime, timedelta
from typing import List, Dict, Any

class Planner:
    """Creates a practical, real-world study plan."""

    def plan(self, goal: str, previous_plan=None) -> List[Dict[str, Any]]:
        
        # Example: goal = "Exam on 15 Dec"
        
        plan = []

        # 1. Extract exam date (optional — if user gives a date)
        exam_date = None
        for word in goal.split():
            if word.isdigit() and len(word) == 2:
                try:
                    exam_date = datetime(datetime.now().year, datetime.now().month, int(word))
                except:
                    pass
        
        # If date missing, assume 7-day preparation
        total_days = 7 if not exam_date else (exam_date - datetime.now()).days
        
        subjects = ["Maths", "Reasoning", "English", "GK"]  # You can also make it dynamic
        
        # 2. Generate daily tasks
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

        # 3. Add final revision day
        plan.append({
            "day": "Final Revision",
            "tasks": [
                "Give full mock test",
                "Analyze mistakes",
                "Revise weak topics"
            ]
        })

        return [
    {"type": "research", "query": f"Best way to prepare for {goal} exam"},
    {"type": "study", "query": f"Important topics for {goal} exam"},
    {"type": "revision", "query": f"Revision plan for {goal} exam"}
]

