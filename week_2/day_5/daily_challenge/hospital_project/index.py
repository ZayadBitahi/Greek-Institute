from flask import Flask, render_template, request, redirect, flash
import psycopg2
import models.hospitalmodel as hm
from database.index import conn, cursor

app = Flask(__name__)
app.secret_key = "dev-secret"

@app.before_request
def _db_reset_tx():
    try:
        conn.rollback()
    except Exception:
        pass

@app.route('/')
def home():
    page = int(request.args.get('page', 1))
    per_page = 6
    search = request.args.get('search', '')

    patients = hm.search_patients(search)
    total = len(patients)
    start = (page - 1) * per_page
    end = start + per_page
    paginated = patients[start:end]

    total_pages = (total + per_page - 1) // per_page

    return render_template('index.html', patients=paginated, page=page, total_pages=total_pages, search=search)


@app.route('/patient/create', methods=['GET', 'POST'])
def create_patient():
    if request.method == 'POST':
        hm.create_patient(
            request.form['first_name'],
            request.form['last_name'],
            request.form['date_of_birth'],
            request.form['gender'],
            request.form['contact_info']
        )
        return redirect('/')
    return render_template('create.html')

@app.route('/patient/edit/<int:id>', methods=['GET', 'POST'])
def edit_patient(id):
    patient = hm.get_patient(id)
    if request.method == 'POST':
        hm.update_patient(
            id,
            request.form['first_name'],
            request.form['last_name'],
            request.form['date_of_birth'],
            request.form['gender'],
            request.form['contact_info']
        )
        return redirect('/')
    return render_template('edit.html', patient=patient)

@app.route('/patient/delete/<int:id>')
def delete_patient(id):
    hm.delete_patient(id)
    return redirect('/')


@app.route('/doctor')
def doctor_list():
    dept_id = request.args.get('department_id', '').strip()
    q = request.args.get('q', '').strip()
    doctors = hm.get_doctors_filtered(q or None, int(dept_id) if dept_id else None)
    departments = hm.get_departments()
    return render_template('doctorindex.html', doctors=doctors, departments=departments, selected_department=dept_id, q=q)

@app.route('/doctor/create', methods=['GET', 'POST'])
def doctor_create():
    if request.method == 'POST':
        department_id = request.form.get('department_id') or None
        hm.create_doctor(
            request.form['first_name'],
            request.form['last_name'],
            request.form['specialty'],
            request.form['email'],
            int(department_id) if department_id else None
        )
        return redirect('/doctor')
    departments = hm.get_departments()
    return render_template('doctorcreate.html', departments=departments)

@app.route('/doctor/edit/<int:id>', methods=['GET', 'POST'])
def doctor_edit(id):
    if request.method == 'POST':
        department_id = request.form.get('department_id') or None
        hm.update_doctor(
            id,
            request.form['first_name'],
            request.form['last_name'],
            request.form['specialty'],
            request.form['email'],
            int(department_id) if department_id else None
        )
        return redirect('/doctor')
    doctor = hm.get_doctor(id)
    departments = hm.get_departments()
    return render_template('doctoredit.html', doctor=doctor, departments=departments)


@app.route('/doctor/delete/<int:id>')
def doctor_delete(id):
    hm.delete_doctor(id)
    return redirect('/doctor')


@app.route('/department')
def department_list():
    departments = hm.get_departments()
    return render_template('departmentindex.html', departments=departments)

@app.route('/department/create', methods=['GET', 'POST'])
def department_create():
    if request.method == 'POST':
        hm.create_department(request.form['name'], request.form['location'])
        return redirect('/department')
    return render_template('departmentcreate.html')

@app.route('/department/edit/<int:id>', methods=['GET', 'POST'])
def department_edit(id):
    if request.method == 'POST':
        hm.update_department(id, request.form['name'], request.form['location'])
        return redirect('/department')
    department = hm.get_department(id)
    return render_template('departmentedit.html', department=department)


@app.route('/department/delete/<int:id>')
def department_delete(id):
    hm.delete_department(id)
    return redirect('/department')


@app.route('/appointment')
def appointment_list():
    q = request.args.get('q', '').strip()
    start = request.args.get('start', '').strip() or None
    end = request.args.get('end', '').strip() or None
    appointments = hm.get_appointments_filtered(q or None, start, end)
    return render_template('appointmentindex.html', appointments=appointments, q=q, start=start or '', end=end or '')



