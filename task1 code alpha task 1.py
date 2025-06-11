import difflib

class DataRedundancyRemovalSystem:
    def __init__(self):  # Fixed the constructor
        self.database = []

    def is_similar(self, new_entry, existing_entry, threshold=0.9):
        similarity = difflib.SequenceMatcher(None, new_entry.lower(), existing_entry.lower()).ratio()
        return similarity >= threshold

    def validate_data(self, new_entry):
        for entry in self.database:
            if self.is_similar(new_entry, entry):
                print(f"⚠ Redundant or False Positive Detected: '{new_entry}' ~ '{entry}'")
                return False
        return True

    def add_data(self, new_entry):
        if self.validate_data(new_entry):
            self.database.append(new_entry)
            print(f"✅ Added: {new_entry}")
        else:
            print(f"❌ Entry skipped: {new_entry}")

    def show_database(self):
        print("\n📂 Current Database Entries:")
        for idx, entry in enumerate(self.database, start=1):
            print(f"{idx}. {entry}")

# Example Usage
system = DataRedundancyRemovalSystem()

entries = [
    "Customer ID 12345 - John Doe",
    "Customer ID 12345 - John Doe",
    "Customer ID 12346 - Jon Doe",
    "Customer ID 12347 - Jane Doe",
    "Customer ID 12345 - John Doe "
]

for entry in entries:
    system.add_data(entry)

system.show_database()
