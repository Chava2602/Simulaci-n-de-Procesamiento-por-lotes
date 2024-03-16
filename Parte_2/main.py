import tkinter as tk
from datetime import datetime
import random
import math
import time

elapsed_seconds = 0
start_time = None
pending_processes = []
current_process = None
finished_processes = []
current_process_number = 1
number_process_batch = 0

programmers = ["Jose", "Carlos", "Carolina", "Juan"]
operations = ["+", "-", "*", "/"]

class Process:
    process_counter = 1

    def __init__(self, name, data, max_time, operation, original_position):
        self.process_number = Process.process_counter
        Process.process_counter += 1
        self.name = name
        self.data = data
        self.max_time = int(max_time)
        self.operation = operation
        self.result = None
        self.original_position = original_position

    def __str__(self):
        return f"{self.process_number}. {self.name}\n{self.data}\nTME: {self.max_time}\n"

def generate_data_process():
    name = random.choice(programmers)
    max_time = random.randint(6, 12)
    return name, max_time

def generate_operation_process():
    operation = random.choice(operations)
    num_A = random.randint(0, 10)
    num_B = random.randint(0, 10)
    if operation == "/" and num_B == 0:
        num_B = random.randint(1, 10)
    data = f"{str(num_A)} {operation} {str(num_B)}"
    result = eval(data)
    return operation, data, result

def generate_process_txt(processes):
    with open("data.txt", "w") as file:
        current_batch = 1
        for i, process in enumerate(processes, start=1):
            if i % 5 == 1:
                file.write(f"Batch {current_batch}\n")
                current_batch += 1
            file.write(f"{i}. {process}\n")
            file.write("\n")
        file.write("\n")

def clear_text_boxes():
    text_box_running.delete("1.0", tk.END)
    text_box_on_hold.delete("1.0", tk.END)
    text_box_finished.delete("1.0", tk.END)

def update_GUI_process_lbl_txt_box():
    update_running_process_text_box()
    update_on_hold_process_text_box()
    update_finished_process_text_box()
    update_pending_batches_label()
    lbl_global_clock.after(1000, update_elapsed_time)

def update_running_process_text_box():
    text_box_running.delete("1.0", tk.END)
    if current_process:
        text_box_running.insert("1.0", f"{current_process}\n")

def update_on_hold_process_text_box():
    text_box_on_hold.delete("1.0", tk.END)
    if pending_processes:
        next_process = pending_processes[0]
        text_box_on_hold.insert(tk.END, f"{next_process}\n")
        current_batch = calculate_current_batch_number(current_process_number)
        current_batch_processes = calculate_current_batch_processes()
        text_box_on_hold.insert(tk.END, f"Pending processes: {current_batch_processes}")

def update_finished_process_text_box():
    text_box_finished.delete("1.0", tk.END)
    global finished_processes
    text_box_finished.delete("1.0", tk.END)
    for i, process in enumerate(finished_processes, start=1):
        result = process.result
        if result == "Error: Process interrupted":
            text_box_finished.insert(tk.END, f"{process.process_number}. {process.name}\n{result}\n\n")
        else:
            text_box_finished.insert(tk.END, f"{process.process_number}. {process.name}\n{process.data} = {result}\n\n")

def update_pending_batches_label():
    T_batches = calculate_number_of_batches()
    current_batch = calculate_current_batch_number(current_process_number)
    n_batches = T_batches - current_batch

    if n_batches == 0:
        text = "Number of pending batches: 0"
    else:
        text = f"Number of pending batches: {n_batches}"

    lbl_pending_batches.config(text=text)

def calculate_current_batch_number(current_process_number):
    while True:
        current_batch = math.ceil(current_process_number / 5)
        return current_batch

def calculate_current_batch_processes():
    number_batches = calculate_number_of_batches()
    n_processes = int(entry_num_processes.get())
    current_batch = calculate_current_batch_number(current_process_number)
    complement_number_process_batch = last_number_process_batch()
    
    if n_processes % 5 == 0:
        current_batch_processes = ((current_process_number - (current_batch * 5)) * -1)

        return current_batch_processes
    
    elif n_processes % 5 != 0 :
        current_batch_processes = ((current_process_number - (current_batch * 5)) * -1) 
        
        if current_batch == number_batches:
            current_batch_processes = ((current_process_number - (current_batch * 5)) * -1)  - (complement_number_process_batch)
        
        return current_batch_processes

    
def last_number_process_batch():
    while True:
        n_processes = int(entry_num_processes.get())
        n_batches = calculate_number_of_batches()
        
        number_process_batch = (((((((n_processes - (n_batches * 5)) * -1 )- 5) * -1) - 5)* -1))
        return number_process_batch

