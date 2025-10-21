# Student Attendance Tracker
# --------------------------------------
# Author: Varad Raj Agrawal
# Description: A simple Python program that records student attendance 
# for a given number of days, skipping specific days (like holidays or absences).
# Ideal for beginners exploring loops, conditionals, and user input handling.

# Take student name as input and remove extra spaces
name = input("Enter the student's name: ").strip()

# Take total working days as input and convert to integer
total_days = int(input("Enter the total number of days: "))

# Initialize day counter
day = 1

# Loop through all the days
while day <= total_days:
    # Example: Skip day 3 (as if the student was absent)
    if day == 3:
        print(f"Day {day} skipped - marked as absent.")
        day += 1
        continue  # Skip recording attendance for this day

    # Record attendance for all other days
    print(f"✅ Attendance recorded for {name} on Day {day}")
    day += 1

# After loop ends
print("\n📘 Attendance tracking completed!")
print(f"Summary: Attendance recorded for {total_days - 1} out of {total_days} days.")
