import Billing


class FinancialRecord:
    def __init__(self):
        self.__patient_bill_list = []

    def get_patient_bill_list(self):
        return self.__patient_bill_list

    def add_bill(self, date, amount):
        bill = Billing.Billing(date, amount)
        self.__patient_bill_list.append(bill)
