# main.py
from agents.orchestrator import Orchestrator
from agents.planner import Planner
from agents.research import Researcher
from agents.summarizer import Summarizer
from agents.coach import Coach
from agents.timetable import TimetableAgent
from services.memory_service import MemoryService
from services.session_service import SessionService


def main():
    print("\n==============================")
    print("   AI Learning Coach Agent")
    print("==============================\n")

    # Initialize services
    memory = MemoryService()
    session = SessionService()

    # Initialize agents
    orch = Orchestrator(
        planner=Planner(),
        researcher=Researcher(),
        summarizer=Summarizer(),
        coach=Coach(),
        timetable=TimetableAgent(),
        memory=memory,
        session=session
    )

    # User input
    user_goal = input("Enter your learning goal: ")

    # Run full agent pipeline
    print("\nRunning AI Agent...\n")
    result = orch.run_mission(user_goal)

    print("\n==============================")
    print("         FINAL OUTPUT")
    print("==============================\n")
    print(result)

    print("\n==============================")
    print("      SESSION INFORMATION")
    print("==============================\n")
    print(session.get_session_info())
    print("\nSession History:")
    for entry in session.get_history():
        print(f"- {entry['time']}: {entry['message']}")


if __name__ == "__main__":
    main()