def calculate_number_of_batches():
    number_batches = 0
    n_processes = int(entry_num_processes.get())
    number_batches = math.ceil(n_processes / 5)
    return number_batches

def start_clock():
    global start_time, elapsed_seconds
    start_time = datetime.now()
    elapsed_seconds = 0
    update_elapsed_time()

def update_elapsed_time():
    global elapsed_seconds, start_time
    if start_time:
        elapsed_time = datetime.now() - start_time
        elapsed_seconds = elapsed_time.seconds
    else:
        elapsed_seconds = 0
    lbl_global_clock.config(text=f"Global Clock: {elapsed_seconds} seconds")
    lbl_global_clock.after(1000, update_elapsed_time)

def running_process():
    global pending_processes, current_process, finished_processes, current_process_number
    if not current_process and pending_processes:
        current_process = pending_processes.pop(0)
        current_process_number = len(finished_processes)+1
    if current_process:
        if current_process.max_time > 0:
            current_process.max_time -= 1
        else:
            finished_processes.append(current_process)
            current_process = None
    update_GUI_process_lbl_txt_box()
    lbl_global_clock.after(1000, running_process)
    
def error_process():
    global current_process
    if current_process:
        current_process.result = "Error: Process interrupted"
        finished_processes.append(current_process)
        current_process = None
    update_GUI_process_lbl_txt_box()

def break_process():
    global current_process, pending_processes
    if current_process:
        n_process = calculate_current_batch_processes()
        current_process.original_position = n_process
        pending_processes.insert(n_process, current_process)
        current_process = None
    update_GUI_process_lbl_txt_box()

def generate_process():
    global pending_processes, finished_processes
    n_processes = int(entry_num_processes.get())
    pending_processes = []
    finished_processes = []
    Process.process_counter = 1
    for i in range(n_processes):
        name, max_time = generate_data_process()
        operation, data, result = generate_operation_process()
        original_position = i + 1
        p = Process(name, data, max_time, operation, original_position)
        p.result = result
        pending_processes.append(p)
    clear_text_boxes()
    generate_process_txt(pending_processes)
    update_GUI_process_lbl_txt_box()
    start_clock()
    lbl_global_clock.after(1000, running_process)

def generate_result_txt():
    global finished_processes
    if finished_processes:
        with open("results.txt", "w") as file:
            current_batch = 1
            for i, process in enumerate(finished_processes, start=1):
                if i % 5 == 1 and i != 1:
                    file.write("\n")
                if i % 5 == 1:
                    file.write(f"Batch {current_batch}\n")
                    current_batch += 1
                file.write(f"{process.process_number}. {process.name}\n{process.data} = {process.result}\n")
                file.write("\n")
            file.write("\n")

def create_main_window():
    global entry_num_processes, text_box_running, text_box_on_hold, lbl_pending_batches, lbl_finished, lbl_global_clock, text_box_finished
    window = tk.Tk()
    window.title("Batch Processing")
    window.geometry("700x400")

    lbl_processes_n = tk.Label(window, text="Number of\nprocesses")
    lbl_processes_n.place(x=15, y=10)
    entry_num_processes = tk.Entry(window)
    entry_num_processes.place(x=90, y=20)

    btn_generate = tk.Button(window, text="Generate", command=generate_process)
    btn_generate.place(x=230, y=15)

    lbl_global_clock = tk.Label(window, text="Global Clock: 0 seconds")
    lbl_global_clock.place(x=520, y=15)

    lbl_on_hold = tk.Label(window, text="On hold")
    lbl_on_hold.place(x=80, y=70)
    text_box_on_hold = tk.Text(window, width=20, height=15)
    text_box_on_hold.place(x=20, y=90)

    lbl_running = tk.Label(window, text="Running process")
    lbl_running.place(x=300, y=130)
    text_box_running = tk.Text(window, width=20, height=8)
    text_box_running.place(x=270, y=150)

    lbl_finished = tk.Label(window, text="Finished")
    lbl_finished.place(x=550, y=70)
    text_box_finished = tk.Text(window, width=20, height=15)
    text_box_finished.place(x=500, y=90)

    lbl_pending_batches = tk.Label(window, text="Number of\n pending batches")
    lbl_pending_batches.place(x=20, y=340)

    btn_get_result = tk.Button(window, text="Get result", command=generate_result_txt)
    btn_get_result.place(x=550, y=340)
    
    btn_error = tk.Button(window, text="Error", command=error_process)
    btn_error.place(x=275, y=290)
    
    btn_break = tk.Button(window, text="Break", command=break_process)
    btn_break.place(x=385, y=290)

    window.mainloop()

if __name__ == "__main__":
    create_main_window()