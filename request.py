import tkinter as tk
from tkinter import ttk
import requests

url = "https://jsonplaceholder.typicode.com/todos"


def get_all_data():
    response = requests.get(url)
    if response.status_code == 200:
        result_text.delete(1.0, tk.END)  # Clear previous result
        result_text.insert(tk.END, response.json())

    else:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error: {response.status_code}")


def get_single_data():
    input_id = id_entry.get()
    request_url = f"https://jsonplaceholder.typicode.com/todos/{input_id}"
    response = requests.get(request_url)
    if response.status_code == 200:
        result_text.delete(1.0, tk.END)  # Clear previous result
        result_text.insert(tk.END, response.json())
    else:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error: {response.status_code}")


def post_data():
    title = title_entry.get()
    completed = bool(completed_var.get())
    data = {
        'title': title,
        'completed': completed
    }
    response = requests.post(url, json=data)
    if response.status_code == 201:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, 'POST request successful')
    else:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"POST request failed with status code {response.status_code}")


def put_data():
    input_id = id_entry.get()
    title = title_entry.get()
    completed = bool(completed_var.get())
    request_url = f"https://jsonplaceholder.typicode.com/todos/{input_id}"
    data = {
        'title': title,
        'completed': completed
    }
    response = requests.put(request_url, json=data)
    if response.status_code == 200:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, 'PUT request successful')
    else:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"PUT request failed with status code {response.status_code}")


def delete_data():
    input_id = id_entry.get()
    request_url = f"https://jsonplaceholder.typicode.com/todos/{input_id}"
    response = requests.delete(request_url)
    if response.status_code == 200:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, 'DELETE request successful')
    else:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"DELETE request failed with status code {response.status_code}")


root = tk.Tk()
root.title("CRUD Operations")

id_label = tk.Label(root, text="Enter ID:")
id_label.grid(row=0, column=0, padx=10, pady=10)

id_entry = tk.Entry(root, width=30)
id_entry.grid(row=0, column=1, padx=10, pady=10)

title_label = tk.Label(root, text="Title:")
title_label.grid(row=1, column=0, padx=10, pady=10)

title_entry = tk.Entry(root, width=30)
title_entry.grid(row=1, column=1, padx=10, pady=10)

completed_label = tk.Label(root, text="Completed:")
completed_label.grid(row=2, column=0, padx=10, pady=10)

completed_var = tk.BooleanVar()
completed_checkbox = ttk.Checkbutton(root, variable=completed_var)
completed_checkbox.grid(row=2, column=1, padx=10, pady=10)

get_all_button = tk.Button(root, text="Get All Data", command=get_all_data)
get_all_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="we")

get_single_button = tk.Button(root, text="Get Data", command=get_single_data)
get_single_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="we")

post_button = tk.Button(root, text="Post Data", command=post_data)
post_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="we")

put_button = tk.Button(root, text="Put Data", command=put_data)
put_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="we")

delete_button = tk.Button(root, text="Delete Data", command=delete_data)
delete_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="we")

result_text = tk.Text(root, height=10, width=50)
result_text.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
