from part import Part
# Program Name: Inventory System - Supplier Class
# Description: A Python class that represents a supplier and their associated parts
# Author: [Your Name]
# Date: [Date]


class Supplier:
    def __init__(self, name):
        self.name = name
        self.parts = []

    def add_part(self, name, cost):
        part = Part(name, cost)
        self.parts.append(part)

    def get_price(self, part_name):
        for part in self.parts:
            if part.name == part_name:
                return part.cost
        return None

    def part_exists(self, part_name):
        for part in self.parts:
            if part.name == part_name:
                return True
        return False
