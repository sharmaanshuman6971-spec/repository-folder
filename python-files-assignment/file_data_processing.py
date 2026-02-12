import os

def process_numbers():
    try:
        # Use absolute paths so Python always finds the files
        base_path = r"C:\Users\anshu\Desktop\repository folder\python-files-assignment"
        numbers_file = os.path.join(base_path, "numbers.txt")
        results_file = os.path.join(base_path, "results.log")

        # Step 1: Open and read numbers.txt
        with open(numbers_file, "r") as infile:
            print("File opened successfully")
            lines = infile.readlines()

        # Step 2: Convert lines to integers
        numbers = [int(line.strip()) for line in lines if line.strip()]

        # Step 3: Compute results
        total_count = len(numbers)
        total_sum = sum(numbers)
        average = total_sum / total_count if total_count > 0 else 0

        # Step 4: Write logs to results.log
        with open(results_file, "w") as logfile:
            logfile.write("File opened successfully\n")
            logfile.write(f"Read {total_count} numbers\n")
            logfile.write(f"Sum: {total_sum}\n")
            logfile.write(f"Average: {average}\n")
            logfile.write("Processing completed\n")

        # Step 5: Print confirmation
        print("Logs written to results.log")

    except FileNotFoundError:
        print("Error: numbers.txt not found at", numbers_file)
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
if __name__ == "__main__":
    process_numbers()