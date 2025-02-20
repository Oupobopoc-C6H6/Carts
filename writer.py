import csv

def write_assignments_to_csv(assignments, csv_file_path):
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['start', 'end', 'required_people', 'assigned_employees'])
        for task, assigned in assignments.items():
            writer.writerow([task.start.strftime('%H:%M'), task.end.strftime('%H:%M'), task.required_people, ','.join(assigned)])
