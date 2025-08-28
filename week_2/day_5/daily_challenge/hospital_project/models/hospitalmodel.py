from database.index import conn, cursor


def get_departments():
    cursor.execute("SELECT * FROM departments ORDER BY id")
    return cursor.fetchall()

def get_department(dept_id):
    cursor.execute("SELECT * FROM departments WHERE id = %s", (dept_id,))
    return cursor.fetchone()

def create_department(name, location):
    cursor.execute("INSERT INTO departments (name, location) VALUES (%s, %s)", (name, location))
    conn.commit()

def update_department(dept_id, name, location):
    cursor.execute("UPDATE departments SET name = %s, location = %s WHERE id = %s", (name, location, dept_id))
    conn.commit()

def delete_department(dept_id):
    cursor.execute("DELETE FROM departments WHERE id = %s", (dept_id,))
    conn.commit()

def get_doctors():
    cursor.execute("SELECT * FROM doctors ORDER BY id")
    return cursor.fetchall()

def get_doctor(doc_id):
    cursor.execute("SELECT * FROM doctors WHERE id = %s", (doc_id,))
    return cursor.fetchone()

def create_doctor(first_name, last_name, specialty, email, department_id):
    cursor.execute(
        "INSERT INTO doctors (first_name, last_name, specialty, email, department_id) VALUES (%s, %s, %s, %s, %s)",
        (first_name, last_name, specialty, email, department_id)
    )
    conn.commit()

def update_doctor(doc_id, first_name, last_name, specialty, email, department_id):
    cursor.execute(
        "UPDATE doctors SET first_name = %s, last_name = %s, specialty = %s, email = %s, department_id = %s WHERE id = %s",
        (first_name, last_name, specialty, email, department_id, doc_id)
    )
    conn.commit()

def delete_doctor(doc_id):
    cursor.execute("DELETE FROM doctors WHERE id = %s", (doc_id,))
    conn.commit()

def get_patients():
    cursor.execute("SELECT * FROM patients ORDER BY id")
    return cursor.fetchall()

def get_patients():
    cursor.execute("SELECT * FROM patients ORDER BY id")
    return cursor.fetchall()


def create_patient(first_name, last_name, date_of_birth, gender, contact_info):
    query = "INSERT INTO patients (first_name, last_name, date_of_birth, gender, contact_info) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (first_name, last_name, date_of_birth, gender, contact_info))
    conn.commit()



def update_patient(patient_id, first_name, last_name, date_of_birth, gender, contact_info):
    cursor.execute(
        "UPDATE patients SET first_name = %s, last_name = %s, date_of_birth = %s, gender = %s, contact_info = %s WHERE id = %s",
        (first_name, last_name, date_of_birth, gender, contact_info, patient_id)
    )
    conn.commit()

def delete_patient(patient_id):
    cursor.execute("DELETE FROM patients WHERE id = %s", (patient_id,))
    conn.commit()

def get_appointments():
    cursor.execute("SELECT * FROM appointments ORDER BY id")
    return cursor.fetchall()

def get_appointment(app_id):
    cursor.execute("SELECT * FROM appointments WHERE id = %s", (app_id,))
    return cursor.fetchone()

def create_appointment(patient_id, doctor_id, appointment_date, reason):
    cursor.execute(
        "INSERT INTO appointments (patient_id, doctor_id, appointment_date, reason) VALUES (%s, %s, %s, %s)",
        (patient_id, doctor_id, appointment_date, reason)
    )
    conn.commit()

def update_appointment(app_id, patient_id, doctor_id, appointment_date, reason):
    cursor.execute(
        "UPDATE appointments SET patient_id = %s, doctor_id = %s, appointment_date = %s, reason = %s WHERE id = %s",
        (patient_id, doctor_id, appointment_date, reason, app_id)
    )
    conn.commit()

def delete_appointment(app_id):
    cursor.execute("DELETE FROM appointments WHERE id = %s", (app_id,))
    conn.commit()

def get_bills():
    cursor.execute("SELECT * FROM billing ORDER BY id")
    return cursor.fetchall()

def get_bill(bill_id):
    cursor.execute("SELECT * FROM billing WHERE id = %s", (bill_id,))
    return cursor.fetchone()

def create_bill(patient_id, amount, billing_date, paid_status):
    cursor.execute(
        "INSERT INTO billing (patient_id, amount, billing_date, paid_status) VALUES (%s, %s, %s, %s)",
        (patient_id, amount, billing_date, paid_status)
    )
    conn.commit()

def update_bill(bill_id, patient_id, amount, billing_date, paid_status):
    cursor.execute(
        "UPDATE billing SET patient_id = %s, amount = %s, billing_date = %s, paid_status = %s WHERE id = %s",
        (patient_id, amount, billing_date, paid_status, bill_id)
    )
    conn.commit()

def delete_bill(bill_id):
    cursor.execute("DELETE FROM billing WHERE id = %s", (bill_id,))
    conn.commit()

def search_patients(keyword):
    if not keyword:
        return get_patients()
    return [p for p in get_patients() if keyword.lower() in p[1].lower() or keyword.lower() in p[2].lower()]
