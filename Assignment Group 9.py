class Doctor:
    def __init__(self, id, name, specialization, timings, qualification, room_number):
        self.id = id
        self.name = name
        self.specialization = specialization
        self.timings = timings
        self.qualification = qualification
        self.room_number = room_number

    def display_info(self):
        print(f"Doctor ID: {self.id}")
        print(f"Doctor Name: {self.name}")
        print(f"Specialization: {self.specialization}")
        print(f"timings: {self.timings}")
        print(f"qualification: {self.qualification}")
        print(f"room_number: {self.room_number}")

class Facility:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Facility: {self.name}")


class Laboratory:
    def __init__(self, name, cost):
        self.name = name
        self.name = cost

    def display_info(self):
        print(f"Laboratory: {self.name}")
        print(f"laboratoty: {self.cost}")


class Patient:
    def __init__(self, id, name, disease, gender, age):
        self.id = id
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def display_info(self):
        print(f"Patient ID: {self.id}")
        print(f"Patient Name: {self.name}")
        print(f"patient disease: {self.disease}")
        print(f"patient gender: {self.gender}")
        print(f"Age: {self.age}")


class HospitalApp:
    def __init__(self):
        self.doctors = []
        self.facilities = []
        self.laboratories = []
        self.patients = []
        self.current_menu = self.main_menu

    def main_menu(self):
        print("Main Menu:")
        print("1. Doctors")
        print("2. Facilities")
        print("3. Laboratories")
        print("4. Patients")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            self.current_menu = self.doctors_menu
        elif choice == '2':
            self.current_menu = self.facilities_menu
        elif choice == '3':
            self.current_menu = self.laboratories_menu
        elif choice == '4':
            self.current_menu = self.patients_menu
        elif choice == '0':
            exit()
        else:
            print("Invalid choice. Please try again.")

    def doctors_menu(self):
        print("Doctors Menu:")
        print("1. Display Doctors List")
        print("2. Search for Doctor by ID")
        print("3. Search for Doctor by Name")
        print("4. Add Doctor")
        print("5. Edit Doctor Info")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            self.display_doctors()
        elif choice == '2':
            self.search_doctor_by_id()
        elif choice == '3':
            self.search_doctor_by_name()
        elif choice == '4':
            self.add_doctor()
        elif choice == '5':
            self.edit_doctor_info()
        elif choice == '6':
            self.current_menu = self.main_menu
        else:
            print("Invalid choice. Please try again.")

    def facilities_menu(self):
        print("Facilities Menu:")
        print("1. Display Facilities List")
        print("2. Add Facility")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            self.display_facilities()
        elif choice == '2':
            self.add_facility()
        elif choice == '3':
            self.current_menu = self.main_menu
        else:
            print("Invalid choice. Please try again.")

    def laboratories_menu(self):
        print("Laboratories Menu:")
        print("1. Display Laboratories List")
        print("2. Add Laboratory")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            self.display_laboratories()
        elif choice == '2':
            self.add_laboratory()
        elif choice == '3':
            self.current_menu = self.main_menu
        else:
            print("Invalid choice. Please try again.")

    def patients_menu(self):
        print("Patients Menu:")
        print("1. Display Patients List")
        print("2. Search for Patient by ID")
        print("3. Add Patient")
        print("4. Edit Patient Info")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            self.display_patient()
        elif choice == '2':
            self.search_patient_by_id()
        elif choice == '3':
            self.add_patient()
        elif choice == '4':
            self.edit_patient_info()
        elif choice == '5':
            self.current_menu = self.main_menu
        else:
            print("Invalid choice. Please try again.")

    def display_doctors(self):
        print("Doctors List:")
        for doctor in self.doctors:
            doctor.display_info()
            print("-------------------------")

    def search_doctor_by_id(self):
        doctor_id = input("Enter Doctor ID: ")
        found = False
        for doctor in self.doctors:
            if doctor.id == doctor_id:
                doctor.display_info()
                found = True
                break
        if not found:
            print("Doctor not found.")

    def search_doctor_by_name(self):
        doctor_name = input("Enter Doctor Name: ")
        found = False
        for doctor in self.doctors:
            if doctor.name.lower() == doctor_name.lower():
                doctor.display_info()
                found = True
                break
        if not found:
            print("Doctor not found.")

    def add_doctor(self):
        id = input("Enter Doctor ID: ")
        name = input("Enter Doctor Name: ")
        specialization = input("Enter Doctor Specialization: ")
        timing = input("Enter Doctor timing: ")
        qualification = input("enter Doctor qualification: ")
        room_number = input("enter Doctor room number: ")
        doctor = Doctor(id, name, specialization, timing, qualification, room_number)
        self.doctors.append(doctor)
        print("Doctor added successfully.")

    def edit_doctor_info(self):
        doctor_id = input("Enter Doctor ID to edit: ")
        found = False
        for doctor in self.doctors:
            if doctor.id == doctor_id:
                print("Current Doctor Info:")
                doctor.display_info()
                print("Enter new information:")
                name = input("Enter new Doctor Name: ")
                specialization = input("Enter new Doctor Specialization: ")
                timing = input("Enter new Doctor timing: ")
                qualification =input("enter the Doctor qualification: ")
                room_number = input("enter Doctor room number: ")
                doctor.name = name
                doctor.specialization = specialization
                doctor.experience = timing
                doctor.qualification = qualification
                doctor.room_number =room_number
                print("Doctor information updated successfully.")
                found = True
                break
        if not found:
            print("Doctor not found.")

    def display_facilities(self):
        print("Facilities List:")
        for facility in self.facilities:
            facility.display_info()
            print("-------------------------")

    def add_facility(self):
        name = input("Enter Facility Name: ")
        facility = Facility(name)
        self.facilities.append(facility)
        print("Facility added successfully.")

    def display_laboratories(self):
        print("Laboratories List:")
        for laboratory in self.laboratories:
            laboratory.display_info()
            print("-------------------------")

    def add_laboratory(self):
        name = input("Enter Laboratory Name: ")
        cost = input("enter laboratory cost: ")
        laboratory = Laboratory (name, cost)
        self.laboratories.append(laboratory)
        print("Laboratory added successfully.")

    def display_patient(self):
        print("patients List:")
        for patient in self.patients:
            patient.dislay_info()
        print("-------------------------")

    def search_patient_by_id(self):
        patient_id = input("Enter Patient ID: ")
        found = False
        for patient in self.patients:
            if patient.id == patient_id:
                patient.display_info()
                found = True
                break
        if not found:
            print("Patient not found.")

    def add_patient(self):
        id = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        disease = input("Enter disease: ")
        gender = input("Enter Patient gender: ")
        age = input("Enter Patient Age: ")
        patient = Patient(id, name, age, disease, gender )
        self.patients.append(patient)
        print("Patient added successfully.")

    def edit_patient_info(self):
        patient_id = input("Enter Patient ID to edit: ")
        found = False
        for patient in self.patients:
            if patient.id == patient_id:
                print("Current Patient Info:")
                patient.display_info()
                print("Enter new information:")
                name = input("Enter new Patient Name: ")
                disease = input("Enter New Patient disease: ")
                gender = input("Enter New Patient gender: ")
                age = input("Enter new Patient Age: ")
                patient.name = name
                patient.age = age
                patient.disease = disease
                patient.gender = gender
                print("Patient information updated successfully.")
                found = True
                break
        if not found:
            print("Patient not found.")

    def run(self):
        while True:
            self.current_menu()


if __name__ == "__main__":
    app = HospitalApp()
    app.run()
