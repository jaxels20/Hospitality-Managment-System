import server_handler_directory.Billing as Billing
from datetime import date


class FinancialRecord:
    """The class which represents the financial record of a patient
    """    
    def __init__(self):
        """Constructs all the necessary attributes for the financial record object.
        """        
        self.__patient_bill_list = []

    def get_patient_bill_list(self):
        """Retrieve all the bills in a specific financial record.

        Returns:
            list: A list that contains all the bills in a financial record.
        """        
        return self.__patient_bill_list

    def generate_bill(self, patient_obj):
        """Generate a bill for the all medicine in a medical record not yet billed.

        Args:
            patient_obj (Patient): The patient where you would like to add the bill.
        """        
        sum = 0
        for medicine in patient_obj.get_medical_record().get_patient_medical_list():
            if medicine.get_added_to_bill() is False:
                medicine.mark_as_billed()
                sum += medicine.get_price()
        if sum != 0:
            bill = Billing.Billing(str(date.today()), sum)
            self.__patient_bill_list.append(bill)
