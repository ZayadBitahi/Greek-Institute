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

def get_patient(patient_id):
    cursor.execute("SELECT * FROM patients WHERE id = %s", (patient_id,))
    return cursor.fetchone()

def create_patient(first_name, last_name, date_of_birth, gender, contact_info):
    cursor.execute(
        "INSERT INTO patients (first_name, last_name, date_of_birth, gender, contact_info) VALUES (%s, %s, %s, %s, %s) RETURNING id",
        (first_name, last_name, date_of_birth, gender, contact_info)
    )
    new_id = cursor.fetchone()[0]
    conn.commit()
    return new_id


def update_patient(patient_id, first_name, last_name, date_of_birth, gender, contact_info):
    cursor.execute(
        "UPDATE patients SET first_name = %s, last_name = %s, date_of_birth = %s, gender = %s, contact_info = %s WHERE id = %s",
        (first_name, last_name, date_of_birth, gender, contact_info, patient_id)
    )
    conn.commit()

def delete_patient(patient_id):
    cursor.execute("DELETE FROM patients WHERE id = %s", (patient_id,))
    conn.commit()

def search_patients(keyword):
    if not keyword:
        return get_patients()
    return [p for p in get_patients() if keyword.lower() in p[1].lower() or keyword.lower() in p[2].lower()]

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

def get_billing():
    cursor.execute("SELECT * FROM billing ORDER BY id")
    return cursor.fetchall()

def get_bill(bill_id):
    cursor.execute("SELECT * FROM billing WHERE id = %s", (bill_id,))
    return cursor.fetchone()

def create_billing(patient_id, amount, billing_date, paid_status):
    cursor.execute(
        "INSERT INTO billing (patient_id, amount, billing_date, paid_status) VALUES (%s, %s, %s, %s)",
        (patient_id, amount, billing_date, paid_status)
    )
    conn.commit()

def update_billing(bill_id, patient_id, amount, billing_date, paid_status):
    cursor.execute(
        "UPDATE billing SET patient_id = %s, amount = %s, billing_date = %s, paid_status = %s WHERE id = %s",
        (patient_id, amount, billing_date, paid_status, bill_id)
    )
    conn.commit()

def delete_billing(bill_id):
    cursor.execute("DELETE FROM billing WHERE id = %s", (bill_id,))
    conn.commit()

def get_doctors_with_department(department_id=None):
    if department_id is not None:
        cursor.execute("""
            SELECT d.id, d.first_name, d.last_name, d.specialty, d.email,
                   COALESCE(dep.name,'') AS department_name
            FROM doctors d
            LEFT JOIN departments dep ON d.department_id = dep.id
            WHERE d.department_id = %s
            ORDER BY d.id
        """, (int(department_id),))
    else:
        cursor.execute("""
            SELECT d.id, d.first_name, d.last_name, d.specialty, d.email,
                   COALESCE(dep.name,'') AS department_name
            FROM doctors d
            LEFT JOIN departments dep ON d.department_id = dep.id
            ORDER BY d.id
        """)
    return cursor.fetchall()

def get_doctors_filtered(q=None, department_id=None):
    sql = """
        SELECT d.id, d.first_name, d.last_name, d.specialty, d.email, COALESCE(dep.name,'')
        FROM doctors d
        LEFT JOIN departments dep ON d.department_id = dep.id
    """
    where = []
    params = []
    if department_id:
        where.append("d.department_id = %s")
        params.append(int(department_id))
    if q:
        like = f"%{q}%"
        where.append("(d.first_name ILIKE %s OR d.last_name ILIKE %s OR d.specialty ILIKE %s OR d.email ILIKE %s OR dep.name ILIKE %s)")
        params.extend([like, like, like, like, like])
    if where:
        sql += " WHERE " + " AND ".join(where)
    sql += " ORDER BY d.id"
    cursor.execute(sql, tuple(params))
    return cursor.fetchall()

def get_appointments_filtered(q=None, start=None, end=None):
    sql = """
        SELECT a.id,
               p.first_name || ' ' || p.last_name AS patient_name,
               d.first_name || ' ' || d.last_name AS doctor_name,
               a.appointment_date,
               a.reason,
               a.patient_id,
               a.doctor_id
        FROM appointments a
        JOIN patients p ON a.patient_id = p.id
        JOIN doctors d ON a.doctor_id = d.id
    """
    where = []
    params = []
    if q:
        like = f"%{q}%"
        where.append("(p.first_name ILIKE %s OR p.last_name ILIKE %s OR d.first_name ILIKE %s OR d.last_name ILIKE %s OR a.reason ILIKE %s)")
        params.extend([like, like, like, like, like])
    if start:
        where.append("a.appointment_date >= %s")
        params.append(start)
    if end:
        where.append("a.appointment_date <= %s")
        params.append(end)
    if where:
        sql += " WHERE " + " AND ".join(where)
    sql += " ORDER BY a.appointment_date DESC, a.id DESC"
    cursor.execute(sql, tuple(params))
    return cursor.fetchall()

def get_bills_with_patient(start_date=None, end_date=None, status=None, q=None):
    sql = """
        SELECT b.id, p.first_name, p.last_name, b.amount, b.billing_date, b.paid_status, b.patient_id
        FROM billing b
        JOIN patients p ON b.patient_id = p.id
    """
    where = []
    params = []
    if start_date:
        where.append("b.billing_date >= %s")
        params.append(start_date)
    if end_date:
        where.append("b.billing_date <= %s")
        params.append(end_date)
    if status is not None:
        where.append("b.paid_status = %s")
        params.append(bool(status))
    if q:
        like = f"%{q}%"
        where.append("(p.first_name ILIKE %s OR p.last_name ILIKE %s)")
        params.extend([like, like])
    if where:
        sql += " WHERE " + " AND ".join(where)
    sql += " ORDER BY b.billing_date DESC, b.id DESC"
    cursor.execute(sql, tuple(params))
    return cursor.fetchall()
