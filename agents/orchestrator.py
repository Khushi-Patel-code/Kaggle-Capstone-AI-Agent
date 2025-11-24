class Orchestrator:
    """
    Main controller that coordinates Planner → Researcher → Summarizer → Coach.
    Integrates MemoryService and SessionService for a full agent pipeline.
    """

    def __init__(self, planner, researcher, summarizer, coach, timetable=None, memory=None, session=None):
        self.planner = planner
        self.researcher = researcher
        self.summarizer = summarizer
        self.coach = coach
        self.timetable = timetable   # <-- ADD THIS
        self.memory = memory
        self.session = session

    # -------------------------------------------------------------
    # Internal helpers
    # -------------------------------------------------------------
    def log(self, message: str):
        print(f"[ORCH] {message}")
        if self.session:
            self.session.log(message)

    def remember(self, key: str, value: str):
        if self.memory:
            self.memory.save(key, value)

    def recall(self, key: str):
        if self.memory:
            return self.memory.get(key)
        return None

    # -------------------------------------------------------------
    # MAIN PIPELINE
    # -------------------------------------------------------------
    def run_mission(self, user_goal: str) -> str:
        self.log(f"Mission started for goal: '{user_goal}'")
        self.remember("last_goal", user_goal)

        # 1. PLANNING ---------------------------------------------------
        self.log("Generating study plan...")
        prior_plan = self.recall("last_plan")
        if prior_plan:
            self.log("Found prior plan. Including context into planning step.")

        plan = self.planner.plan(user_goal)
        self.remember("last_plan", plan)
        self.log("Plan created.")

        # 2. RESEARCH ---------------------------------------------------
        self.log("Searching the web for supporting material...")
        research_results = self.researcher.research(plan)
        self.remember("last_research", str(research_results))
        self.log("Research complete.")

        # 3. SUMMARIZATION ---------------------------------------------
        self.log("Summarizing the research...")
        summary = self.summarizer.summarize(research_results)
        self.remember("last_summary", summary)
        self.log("Summary complete.")

        # 4. COACHING ---------------------------------------------------
        self.log("Generating coaching insights...")
        final_output = self.coach.create_output(user_goal, plan, summary)
        self.remember("last_output", final_output)
        self.log("Coaching step complete.")

        # ---------------------------------------------------------------
        # 5. TIMETABLE GENERATION  <-- ADD THIS WHOLE BLOCK
        # ---------------------------------------------------------------
        if self.timetable:
            self.log("Generating personalized timetable...")

            user_schedule = {
                "free_slots": [
                    ("06:00", "08:00"),
                    ("18:00", "20:00"),
                    ("21:00", "22:30")
                ]
            }

            timetable = self.timetable.generate_timetable(
                user_goal,
                plan,
                summary,
                user_schedule
            )

            self.remember("last_timetable", timetable)
            final_output["timetable"] = timetable
            self.log("Timetable generation complete.")
        else:
            self.log("No timetable agent available. Skipping timetable step.")

        # 6. FINISH -----------------------------------------------------
        self.log("Mission complete.")
        return final_output
