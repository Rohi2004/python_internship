from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

# Classes for Entity Representation
class Expense:
    def __init__(self, expense_id, amount, category, description=""):
        self.expense_id = expense_id
        self.amount = amount
        self.category = category
        self.description = description

class TravelDetail:
    def __init__(self, travel_id, destination, start_date, end_date):
        self.travel_id = travel_id
        
        self.destination = destination
        self.start_date = start_date
        self.end_date = end_date
        self.expenses = {}

    def add_expense(self, expense):
        self.expenses[expense.expense_id] = expense

    def remove_expense(self, expense_id):
        if expense_id in self.expenses:
            del self.expenses[expense_id]

    def update_expense(self, expense_id, amount, category, description):
        if expense_id in self.expenses:
            self.expenses[expense_id].amount = amount
            self.expenses[expense_id].category = category
            self.expenses[expense_id].description = description

class Team:
    def __init__(self, team_id, name):
        self.team_id = team_id
        self.name = name
        self.travels = {}

    def add_travel(self, travel):
        self.travels[travel.travel_id] = travel

    def remove_travel(self, travel_id):
        if travel_id in self.travels:
            del self.travels[travel_id]

# Global dictionaries to manage data
teams = {}
travel_details = {}

# Service function to organize team travels
def organize_team_travels(team_id):
    team = teams.get(team_id)
    if not team:
        return "Team not found", 404
    return team.travels

# CRUD Routes for Travel Details
@app.route('/travel/<travel_id>', methods=['GET'])
def travel_details_view(travel_id):
    travel = travel_details.get(travel_id)
    if not travel:
        return "Travel not found", 404
    return render_template('travel.html', travel=travel)

@app.route('/travel', methods=['POST'])
def add_travel():
    travel_id = request.form.get('travel_id')
    destination = request.form.get('destination')
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')

    new_travel = TravelDetail(travel_id=travel_id, destination=destination, start_date=start_date, end_date=end_date)
    travel_details[travel_id] = new_travel

    return redirect(url_for('travel_details_view', travel_id=travel_id))

# CRUD Routes for Expenses
@app.route('/travel/<travel_id>/add_expense', methods=['POST'])
def add_expense(travel_id):
    travel = travel_details.get(travel_id)
    if not travel:
        return jsonify({'success': False, 'message': 'Travel not found'})

    expense_id = request.form.get('expense_id')
    amount = float(request.form.get('amount'))
    category = request.form.get('category')
    description = request.form.get('description')

    new_expense = Expense(expense_id=expense_id, amount=amount, category=category, description=description)
    travel.add_expense(new_expense)

    return jsonify({'success': True})

@app.route('/travel/<travel_id>/update_expense/<expense_id>', methods=['POST'])
def update_expense(travel_id, expense_id):
    travel = travel_details.get(travel_id)
    if not travel:
        return jsonify({'success': False, 'message': 'Travel not found'})

    amount = float(request.form.get('amount'))
    category = request.form.get('category')
    description = request.form.get('description')

    travel.update_expense(expense_id, amount, category, description)
    return jsonify({'success': True})

@app.route('/travel/<travel_id>/remove_expense/<expense_id>', methods=['POST'])
def remove_expense(travel_id, expense_id):
    travel = travel_details.get(travel_id)
    if not travel:
        return jsonify({'success': False, 'message': 'Travel not found'})

    travel.remove_expense(expense_id)
    return jsonify({'success': True})

if __name__ == "__main__":
    app.run(debug=True)
