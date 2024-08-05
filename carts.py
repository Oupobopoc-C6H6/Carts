#made by Joseph Groom
from datetime import datetime, timedelta
import csv

class Employee():

    def __init__(self,name,shifts = [],breaks = []):
        self.name = name
        self.shifts = shifts
        self.breaks = breaks
        self.assignedCarts = []
        self.cartDuties = 0

    def available_for_carts(self, cartStart, cartEnd):
        # Ensure the employee has fewer than 4 cart tasks assigned
        if self.cartDuties >= 4:
            return False
        
        # Check if the task conflicts with any shift
        for shift in self.shifts:
            if shift.start <= cartStart < shift.end and shift.start < cartEnd <= shift.end:
                # Check if the task conflicts with any breaks
                for b in self.breaks:
                    if not (cartEnd <= b.start or cartStart >= b.end):
                        return False
                # Check if the task conflicts with already assigned tasks and ensure no consecutive intervals
                for t in self.assigned_get_carts:
                    if not (cartEnd <= t.start or cartStart >= t.end):
                        return False
                    if  (cartStart == t.end or cartEnd == t.start):
                        return False
                return True
        
        return False

    def assignCarts(self, cartDuty):
        # function to assign a cartDuty to an Employee Class adding the duty when called and increasing num duties
        self.assignedCarts.append(cartDuty)
        self.cartDuties += 1

    def __str__(self):
        return "Name: {0}, {1}-{2}, Break(s) {3}".format(self.name,self.shiftStart,self.shiftEnd,self.breaks)

class Shift:
    def __init__(self, start: datetime, end: datetime):
        self.start = start
        self.end = end

class Break:
    def __init__(self, start: datetime, end: datetime):
        self.start = start
        self.end = end

class cartDuty:
    def __init__(self,start: datetime,end: datetime, numPeople: int):
        self.start = start
        self.end = end
        self.numPeople = numPeople

def parseSchedule(csv_path):
    employees = []
    with open(csv_path,mode="r") as file:
        schedule = csv.DictReader(file,delimiter=',')
        for row in schedule:
            name = row['Name']
            shiftStart = datetime.strptime(row["Shift Start"], '%H:%M')
            shiftEnd = datetime.strptime(row["Shift End"], '%H:%M')
            shift = Shift(shiftStart,shiftEnd)
            breaks = []
            # Check for breaks
            breakStr = row['Break']
            if breakStr:
                for brk in breakStr.split(','):
                    break_start, break_end = brk.split('-')
                    breaks.append(Break(datetime.strptime(break_start, '%H:%M'), datetime.strptime(break_end, '%H:%M')))
            # Check if the employee is already there and if this is just a repeat
            if name not in employees:
                employees[name] = Employee(name,shift,breaks)
            else:
                employees[name].shifts.append(shift)
                employees[name].breaks.append(breaks)
    return list(employees.values())

def main():
    schedule_input = "schedule.csv"  # Replace with the actual CSV file path
    cart_duties_input = "cart_duties.csv"  # Replace with the actual tasks CSV file path
    output_file = "assigned_tasks.csv"  # File to write the assignments

    employees = parseSchedule(schedule_input)
    cartDuties = parseCartDuty(cart_duties_input)
    assignments = assign_cart_duties(employees, cartDuties)

    write_assignments_to_csv(assignments, output_file)

if __name__ == "__main__":
    main()