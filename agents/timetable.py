class TimetableAgent:
    """
    Generates a personalized daily timetable based on:
      - user goal
      - research summary
      - plan steps
      - free time slots
    """

    def generate_timetable(self, mission, plan, summary, user_schedule):
        timetable = []

        free_slots = user_schedule.get("free_slots", [])

        topics = [
    step.get("query", "Study")
    for step in plan
    if step.get("type") == "research"
]


        for i, (start, end) in enumerate(free_slots):
            topic = topics[i % len(topics)]
            timetable.append({
                "time": f"{start} - {end}",
                "study_topic": topic
            })

        return timetable
