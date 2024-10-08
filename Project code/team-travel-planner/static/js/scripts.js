document.addEventListener("DOMContentLoaded", function () {
    // Handle remove expense
    document.querySelectorAll('.remove-expense').forEach(button => {
        button.addEventListener('click', function () {
            const expenseId = this.dataset.expenseId;
            fetch(`/travel/${travelId}/remove_expense/${expenseId}`, {
                method: 'POST'
            }).then(response => {
                if (response.ok) {
                    document.getElementById(`expense-${expenseId}`).remove();
                }
            });
        });
    });

    // Handle update expense
    document.querySelectorAll('.update-expense').forEach(button => {
        button.addEventListener('click', function () {
            const expenseId = this.dataset.expenseId;
            const expenseItem = document.getElementById(`expense-${expenseId}`);
            const amount = expenseItem.innerText.split(' - ')[1].replace('$', '');
            const category = expenseItem.innerText.split(' - ')[0];
            const description = expenseItem.innerText.split(' - ')[2];

            document.getElementById('update-expense-id').value = expenseId;
            document.getElementById('update-amount').value = amount;
            document.getElementById('update-category').value = category;
            document.getElementById('update-description').value = description;

            document.getElementById('update-expense-form').style.display = 'block';
        });
    });

    document.getElementById('update-expense-form').addEventListener('submit', function (e) {
        e.preventDefault();
        const expenseId = document.getElementById('update-expense-id').value;
        const formData = new FormData(this);

        fetch(`/travel/${travelId}/update_expense/${expenseId}`, {
            method: 'POST',
            body: formData
        }).then(response => {
            if (response.ok) {
                const expenseItem = document.getElementById(`expense-${expenseId}`);
                const newAmount = document.getElementById('update-amount').value;
                const newCategory = document.getElementById('update-category').value;
                const newDescription = document.getElementById('update-description').value;

                expenseItem.innerHTML = `${newCategory} - $${newAmount} - ${newDescription}`;
                document.getElementById('update-expense-form').style.display = 'none';
            }
        });
    });
});
