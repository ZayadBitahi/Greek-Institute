from flask import Flask, render_template, request, redirect
import models.hospitalmodel as hm

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)



@app.route('/doctor')
def doctor_list():
    doctors = hm.get_doctors()
    return render_template('doctorindex.html', doctors=doctors)

@app.route('/doctor/create', methods=['GET', 'POST'])
def doctor_create():
    if request.method == 'POST':
        hm.create_doctor(
            request.form['first_name'],
            request.form['last_name'],
            request.form['specialty'],
            request.form['email'],
            request.form['department_id']
        )
        return redirect('/doctor')
    return render_template('doctorcreate.html')

@app.route('/doctor/edit/<int:id>', methods=['GET', 'POST'])
def doctor_edit(id):
    doctor = hm.get_doctor(id)
    if request.method == 'POST':
        hm.update_doctor(
            id,
            request.form['first_name'],
            request.form['last_name'],
            request.form['specialty'],
            request.form['email'],
            request.form['department_id']
        )
        return redirect('/doctor')
    return render_template('doctoredit.html', doctor=doctor)

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
        hm.create_department(
            request.form['name'],
            request.form['location']
        )
        return redirect('/department')
    return render_template('departmentcreate.html')

@app.route('/department/edit/<int:id>', methods=['GET', 'POST'])
def department_edit(id):
    department = hm.get_department(id)
    if request.method == 'POST':
        hm.update_department(
            id,
            request.form['name'],
            request.form['location']
        )
        return redirect('/department')
    return render_template('departmentedit.html', department=department)

@app.route('/department/delete/<int:id>')
def department_delete(id):
    hm.delete_department(id)
    return redirect('/department')


@app.route('/appointment')
def appointment_list():
    appointments = hm.get_appointments()
    return render_template('appointmentindex.html', appointments=appointments)

@app.route('/appointment/create', methods=['GET', 'POST'])
def appointment_create():
    if request.method == 'POST':
        hm.create_appointment(
            request.form['patient_id'],
            request.form['doctor_id'],
            request.form['appointment_date'],
            request.form['reason']
        )
        return redirect('/appointment')
    return render_template('appointmentcreate.html')

@app.route('/appointment/edit/<int:id>', methods=['GET', 'POST'])
def appointment_edit(id):
    appointment = hm.get_appointment(id)
    if request.method == 'POST':
        hm.update_appointment(
            id,
            request.form['patient_id'],
            request.form['doctor_id'],
            request.form['appointment_date'],
            request.form['reason']
        )
        return redirect('/appointment')
    return render_template('appointmentedit.html', appointment=appointment)

@app.route('/appointment/delete/<int:id>')
def appointment_delete(id):
    hm.delete_appointment(id)
    return redirect('/appointment')


@app.route('/billing')
def billing_list():
    bills = hm.get_billing()
    return render_template('billingindex.html', bills=bills)

@app.route('/billing/create', methods=['GET', 'POST'])
def billing_create():
    if request.method == 'POST':
        hm.create_billing(
            request.form['patient_id'],
            request.form['amount'],
            request.form['billing_date'],
            request.form.get('paid_status') == 'on'
        )
        return redirect('/billing')
    return render_template('billingcreate.html')

@app.route('/billing/edit/<int:id>', methods=['GET', 'POST'])
def billing_edit(id):
    bill = hm.get_bill(id)
    if request.method == 'POST':
        hm.update_billing(
            id,
            request.form['patient_id'],
            request.form['amount'],
            request.form['billing_date'],
            request.form.get('paid_status') == 'on'
        )
        return redirect('/billing')
    return render_template('billingedit.html', bill=bill)

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





