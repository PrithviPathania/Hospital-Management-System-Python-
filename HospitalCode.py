class Doctor:
    #constructor / initalizer for properties 
    def __init__(self, doctor_id=None, name=None, specialization=None, working_time=None, qualification=None, room_number=None):
        self.__doctor_id = doctor_id
        self.__name = name
        self.__specialization = specialization
        self.__working_time = working_time
        self.__qualification = qualification
        self.__room_number = room_number

    #getters and setters
    @property
    def doctor_id(self):
        return self.__doctor_id

    @doctor_id.setter
    def doctor_id(self, new_id):
        self.__doctor_id = new_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def specialization(self):
        return self.__specialization

    @specialization.setter
    def specialization(self, new_specialization):
        self.__specialization = new_specialization

    @property
    def working_time(self):
        return self.__working_time

    @working_time.setter
    def working_time(self, new_working_time):
        self.__working_time = new_working_time

    @property
    def qualification(self):
        return self.__qualification

    @qualification.setter
    def qualification(self, new_qualification):
        self.__qualification = new_qualification

    @property
    def room_number(self):
        return self.__room_number

    @room_number.setter
    def room_number(self, new_room_number):
        self.__room_number = new_room_number

    #string representation with spacing by underscore
    def __str__(self):
        return f"{self.doctor_id}_{self.name}_{self.specialization}_{self.working_time}_{self.qualification}_{self.room_number}"

