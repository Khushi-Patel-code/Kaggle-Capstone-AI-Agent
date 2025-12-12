# Academic & Productivity Multi-Agent Assistant for Students
### Concierge Agents
### Kaggle Capstone

## Team name: 404 Found

### Team members:
**Khushi Patel**
**Aadhya Patel**



## 🎯 1. The Problem (The Pitch: Core Concept & Value)

The biggest challenge for self-learners preparing for competitive exams is **creating an effective, personalized, and actionable study plan** that adapts to their specific time constraints and knowledge gaps.

* **Generic Plans:** Most available study guides are static and non-adaptive, leading to wasted time on already mastered topics or skipping critical subjects.
* **Overwhelm:** Students struggle to synthesize vast amounts of online research (timetables, important topics, best methods) into a single, cohesive strategy.
* **Lack of Structure:** Without a dedicated framework, maintaining consistency and focusing on the right materials becomes difficult.

## ✅ 2. The Solution: A Multi-Agent Framework

The **AI Learning Coach** is a multi-agent system designed to act as a virtual, integrated study consultant. It takes a high-level goal (e.g., "Prepare for my exam on the 15th") and automatically delivers a comprehensive, personalized study strategy, research summary, and daily timetable.

Our system provides **clear, meaningful value** by centralizing and automating the four critical tasks of study preparation: **Planning, Research, Synthesis, and Scheduling.**

## 🤖 3. Why a Multi-Agent Approach?

A single monolithic agent struggles with modularity, explainability, and extensibility.

This project adopts a **multi-agent architecture** to:
- Improve **separation of concerns**
- Allow **independent agent upgrades**
- Enable **clear reasoning traces** via session logs
- Support future expansion (e.g., quiz agent, progress tracker)

Each agent specializes in one cognitive task, mirroring real-world study workflows.


## 🛠️ 4. Architecture Overview (Implementation & Documentation)

The AI Learning Coach follows an **Orchestrator-driven pipeline** where specialized sub-agents perform sequential tasks, leveraging **Memory** and **Session** services for state management.


### **Agent Pipeline:**

1.  **Orchestrator (The Controller):** Manages the flow, logs progress via `SessionService`, and saves key artifacts via `MemoryService`.
2.  **Planner:** Generates a **structured, time-bound study plan** based on the user's goal, including both daily study tasks and specific research steps. *(Uses time calculation heuristics from `datetime`.)*
3.  **Researcher:** Executes the research queries identified by the Planner using a **simulated `GoogleSearchTool`**.
4.  **Summarizer:** Compresses the raw research snippets into a **concise summary** of key concepts and strategies, making the information actionable.
5.  **Coach:** Synthesizes the final plan and summary into a **motivational and actionable final output** for the user.
6.  **Timetable Agent (Bonus Feature):** Takes the strategic plan and a user's pre-defined `free_slots` to generate a **personalized, time-specific daily schedule** for maximum efficiency.

### System Execution Flow

User Goal  
→ Orchestrator  
→ Planner (creates structured plan)  
→ Researcher (collects supporting material)  
→ Summarizer (condenses information)  
→ Coach (generates guidance)  
→ Timetable Agent (allocates time slots)  
→ Final Output + Session Log

### **Key Concepts Applied**

This project successfully implements the following required concepts:

| Concept | Implementation Details |
| :--- | :--- |
| **Agent Orchestration** | The `Orchestrator` class explicitly manages the sequential flow and data handoff between all five sub-agents. |
| **Tool Use** | The `Researcher` agent uses the `GoogleSearchTool` to find supporting data for the plan. |
| **Memory** | The `MemoryService` is used by the `Orchestrator` to recall and store key outputs (`last_plan`, `last_summary`) for potential future context and refinement. |
| **Statefulness** | The `SessionService` maintains a full log of every step, timestamp, and message, providing a complete audit trail for the mission. |

## 🚀 5. Setup and Execution

### **Prerequisites**

You must have Python 3.10+ installed (tested on Python 3.13).

### **Setup Instructions**

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Khushi-Patel-code/AI-learning-coach-kaggle-capstone
    cd AI-learning-coach-kaggle-capstone
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Agent:**
    ```bash
    python main.py
    ```

### **Example Interaction**

When prompted, enter your goal:
```
Enter your learning goal: exam on 3rd dec
```

## 💡 6. Bonus Features

* **Timetable Agent:** A dedicated agent that translates abstract study steps into a concrete, time-blocked schedule based on user-provided free time slots.
* **Integrated Session Logging:** The `SessionService` provides complete transparency into the agent's decision-making process.

## ✍️ 7. Code Structure

```
Kaggle-Capstone-AI-Agent/
├── main.py
├── README.md
├── requirements.txt
├── agents/
│   ├── coach.py
│   ├── orchestrator.py
│   ├── planner.py
│   ├── research.py
│   ├── summarizer.py
│   ├── timetable.py
│   └── __pycache__/
│       ├── coach.cpython-313.pyc
│       ├── orchestrator.cpython-313.pyc
│       ├── planner.cpython-313.pyc
│       ├── research.cpython-313.pyc
│       ├── summarizer.cpython-313.pyc
│       └── timetable.cpython-313.pyc
├── services/
│   ├── memory_service.py
│   ├── session_service.py
│   └── __pycache__/
│       ├── memory_service.cpython-313.pyc
│       └── session_service.cpython-313.pyc
└── tools/
    ├── __init__.py
    ├── google_search_tool.py
    ├── plan_formatter.py
    ├── summarizer_tool.py
    └── __pycache__/
        ├── __init__.cpython-313.pyc
        ├── google_search_tool.cpython-313.pyc
        └── summarizer_tool.cpython-313.pyc
```

## ⚠️ 8. Limitations & Future Work

### Current Limitations
- Research is performed using a simulated search tool
- User availability (`free_slots`) is currently hard-coded
- No persistent storage beyond in-memory session lifetime

### Future Enhancements
- Integrate real web search APIs
- Add user profiles and long-term memory
- Introduce adaptive difficulty based on performance
- Add reminder & notification agent
- Web or GUI-based interface

## 👥 Authors (Team: 404 Found)

- Khushi Patel
- Aadhya Patel

