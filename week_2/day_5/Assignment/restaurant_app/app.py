from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)


def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="restaurant",  
        user="postgres",           
        password="2939978"         
    )


@app.route("/")
def home():
    return redirect(url_for("menu"))


@app.route("/menu")
def menu():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Menu_Items ORDER BY id;")
    items = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("menu.html", items=items)


@app.route("/add", methods=["GET", "POST"])
def add_item():
    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)",
            (name, price)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for("menu"))
    
    return render_template("add_item.html")


@app.route("/delete/<int:item_id>")
def delete_item(item_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Menu_Items WHERE id = %s", (item_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for("menu"))

@app.route('/update/<int:item_id>', methods=['GET', 'POST'])
def update_item(item_id):
    conn = get_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        cursor.execute(
            "UPDATE Menu_Items SET item_name=%s, item_price=%s WHERE id=%s",
            (name, price, item_id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('menu'))
    cursor.execute("SELECT id, item_name, item_price FROM Menu_Items WHERE id=%s", (item_id,))
    item = cursor.fetchone()
    cursor.close()
    conn.close()

    if not item:
        return "Item not found", 404
    return render_template('update_item.html', item=item)

@app.route('/stats')
def stats():
    patient_count = 120
    doctor_count = 25
    appointment_count = 340

    return render_template(
        'stats.html',
        patient_count=patient_count,
        doctor_count=doctor_count,
        appointment_count=appointment_count
    )


