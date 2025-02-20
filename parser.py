import csv
from datetime import datetime
from classes import Employee, Shift, Break, cartDuty

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

def parseCartDuty(csv_file_path):
    cartDuties = []
    with open(csv_file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            start = datetime.strptime(row['start'], '%H:%M')
            end = datetime.strptime(row['end'], '%H:%M')
            required_people = int(row['required_people'])
            cartDuties.append(CartDuty(start, end, required_people))
    return cartDuties