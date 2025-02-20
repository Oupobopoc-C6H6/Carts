from parser import parseSchedule, parseCartDuty
from scheduler import assign_cart_duties
from writer import write_assignments_to_csv

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