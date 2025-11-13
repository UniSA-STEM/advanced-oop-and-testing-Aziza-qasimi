"""
File: health_record.py
Description: Class to manage animal health records.
Author: Aziza Qasimi
ID: <YourID>
Username: <YourUsername>
This is my own work as defined by the University's Academic Integrity Policy.
"""

import datetime

class HealthRecord:
    """Represents a health record for an animal."""

    def __init__(self, description: str, severity: int, date_reported=None):
        if not 1 <= severity <= 5:
            raise ValueError("Severity must be between 1 (low) and 5 (critical).")
        self.description = description
        self.severity = severity
        self.date_reported = date_reported or datetime.date.today()
        self.treatment_notes = []
        self.is_open = True  # True if the issue is active

    def add_treatment(self, note: str):
        """Add a treatment note to the record."""
        self.treatment_notes.append(note)
        print(f"Treatment note added: {note}")

    def close_record(self):
        """Mark the health record as closed."""
        self.is_open = False
        print(f"Health record '{self.description}' is now closed.")

    def summary(self):
        """Return a summary dictionary for reporting."""
        return {
            "description": self.description,
            "severity": self.severity,
            "date_reported": self.date_reported,
            "treatments": self.treatment_notes,
            "is_open": self.is_open
        }
