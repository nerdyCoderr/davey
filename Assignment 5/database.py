# Program Name: Inventory System - Database Class
# Description: A Python class that stores suppliers and their associated parts
# Author: [Your Name]
# Date: [Date]

class Database:
    def __init__(self):
        self.suppliers = []

    def add_supplier(self, supplier):
        self.suppliers.append(supplier)

    def find_part(self, part_name):
        lowest_price = float('inf')
        lowest_supplier = None

        for supplier in self.suppliers:
            price = supplier.get_price(part_name)
            if price is not None and price < lowest_price:
                lowest_price = price
                lowest_supplier = supplier.name

        if lowest_supplier is None:
            return False, None
        else:
            return lowest_supplier, lowest_price
