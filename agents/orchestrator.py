# agents/orchestrator.py

class Orchestrator:
    """
    Main controller that coordinates Planner → Researcher → Summarizer → Coach.
    Integrates MemoryService and SessionService for a full agent pipeline.
    """

    def __init__(self, planner, researcher, summarizer, coach, memory=None, session=None):
        self.planner = planner
        self.researcher = researcher
        self.summarizer = summarizer
        self.coach = coach
        self.memory = memory
        self.session = session

    # -------------------------------------------------------------
    # Internal helpers
    # -------------------------------------------------------------
    def log(self, message: str):
        """Store logs in session service if available."""
        print(f"[ORCH] {message}")  # console log
        if self.session:
            self.session.log(message)

    def remember(self, key: str, value: str):
        """Store memory if service exists."""
        if self.memory:
            self.memory.save(key, value)

    def recall(self, key: str):
        """Retrieve memory if available."""
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

        # FIX: Your planner uses plan(), not create_plan()
        plan = self.planner.plan(user_goal)
        self.remember("last_plan", plan)
        self.log("Plan created.")

        # 2. RESEARCH ---------------------------------------------------
        self.log("Searching the web for supporting material...")

        # FIX: research_topics() does NOT exist → replace with research(plan)
        research_results = self.researcher.research(plan)

        self.remember("last_research", str(research_results))
        self.log("Research complete.")

        # 3. SUMMARIZATION ---------------------------------------------
        self.log("Summarizing the research...")

        # FIX: summarize_research() does NOT exist → replace with summarize()
        summary = self.summarizer.summarize(research_results)

        self.remember("last_summary", summary)
        self.log("Summary complete.")

        # 4. COACHING ---------------------------------------------------
        self.log("Generating coaching insights...")
        final_output = self.coach.generate_advice(plan, summary)
        self.remember("last_output", final_output)
        self.log("Coaching step complete.")

        # 5. FINISH -----------------------------------------------------
        self.log("Mission complete.")
        return final_output
