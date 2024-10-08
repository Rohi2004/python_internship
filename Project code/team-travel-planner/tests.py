import unittest

# Assuming you have the classes Team, TravelDetail, and Expense defined in app.py
from app import Team, TravelDetail, Expense

class TestTravelPlanning(unittest.TestCase):

    def setUp(self):
        self.team = Team("001", "Team A")
        self.travel = TravelDetail("T001", "Paris", "2024-09-01", "2024-09-10")
        self.expense = Expense("E001", 100, "Accommodation", "Hotel stay in Paris")
        self.team.add_travel(self.travel)

    def test_add_travel(self):
        self.assertIn("T001", self.team.travels)

    def test_add_expense(self):
        self.travel.add_expense(self.expense)
        self.assertIn("E001", self.travel.expenses)

    def test_update_expense(self):
        self.travel.add_expense(self.expense)
        self.travel.update_expense("E001", 150, "Accommodation", "Updated hotel stay")
        self.assertEqual(self.travel.expenses["E001"].amount, 150)

    def test_remove_expense(self):
        self.travel.add_expense(self.expense)
        self.travel.remove_expense("E001")
        self.assertNotIn("E001", self.travel.expenses)

if __name__ == "__main__":
    unittest.main()
