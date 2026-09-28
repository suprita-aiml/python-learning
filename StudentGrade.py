print("🎓 Student Grade Calculator")

# Number of subjects
n = int(input("Enter number of subjects: "))

marks = []

# Take marks for each subject
for i in range(n):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

# Calculate total and percentage
total = sum(marks)
percentage = total / n

# Custom grading system
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# Display result
print("\n----- Student Result -----")
print("Marks:", marks)
print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)