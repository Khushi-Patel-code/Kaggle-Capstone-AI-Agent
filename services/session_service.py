# services/session_service.py

"""
Tracks project session info such as:
- session ID
- timestamps
- user query history
"""

import uuid
from datetime import datetime

class SessionService:

    def __init__(self):
        self.session_id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.history = []  # stores list of messages/steps

    def log(self, message: str):
        """Adds an entry to the session history."""
        timestamp = datetime.utcnow().isoformat()
        self.history.append({"time": timestamp, "message": message})

    def get_history(self):
        """Returns the full session log."""
        return self.history

    def get_session_info(self):
        """Returns metadata about the session."""
        return {
            "session_id": self.session_id,
            "created_at": self.created_at.isoformat(),
            "messages_logged": len(self.history),
        }
