import server_handler_directory.Billing as Billing
from datetime import date


class FinancialRecord:
    def __init__(self):
        self.__patient_bill_list = []

    def get_patient_bill_list(self):
        return self.__patient_bill_list

    def add_bill(self, date, amount):
        bill = Billing.Billing(date, amount)
        self.__patient_bill_list.append(bill)

    def generate_bill(self, patient_obj):
        sum = 0
        for medicine in patient_obj.get_medical_record().get_patient_medical_list():
            if medicine.get_added_to_bill() is False:
                medicine.mark_as_billed()
                sum += medicine.get_price()
        if sum != 0:
            bill = Billing.Billing(date.today(), sum)
            self.__patient_bill_list.append(bill)
