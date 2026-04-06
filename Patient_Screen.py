import sqlite3

def connect_db(): #reusable code, teaching it to talk to the database
    conn = sqlite3.connect('CHP.db') #change to fit our medical program
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS patient (
        patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        street_address TEXT,
        state TEXT,
        zip_code TEXT,
        phone INTEGER,
        email TEXT,
        insurance BOOLEAN,
        insurance_name TEXT,
        policy_number TEXT,
        last4_ssn TEXT,
        dob TEXT,
        gender TEXT,
        age TEXT,
        provider_id INTEGER,
        appointment_status TEXT,
        log_status TEXT
    )
''')
    conn.commit()
    return conn

def add_patient(conn): #add patient, copy this for our project!!! with the excel spreadsheet
    patient_id = int(input("Enter Patient ID: "))
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    street_address = input("Enter street address: ")
    state = input("Enter state: ")
    zip_code = int(input("Enter zip code: "))
    phone = int(input("Enter phone number: "))
    email = input("Enter email: ")
    has_insurance_input = input("Do you have insurance? (yes/no): ")
    insurance = has_insurance_input == "yes"
    if insurance:
        insurance_name = input("Enter insurance provider: ")
        policy_number = input("Enter policy number: ")
    else:
        insurance_name = None
        policy_number = None
    
    last4_ssn = input("Enter last 4 digits of SSN: ")
    dob = input("Enter date of birth: ")
    gender = input("Enter gender: ")
    age = input("Enter age: ")
    appointment_status = "Completed"
    log_status = "No visit summary added."

    cur = conn.cursor()
    cur.execute('''
    INSERT INTO patient (patient_id, first_name, last_name, street_address, state,
zip_code, phone, email, insurance, insurance_name, policy_number, last4_ssn, dob,
gender, age, appointment_status, log_status)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    ''', (patient_id, first_name, last_name, street_address, state, zip_code,
phone, email, insurance, insurance_name, policy_number, last4_ssn, dob, gender,
age, appointment_status, log_status))
    conn.commit()
    print("Patient added.")
    
def view_patient(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM patient")
    rows = cur.fetchall()
    for row in rows:
        print(f"Patient ID: {row[0]}")
        print(f"First Name: {row[1]}")
        print(f"Last Name: {row[2]}")
        print(f"Street Address: {row[3]}")
        print(f"State: {row[4]}")
        print(f"Zip Code: {row[5]}")
        print(f"Phone Number: {row[6]}")
        print(f"Email Address: {row[7]}")
        print(f"Insurance Name: {row[9]}")
        print(f"Policy Number: {row[10]}")
        print(f"Last 4 of SSN: {row[11]}")
        print(f"Date of Birth: {row[12]}")
        print(f"Gender: {row[13]}")
        print(f"Age: {row[14]}")
        print(f"Provider ID: {row[15]}")
        print(f"Appointment Status: {row[16]}")
        print(f"Visit Summary: {row[17]}")
        print("-" * 25)
        
def update_appointment_status(conn):
    patient_id = input("Enter patient ID to update: ")
    new_status = input("Enter new status (Completed, Missed, Canceled): ")
    cur = conn.cursor()
    cur.execute("UPDATE patient SET appointment_status = ? WHERE patient_id = ?",
(new_status, patient_id))
    conn.commit()
    print("Appointment status updated.")

def log_appointment(conn):
    patient_id = input("Enter patient ID to update: ")
    log_status = input("Enter patient visit summary: ")
    cur = conn.cursor()
    cur.execute("UPDATE patient SET log_status = ? WHERE patient_id = ?",
(log_status, patient_id))
    conn.commit()
    print("Visit summary updated.")
    
def main():
    conn = connect_db()
    user_choice = ""
    
    while user_choice !="5":
        print("\n--- CHP Patient Database ---")
        print("1. Add New Patient")
        print("2. View All Patients")
        print("3. Update Patient Appointment Status")
        print("4. Log Patient Visit Summary")
        print("5. Exit")
        
        user_choice = input("Enter your choice: ")

        if user_choice =='1':
            add_patient(conn)
        elif user_choice =='2':
            view_patient(conn)
        elif user_choice =='3':
            update_appointment_status(conn)
        elif user_choice =='4':
            log_appointment(conn)
        elif user_choice =='5':
            print("Exiting program.")
        else:
            print("Invalid option. Please try again.")
    conn.close()
main()