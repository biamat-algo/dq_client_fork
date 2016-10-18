# -*- coding: utf-8 -*-


class Account:

    def __init__(self, email, balance, total_records):
        self.email = email
        self.balance = balance,
        self.total_records = total_records

    def __repr__(self):
        return str(vars(self))
