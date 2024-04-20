import os
import tkinter as tk
from tkinter import ttk

def add_expense():
    date = date_entry.get()
    category = category_entry.get()
    amount = amount_entry.get()

    if date and category and amount:
        with open("expenses.txt", "a") as file:
            file.write(f"{date},{category},{amount}\n")
        status_label.config(text="Expense added successfully!", fg="green")
        date_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
        view_expenses()
    else:
        status_label.config(text="Please fill all the fields!", fg="red")

def view_expenses():
    global expenses_tree
    if os.path.exists("expenses.txt"):
        expenses_tree.delete(*expenses_tree.get_children())
        with open("expenses.txt", "r") as file:
            for line in file:
                date, category, amount = line.strip().split(",")
                expenses_tree.insert("", tk.END, values=(date, category, amount))
    else:
        expenses_tree.delete(*expenses_tree.get_children())
        status_label.config(text="No expenses recorded.", fg="red")

def summary():
    total_expense = 0
    category_expense = {}

    if os.path.exists("expenses.txt"):
        with open("expenses.txt", "r") as file:
            for line in file:
                _, category, amount = line.strip().split(",")
                total_expense += float(amount)
                if category in category_expense:
                    category_expense[category] += float(amount)
                else:
                    category_expense[category] = float(amount)

    summary_text = f"Total Expense: ${total_expense:.2f}\n\nCategory-wise Expense:\n"
    for category, expense in category_expense.items():
        summary_text += f"{category}: ${expense:.2f}\n"

    summary_label.config(text=summary_text)

# Create the main application window
root = tk.Tk()
root.title("Expense Tracker")

# Set background color
root.configure(bg="#ADD8E6")

# Create labels and entries for adding expenses
date_label = tk.Label(root, text="Date (YYYY-MM-DD):", bg="#ADD8E6")
date_label.grid(row=0, column=0, padx=5, pady=5)
date_entry = tk.Entry(root, bg="#ADD8E6")
date_entry.grid(row=0, column=1, padx=5, pady=5)

category_label = tk.Label(root, text="Category:", bg="#ADD8E6")
category_label.grid(row=1, column=0, padx=5, pady=5)
category_entry = tk.Entry(root, bg="#ADD8E6")
category_entry.grid(row=1, column=1, padx=5, pady=5)

amount_label = tk.Label(root, text="Amount:", bg="#ADD8E6")
amount_label.grid(row=2, column=0, padx=5, pady=5)
amount_entry = tk.Entry(root, bg="#ADD8E6")
amount_entry.grid(row=2, column=1, padx=5, pady=5)

add_button = tk.Button(root, text="Add Expense", command=add_expense, bg="green", fg="white")
add_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

# Create a treeview to display expenses
columns = ("Date", "Category", "Amount")
expenses_tree = ttk.Treeview(root, columns=columns, show="headings")
expenses_tree.heading("Date", text="Date")
expenses_tree.heading("Category", text="Category")
expenses_tree.heading("Amount", text="Amount")
expenses_tree.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Create a label to show the status of expense addition
status_label = tk.Label(root, text="", fg="green", bg="#ADD8E6")
status_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Create a button to view expenses
view_button = tk.Button(root, text="View Expenses", command=view_expenses, bg="aqua")
view_button.grid(row=6, column=0, columnspan=2, padx=5, pady=10)

# Create a button to view summary
summary_button = tk.Button(root, text="Summary", command=summary, bg="red", fg="white")
summary_button.grid(row=7, column=0, columnspan=2, padx=5, pady=10)

# Create a label to show the summary
summary_label = tk.Label(root, text="", justify="left", bg="#ADD8E6")
summary_label.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()