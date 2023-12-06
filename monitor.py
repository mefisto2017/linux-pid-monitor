import psutil
import time

# Especifica el archivo para guardar los PIDs
pid_file = "/home/username/pids.txt"
previous_processes = []

# Function to list and save the new processes with username, process name, and PID
def list_and_save_processes():
    # Get the current processes with username, process name, and PID
    current_processes = [(process.info['username'], process.info['name'], process.pid) for process in psutil.process_iter(['pid', 'name', 'username'])]

    # Find and save the new processes in the file
    with open(pid_file, 'a') as file:
        for process in current_processes:
            if process not in previous_processes:
                file.write(f"{process[0]} {process[1]} {process[2]}\n")
                previous_processes.append(process)

    #print(f"New processes appended to {pid_file}")

# Run the script continuously with an initial delay
time.sleep(5)  # Initial delay of 5 seconds
while True:
    list_and_save_processes()
    # Adjust the sleep duration
    time.sleep(0.1)