class DoctorManager:
    doctor_list = []

    def __init__(self):
        '''
        Purpose: Constructor for DoctorManager class
        Author(s): Kaden
        Date: Dec 10, 2024
        Version: 1v
        '''
        # Initialize an empty doctor list and read data from file
        self.doctor_list = []
        self.read_doctors_file()
    
    @property
    def doctors(self):
        '''
        Purpose: Getter for doctors list
        Returns: List of all doctors
        Author(s): Jace
        Date: Dec 10, 2024
        Version: 1v
        '''
        return self.doctor_list
    
    def format_dr_info(self, doctor):
        '''
        Purpose: Format doctor information for file storage
        Parameters: doctor - A Doctor object to format
        Returns: Formatted string of doctor information
        Author(s): Kaden
        Date: Dec 10, 2024
        Version: 1v
        '''
        # Convert doctor object to string format for file storage
        return str(doctor)
        
    def enter_dr_info(self):
        '''
        Purpose: Get doctor information from user input
        Returns: A new Doctor object with entered information
        Author(s): Kaden
        Date: Dec 16, 2024
        Version: 1v
        '''

        print("Enter new doctor information:")
        # Prompt user for each doctor detail
        doctor_id = input("Enter Doctor ID: ")
        name = input("Enter Doctor Name: ")
        specialization = input("Enter Specialization: ")
        timing = input("Enter Working Hours: ")
        qualification = input("Enter Qualification: ")
        room_nb = input("Enter Room Number: ")

        # Return a new Doctor instance with the entered details
        return Doctor(doctor_id, name, specialization, timing, qualification, room_nb)
    
    def read_doctors_file(self):
        '''
        Purpose: Read doctor information from file
        Author(s): Kevin
        Date: Dec 10 2024
        Version: 1v
        '''
        try: 
            temp_list = [] #list to append each line to
            self.doctor_list = [] #clear the old list of doctors
            with open ('doctors.txt', 'r') as file: #read the file only
                for line in file:
                    temp_list.append(line) #appending the each line of the file to this temp string
                temp_list.pop(0) #pop/remove the first item of the item which is "d_name_specilist_timing_qualification_roomNb"
                for line in temp_list:  #for each line in temp list
                    if len(line) > 3: #ensure that the line contains text and is not empty
                        new_doctor_class = Doctor(*line.strip().split("_")) #each line will be split by underscores, the split elements will be an argument (ex: arg1_arg2 --> arg1, arg2), these arguments will be used to create a new doctor class
                    self.doctor_list.append(new_doctor_class)
            print(self.doctor_list)
        except Exception as e:
            print(f"Error: {e}")
    
    def search_doctor_by_id(self):
        '''
        Purpose: Search for a doctor using their ID
        Returns: Doctor object if found, None otherwise
        Author(s): Kaden
        Date: Dec 12, 2024
        Version: 1v
        '''

        search_id = input("Enter Doctor ID to search: ")
        # Loop through the list to find a doctor with the matching ID

        for doctor in self.doctor_list:
            if doctor.doctor_id == search_id:
                print("\nDoctor found:")
                self.display_doctor_info(doctor) # Displays doctor details
                return doctor
        print("Doctor not found.")
        return None
    
    def search_doctor_by_name(self):
        '''
        Purpose: Search for a doctor using their name
        Returns: Doctor object if found, None otherwise
        Author(s): Kaden
        Date: Dec 16, 2024
        Version: 1v
        '''

        search_name = input("Enter Doctor Name to search: ").lower()
        # Loop through the list to find a doctor with the matching name
        for doctor in self.doctor_list:
            if doctor.name.lower() == search_name:
                print("\nDoctor found:")
                self.display_doctor_info(doctor) # Display doctor details
                return doctor
        print("Doctor not found.")
        return None
    
    def display_doctor_info(self, doctor):
        '''
        Purpose: Display information for a specific doctor
        Parameters: doctor - The Doctor object to display
        Author(s): Kaden
        Date: Dec 17, 2024
        Version: 1v 
        '''
        if doctor:
            # Display each attribute of the doctor
            print(f"Doctor ID: {doctor.doctor_id}")
            print(f"Name: {doctor.name}")
            print(f"Specialization: {doctor.specialization}")
            print(f"Timing: {doctor.working_time}")
            print(f"Qualification: {doctor.qualification}")
            print(f"Room Number: {doctor.room_number}")
        else: 
            print("No doctor information to display.")
    
    def edit_doctor_info(self):
        '''
        Purpose: Edit information for an existing doctor
        Author(s): Kaden
        Date: Dec 17, 2024
        Version: 1v
        ''' 
        doctor = self.search_doctor_by_id() # Search for the doctor by ID
        if doctor:
            print("Editing doctor information (leave blank to keep current value):")
            # Allow user to update doctor attributes while keeping old values if blank
            doctor.name = input(f"Enter new name [{doctor.name}]: ") or doctor.name
            doctor.specialization = input(f"Enter new specialization [{doctor.specialization}]: ") or doctor.specialization
            doctor.working_time = input(f"Enter new timing [{doctor.working_time}]: ") or doctor.working_time
            doctor.qualification = input(f"Enter new qualification [{doctor.qualification}]: ") or doctor.qualification
            doctor.room_number = input(f"Enter new room number [{doctor.room_number}]: ") or doctor.room_number
            print("Doctor information updated successfully.")
        else:
            print("Doctor not found.")
    
    def display_doctors_list(self):
        '''
        Purpose: Display information for all doctors
        Author(s): Jace
        Date: Dec 12, 2023
        Version: 1v
        '''

        if not self.doctor_list:
            print("No doctors available.")
        else:
            print("\nID    Name                   Specialization          Timing          Qualification   Room Number")
            for doctor in self.doctor_list:
                print(f"{doctor.doctor_id:<5} {doctor.name:<22} {doctor.specialization:<23} {doctor.working_time:<15} "
                    f"{doctor.qualification:<15} {doctor.room_number:<10}")
    
    def write_list_of_doctors_to_file(self):
        '''
        Purpose: Write all doctor information to file
        Author(s): Kevin
        Date: Dec 10, 2024
        Version: 1v
        '''
        with open('doctors.txt', 'w') as file: #open the file with write perms
            file.write("d_name_specialist_timing_qualification_roomNb\n") #this was pop in the read function, so we need to add this back
            for doctor in self.doctor_list: #for each doctor class in the doctor list
                file.write(f"{doctor}\n") #on the file write the doctor string.
    
    def add_dr_to_file(self):
        '''
        Purpose: Add a new doctor to the system and file
        Author(s): Jace
        Date: Dec 16, 2024
        Version: 1v
        '''
        new_doctor = self.enter_dr_info() # Get new doctor information
        try:
            self.doctor_list.append(new_doctor) # Append the doctor object to the list
            self.write_list_of_doctors_to_file() # Save the updated list to file
            print("New doctor added sucessfully.")
        except Exception as e:
            print(f"Error adding doctor: {e}")

