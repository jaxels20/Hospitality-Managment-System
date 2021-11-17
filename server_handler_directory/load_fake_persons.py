import MedicalEmployee
import Patient
import pickle

patients = [Patient.Patient('1234567890', 'Fede', 'a+', '19/10/2001', 180), \
            Patient.Patient('0987654321', 'Israel', 'b+', '19/11/2001', 160), \
            Patient.Patient('1357908642', 'Wupti', 'c+', '19/7/2001', 190)]

Nurses = [MedicalEmployee.MedicalEmployee('nurse1', 'nurse1', 'nurse1', 'nurse'),
          MedicalEmployee.MedicalEmployee('nurse2', 'nurse2', 'nurse2', 'nurse')]

doctors = [MedicalEmployee.MedicalEmployee('doctor1', 'doctor1', 'doctor1', 'doctor'),
           MedicalEmployee.MedicalEmployee('doctor2', 'doctor2', 'doctor2', 'doctor')]

with open('data\\nurses_data.pkl', 'wb') as outp:
    for nurse in Nurses:
        pickle.dump(nurse, outp, pickle.HIGHEST_PROTOCOL)

with open('data\patients_data.pkl', 'wb') as outp:
    for patient in patients:
        pickle.dump(patient, outp, pickle.HIGHEST_PROTOCOL)

with open('data\doctors_data.pkl', 'wb') as outp:
    for doctor in doctors:
        pickle.dump(doctor, outp, pickle.HIGHEST_PROTOCOL)
