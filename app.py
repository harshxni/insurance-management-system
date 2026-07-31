from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")



@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        password = request.form['password']

        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO customer(name, email, phone, address, password) VALUES (?, ?, ?, ?, ?)",
            (name, email, phone, address, password)
        )

        connection.commit()
        connection.close()

        return "Registration Successful!"

    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM customer WHERE email=? AND password=?",
            (email, password)
        )

        user = cursor.fetchone()

        connection.close()

        if user:
            return render_template("dashboard.html")
        else:
            return "Invalid Email or Password"

    return render_template("login.html")


@app.route('/policies')
def policies():

    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM policy")

    policies = cursor.fetchall()

    connection.close()

    return render_template("policies.html", policies=policies)


@app.route('/apply')
def apply():

    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM policy")

    policies = cursor.fetchall()

    connection.close()

    return render_template("apply.html", policies=policies)

@app.route('/apply_policy', methods=['POST'])
def apply_policy():

    policy_name = request.form['policy_name']

    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO application(customer_email, policy_name, status) VALUES (?, ?, ?)",
        ("customer@gmail.com", policy_name, "Applied")
    )

    connection.commit()
    connection.close()

    return "Policy Applied Successfully!"

@app.route('/applications')
def applications():

    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM application")

    applications = cursor.fetchall()

    connection.close()

    return render_template("applications.html", applications=applications)

@app.route('/payment', methods=['GET', 'POST'])
def payment():

    if request.method == 'POST':

        policy_name = request.form['policy_name']
        amount = request.form['amount']

        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        cursor.execute(
    "INSERT INTO payment(customer_name, policy_name, amount) VALUES (?, ?, ?)",
    ("Customer", policy_name, amount)
)

        connection.commit()
        connection.close()

        return "Payment Successful!"

    return render_template("payment.html")

@app.route('/payments')
def payments():

    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM payment")

    payments = cursor.fetchall()

    connection.close()

    return render_template("payments.html", payments=payments)

@app.route('/claim', methods=['GET', 'POST'])
def claim():

    if request.method == 'POST':

        policy_name = request.form['policy_name']
        claim_reason = request.form['claim_reason']

        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        cursor.execute(
    "INSERT INTO claim(customer_name, policy_name, reason, status) VALUES (?, ?, ?, ?)",
    ("Customer", policy_name, claim_reason, "Pending")
)

        connection.commit()
        connection.close()

        return "Claim Submitted Successfully!"

    return render_template("claim.html")

@app.route('/claims')
def claims():

    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM claim")

    claims = cursor.fetchall()

    connection.close()

    return render_template("claims.html", claims=claims)


if __name__ == '__main__':
    app.run(debug=True)


