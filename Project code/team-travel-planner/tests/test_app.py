import unittest
from app import Team, TravelDetail, Expense

class TestTravelPlanningTool(unittest.TestCase):
    def setUp(self):
        self.team = Team(team_id="T1", name="Wanderers")
        self.travel = TravelDetail(travel_id="TRV123", destination="London", start_date="2023-04-01", end_date="2023-04-10")
        self.expense = Expense(expense_id="EXP1001", amount=1000, category="Transport")

    def test_add_travel(self):
        self.team.add_travel(self.travel)
        self.assertIn("TRV123", self.team.travels)

    def test_remove_travel(self):
        self.team.add_travel(self.travel)
        self.team.remove_travel("TRV123")
        self.assertNotIn("TRV123", self.team.travels)

        def test_add_expense(self):
        self.travel.add_expense(self.expense)
        self.assertIn("EXP1001", self.travel.expenses)

    def test_remove_expense(self):
        self.travel.add_expense(self.expense)
        self.travel.remove_expense("EXP1001")
        self.assertNotIn("EXP1001", self.travel.expenses)

    def test_get_travel(self):
        self.team.add_travel(self.travel)
        self.assertEqual(self.team.get_travel("TRV123"), self.travel)

    def test_get_expense(self):
        self.travel.add_expense(self.expense)
        self.assertEqual(self.travel.get_expense("EXP1001"), self.expense)

if __name__ == "__main__":
    unittest.main()
