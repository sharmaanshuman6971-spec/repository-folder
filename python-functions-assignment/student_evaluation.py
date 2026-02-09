# Modular Student Evaluation System

def greet_student(name):
    return "Hello, " + name

def calculate_scores(scores):
    num_subjects = len(scores)
    average = sum(scores) / num_subjects
    return num_subjects, average

def evaluate_result(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"

def main():
    # Example data
    name = "Alice"
    scores = [60, 70, 65]

    # Call functions
    greeting = greet_student(name)
    num_subjects, average = calculate_scores(scores)
    result = evaluate_result(average)

    # Print final output
    print(greeting)
    print("Subjects:", num_subjects)
    print("Average Score:", average)
    print("Result:", result)

# Start program
main()