class Patient: 
    def __init__(self, pid=None, name=None, disease=None, gender=None, age=None):
        '''
        Purpose: Constructor for Patient class
        Parameters: pid, name, disease, gender, age (all optional)
        Author(s): Wamia Ihsan
        Date: 2024/12/12
        Version: 1.0
        '''
        #initialize all private member variables with the passed parameters
        self.__pid = pid
        self.__name = name
        self.__disease = disease
        self.__gender = gender
        self.__age = age

    @property
    def pid(self):
        '''
        Purpose: Getter for patient ID
        Returns: The patient's ID
        Author(s): Wamia Ihsan
        Date: 2024/12/12
        Version: 1.0
        '''
        #return the private pid variable
        return self.__pid

    @pid.setter
    def pid(self, new_pid):
        '''
        Purpose: Setter for patient ID
        Parameters: new_pid - The new ID to set
        Author(s): Wamia Ihsan
        Date: 2024/12/12
        Version: 1.0
        '''
        #set private pid variable to the new value
        self.__pid = new_pid

    @property
    def name(self):
        '''
        Purpose: Getter for name
        Returns: The patient's name
        Author(s): Wamia Ihsan
        Date: 2024/12/12
        Version: 1.0
        '''
        #return the private name variable
        return self.__name

    @name.setter
    def name(self, new_name):
        '''
        Purpose: Setter for name
        Parameters: new_name - The new name to set
        Author(s): Wamia Ihsan
        Date: 2024/12/12
        Version: 1.0
        '''
        #Set the private name variable to the new value
        self.__name = new_name

    @property
    def disease(self):
        '''
        Purpose: Getter for disease
        Returns: The patient's disease
        Author(s): Wamia Ihsan
        Date: 2024/12/16
        Version: 1.0
        '''
        #return the private disease variable
        return self.__disease

    @disease.setter
    def disease(self, new_disease):
        '''
        Purpose: Setter for disease
        Parameters: new_disease - The new disease to set
        Author(s): Wamia Ihsan
        Date: 2024/12/16
        Version: 1.0
        '''
        #set the private disease variable to the new value
        self.__disease = new_disease

    @property
    def gender(self):
        '''
        Purpose: Getter for gender
        Returns: The patient's gender
        Author(s): Wamia Ihsan
        Date: 2024/12/16
        Version: 1.0
        '''
        #return the private gender variable
        return self.__gender

    @gender.setter
    def gender(self, new_gender):
        '''
        Purpose: Setter for gender
        Parameters: new_gender - The new gender to set
        Author(s): Wamia Ihsan
        Date: 2024/12/16
        Version: 1.0
        '''
        #set the private gender variable to the new value
        self.__gender = new_gender

    @property
    def age(self):
        '''
        Purpose: Getter for age
        Returns: The patient's age
        Author(s): Wamia Ihsan
        Date: 2024/12/16
        Version: 1.0
        '''
        #return the private age variable
        return self.__age

    @age.setter
    def age(self, new_age):
        '''
        Purpose: Setter for age
        Parameters: new_age - The new age to set
        Author(s): Wamia Ihsan
        Date: 2024/12/16
        Version: 1.0
        '''
        #set the private age variable to the new value
        self.__age = new_age

    def __str__(self):
        '''
        Purpose: String representation of the Patient object
        Returns: String containing all patient information separated by underscores
        Author(s): Wamia Ihsan
        Date: 2024/12/16
        Version: 1.0
        '''
        #return a string containing all patient properties separated by underscores (_)
        return f"{self.__pid}_{self.__name}_{self.__disease}_{self.__gender}_{self.__age}"