@app.route('/appointment/create', methods=['GET', 'POST'])
def appointment_create():
    if request.method == 'POST':
        try:
            patient_id = int(request.form['patient_id'])
            doctor_id = int(request.form['doctor_id'])
        except ValueError:
            flash('Invalid IDs')
            return redirect('/appointment/create')

        appointment_date = request.form['appointment_date']
        reason = request.form['reason']

        if not hm.get_patient(patient_id):
            flash('Selected patient does not exist')
            return redirect('/appointment/create')
        if not hm.get_doctor(doctor_id):
            flash('Selected doctor does not exist')
            return redirect('/appointment/create')

        hm.create_appointment(patient_id, doctor_id, appointment_date, reason)
        return redirect('/appointment')

    patients = hm.get_patients()
    doctors = hm.get_doctors()
    return render_template('appointmentcreate.html', patients=patients, doctors=doctors)

@app.route('/appointment/edit/<int:id>', methods=['GET', 'POST'])
def appointment_edit(id):
    if request.method == 'POST':
        try:
            patient_id = int(request.form['patient_id'])
            doctor_id = int(request.form['doctor_id'])
        except ValueError:
            flash('Invalid IDs')
            return redirect(f'/appointment/edit/{id}')

        appointment_date = request.form['appointment_date']
        reason = request.form['reason']

        if not hm.get_patient(patient_id):
            flash('Selected patient does not exist')
            return redirect(f'/appointment/edit/{id}')
        if not hm.get_doctor(doctor_id):
            flash('Selected doctor does not exist')
            return redirect(f'/appointment/edit/{id}')

        hm.update_appointment(id, patient_id, doctor_id, appointment_date, reason)
        return redirect('/appointment')

    appointment = hm.get_appointment(id)
    patients = hm.get_patients()
    doctors = hm.get_doctors()
    return render_template('appointmentedit.html', appointment=appointment, patients=patients, doctors=doctors)


@app.route('/appointment/delete/<int:id>')
def appointment_delete(id):
    hm.delete_appointment(id)
    return redirect('/appointment')


@app.route('/billing')
def billing_list():
    status_param = request.args.get('status', '').strip()
    start_date = request.args.get('start', '').strip() or None
    end_date = request.args.get('end', '').strip() or None
    q = request.args.get('q', '').strip() or None
    status = None
    if status_param == 'paid':
        status = True
    elif status_param == 'unpaid':
        status = False
    bills = hm.get_bills_with_patient(start_date, end_date, status, q)
    return render_template('billingindex.html', bills=bills, status=status_param, start=start_date or '', end=end_date or '', q=q or '')


@app.route('/billing/create', methods=['GET', 'POST'])
def billing_create():
    if request.method == 'POST':
        patient_id = int(request.form['patient_id'])
        amount = request.form['amount']
        billing_date = request.form['billing_date']
        paid_status = request.form.get('paid_status') == 'on'
        if not hm.get_patient(patient_id):
            return redirect('/billing/create')
        hm.create_billing(patient_id, amount, billing_date, paid_status)
        return redirect('/billing')
    patients = hm.get_patients()
    return render_template('billingcreate.html', patients=patients)

@app.route('/billing/edit/<int:id>', methods=['GET', 'POST'])
def billing_edit(id):
    if request.method == 'POST':
        patient_id = int(request.form['patient_id'])
        amount = request.form['amount']
        billing_date = request.form['billing_date']
        paid_status = request.form.get('paid_status') == 'on'
        if not hm.get_patient(patient_id):
            return redirect(f'/billing/edit/{id}')
        hm.update_billing(id, patient_id, amount, billing_date, paid_status)
        return redirect('/billing')
    bill = hm.get_bill(id)
    patients = hm.get_patients()
    return render_template('billingedit.html', bill=bill, patients=patients)

@app.route('/billing/delete/<int:id>')
def billing_delete(id):
    hm.delete_billing(id)
    return redirect('/billing')



@app.route('/patients')
def patients_list():
    page = int(request.args.get('page', 1))
    per_page = 6
    search = request.args.get('search', '')

    patients = hm.search_patients(search)
    total = len(patients)
    start = (page - 1) * per_page
    end = start + per_page
    paginated = patients[start:end]

    total_pages = (total + per_page - 1) // per_page

    return render_template('index.html', patients=paginated, page=page, total_pages=total_pages, search=search)


@app.route('/stats')
def stats():
    total_patients = len(hm.get_patients())
    total_doctors = len(hm.get_doctors())
    total_departments = len(hm.get_departments())
    total_appointments = len(hm.get_appointments())

    return render_template(
        'stats.html',
        total_patients=total_patients,
        total_doctors=total_doctors,
        total_departments=total_departments,
        total_appointments=total_appointments
    )


if __name__ == '__main__':
    app.run(debug=True)


