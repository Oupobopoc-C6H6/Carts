from classes import Employee, cartDuty

def assign_cart_duties(employees, cartDuties):
    assignments = {task: [] for task in cartDuties}
    
    for task in cartDuties:
        available_employees = [e for e in employees if e.available_for_carts(task.start, task.end)]
        
        if len(available_employees) >= task.required_people:
            selected_employees = available_employees[:task.required_people]
            for emp in selected_employees:
                emp.assignCarts(task)
                assignments[task].append(emp.name)
        else:
            print(f"Not enough employees available for cart duty from {task.start} to {task.end}")
    
    return assignments