class PatientManagement:
    def __init__(self): 
        '''Dinar'''
        # start with predefined patient data and load data from "patients.txt"
        self.patients = []
        self.filename = "patients.txt"
        self.read_patients_file()

    def format_patient_info_for_file(self, patient): 
        '''Dinar'''
        # Format patient information for saving to a file
        return f"{patient['id']}_{patient['name']}_{patient['disease']}_{patient['gender']}_{patient['age']}"

    def enter_patient_info(self): 
        '''Dinar'''
        # Ask the user to enter new patient details
        patient_id = input("Enter Patient ID: ")
        # Check if the entered ID already exists
        if any(patient["id"] == patient_id for patient in self.patients):
            print("Patient with this ID already exists.")
            return None
        # Collect other details for the new patient
        name = input("Enter Patient Name: ")
        disease = input("Enter Patient Disease: ")
        gender = input("Enter Patient Gender: ")
        age = int(input("Enter Patient Age: "))
        return {"id": patient_id, "name": name, "disease": disease, "gender": gender, "age": age}

    def search_patient_by_id(self): 
        '''Dinar'''
        # Search for a patient using their ID
        patient_id = input("Enter Patient ID: ")
        for patient in self.patients:
            if patient["id"] == patient_id:
                # Display the patient's information
                self.display_patient_info(patient)
                return
        print("Can't find the patient with the provided ID.")

    def display_patient_info(self, patient): 
        '''Gursehaj'''
        # Display the details of a patient
        print(f"ID: {patient['id']}\nName: {patient['name']}\nDisease: {patient['disease']}\nGender: {patient['gender']}\nAge: {patient['age']}")

    def edit_patient_info_by_id(self): 
        '''Gursehaj'''
        # Edit the details of an existing patient by ID
        patient_id = input("Enter Patient ID to Edit: ")
        for patient in self.patients:
            if patient["id"] == patient_id:
                # Allow the user to update fields (leave blank to keep the current value)
                print("Leave fields blank to keep current values.")
                name = input(f"Enter new name (current: {patient['name']}): ") 
                disease = input(f"Enter new disease (current: {patient['disease']}): ") 
                gender = input(f"Enter new gender (current: {patient['gender']}): ") 
                age = input(f"Enter new age (current: {patient['age']}): ")
                age = int(age) if age else patient["age"]
                # Update the patient's information
                patient.update({"name": name or patient["name"], 
                                "disease": disease or patient["disease"], 
                                "gender": gender or patient["gender"], 
                                "age": age})
                print("Patient details updated.")
                return
        # Inform the user if the patient is not found
        print("Can't find the patient with the provided ID.")

    def display_patients_list(self): 
        '''Gursehaj'''
        # Display a list of all patients
        if not self.patients:
            print("No patients available.")
            return
        print("Patient List:")
        for patient in self.patients:
            # Display each patient's details
            print("\nID   Name        Disease        Gender    Age")
            print(f"{patient['id']:<5}{patient['name']:<12}{patient['disease']:<15}{patient['gender']:<10}{patient['age']}")

    def read_patients_file(self):
        '''Gursehaj'''
        # Read patients data from "patients.txt"
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                for line in lines[1:]:  # Skip the header line
                    id, name, disease, gender, age = line.strip().split('_')
                    self.patients.append({
                        "id": id,
                        "name": name,
                        "disease": disease,
                        "gender": gender,
                        "age": int(age)
                    })
            print("Patients data loaded successfully.")
        except FileNotFoundError:
            print(f"File {self.filename} not found.")
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")

    def write_patients_file(self):
        '''Gursehaj'''
        # Write patients data to "patients.txt"
        try:
            with open(self.filename, 'w') as file:
                file.write("id_Name_Disease_Gender_Age\n")
                for patient in self.patients:
                    file.write(self.format_patient_info_for_file(patient) + "\n")
            print("Patients data saved successfully.")
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")
     
    def add_patient_to_file(self): 
        '''Gursehaj'''
        # Add a new patient to the list
        new_patient = self.enter_patient_info()
        if new_patient:
            self.patients.append(new_patient)
            print("New patient added.")
            # Update the file with the new patient
            self.write_patients_file()

