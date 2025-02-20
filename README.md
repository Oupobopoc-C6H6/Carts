# **Automated Shift-Based Task Scheduler**

## **Overview**  
This Python-based scheduling tool automates the assignment of employees to a recurring task—retrieving carts—while ensuring fairness and compliance with individual shift constraints. It reads employee shift schedules and task requirements from CSV files, then generates an optimized schedule that balances workload and prevents consecutive assignments.

## **Features**  
- **Flexible Shift and Break Handling:** Employees can have multiple shifts and breaks, ensuring compliance with real-world scheduling constraints.  
- **Task Scheduling with Fair Distribution:** Assigns employees to cart duty no more than four times per shift, preventing overload.  
- **CSV-Based Input and Output:** Reads employee schedules and task requirements from CSV files and outputs an optimized schedule.  
- **Consecutive Task Prevention:** Ensures no employee is scheduled for back-to-back cart duties.  
- **Modular Codebase:** Organized with separate class and function definitions for maintainability and scalability.  

## **Usage**  
1. Prepare CSV files containing employee shift schedules and cart duty time slots.  
2. Run the program to generate an optimized schedule.  
3. Review the output CSV file to see the assigned tasks.  