class Management():
    def display_menu(self):
        print("\nMain Menu")
        print("1. Doctors")
        print("2. Patients")
        print("3. Exit")
        submenu_choice = int(input("Enter your choice (1-3): "))

        if submenu_choice == 1: #Doctors submenu will be displayed
            self.display_doctors_menu()
        elif submenu_choice == 2: #Patients submenu will be displayed
            self.display_patients_menu()
        elif submenu_choice == 3: #exit the program
            print("Thanks for using the program. Bye!")
        else:
            print("Invalid choice. Please try again.")
            self.display_menu()
 
    def display_doctors_menu(self):
        doctor_manager = DoctorManager()

        print("\nDoctors Menu")
        print("1: Display Doctors list")
        print("2: Search Doctor by Id")
        print("3: Search Doctor by Name")
        print("4: Add a new Doctor")
        print("5: Edit Doctor info")
        print("6: Return to main menu")

        doctors_menu_choice = int(input("Enter your choice 1-6: "))

        #Printing numbers here is just a placeholder for debuging 
        if doctors_menu_choice == 1:
            # Implement display_doctors_list() here after Doctormanager class code is completed
            doctor_manager.display_doctors_list()
            self.display_doctors_menu()
        elif doctors_menu_choice == 2:
            # Implement search_doctor() here after Doctormanager class code is completed
            doctor_manager.search_doctor_by_id()
            self.display_doctors_menu()
        elif doctors_menu_choice == 3:
            # Implement add_doctor() here  after Doctormanager class code is complete
            doctor_manager.search_doctor_by_name()
            self.display_doctors_menu()
        elif doctors_menu_choice == 4:
            # Implement edit_doctor() here after Doctormanager class code is completed
            doctor_manager.add_dr_to_file()
            self.display_doctors_menu()
        elif doctors_menu_choice == 5:
            # Implement delete_doctor() here after Doctormanager class code is completed
            doctor_manager.edit_doctor_info()
            self.display_doctors_menu()
        elif doctors_menu_choice == 6: #Option 6 allows returning to the main menu.
            self.display_menu()
        else:
            print("Invalid choice. Please try again.")
            self.display_doctors_menu()
    
    def display_patients_menu(self):
        patient_manager = PatientManagement()

        print("\nPatients Menu")
        print("1. Display patients list")
        print("2. Search patient by ID")
        print("3. Add a new patient")
        print("4. Edit patient info")
        print("5. Return to main menu")
        patient_menu_choice = int(input("Enter your choice 1-5: "))

        if patient_menu_choice == 1:
            patient_manager.display_patients_list() 
            self.display_patients_menu()
        elif patient_menu_choice == 2:
            patient_manager.search_patient_by_id()
            self.display_patients_menu()
        elif patient_menu_choice == 3:
            patient_manager.add_patient_to_file()
            self.display_patients_menu()
        elif patient_menu_choice == 4:
            patient_manager.edit_patient_info_by_id()
            self.display_patients_menu()
        elif patient_menu_choice == 5: #Option 5 allows returning to the main menu.
            self.display_menu()
        else:
            print("Invalid choice. Please try again.")
    
def main():
    menu = Management()
    menu.display_menu()

if __name__ == "__main__":
    main()