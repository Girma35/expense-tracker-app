import pandas as pd
from tkinter import *
from tkinter import messagebox

# Initialize the main window
window = Tk()
window.title("Personal Expense Tracker")
window.config(background="black")
window.geometry("600x800")

# Create a canvas for plotting
canvas = Canvas(window)
canvas.grid(column=0, row=0, columnspan=10, rowspan=10)

# Welcome label
welcome_label = Label(text="Welcome To Expense Tracker App", fg="red", font=("Helvetica", 16), bg="black", padx=50, pady=50)
welcome_label.grid(column=0, row=0, columnspan=2)

# Daily budget data
data = {
    "day": ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"],
    "value": [25, 30, 20, 25, 35, 40, 30]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Saving DataFrame to CSV
df.to_csv("budget.csv", index=False)

# Entry for day
day_entry = Entry(window)
day_entry.grid(column=1, row=1, padx=10, pady=10)

def daily_budget():
    day = day_entry.get().lower()
    if day in df['day'].values:
        budget = df.loc[df['day'] == day, 'value'].values[0]
        budget_label.config(text=f"Daily budget for {day.capitalize()}: ${budget}")
    else:
        messagebox.showerror("Error", "Invalid day entered. Please enter a valid day of the week.")

budget_button = Button(text="Click To Know Today's Budget", activebackground="green", font=("Helvetica", 10), command=daily_budget)
budget_button.grid(column=0, row=1, padx=10, pady=10)

# Budget label to display the daily budget
budget_label = Label(window, text="", font=("Helvetica", 10), bg="black", fg="white")
budget_label.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

# Expense amount label and entry
amount_label = Label(text="Please enter the expense amount", font=("Helvetica", 10), bg="black", fg="white")
amount_label.grid(column=0, row=3, padx=10, pady=10)
amount_entry = Entry(window)
amount_entry.grid(column=1, row=3, padx=10, pady=10)

# Expense category label and entry
category_label = Label(text="Please enter the expense category", font=("Helvetica", 10), bg="black", fg="white")
category_label.grid(column=0, row=4, padx=10, pady=10)
category_entry = Entry(window)
category_entry.grid(column=1, row=4, padx=10, pady=10)

# Save expense function
def save_expense():
    amount = amount_entry.get()
    category = category_entry.get()
    if amount and category:
        try:
            data = {"Amount": [float(amount)], "Category": [category]}
            df_expense = pd.DataFrame(data)
            df_expense.to_csv("expense.csv", mode='a', header=not pd.io.common.file_exists("expense.csv"), index=False)

            messagebox.showinfo("Success", "Expense saved successfully")
            amount_entry.delete(0, END)
            category_entry.delete(0, END)
        except ValueError:
            messagebox.showerror("Error", "Invalid amount entered. Please enter a numeric value.")
    else:
        messagebox.showerror("Error", "Please fill in both fields.")

save_button = Button(text="Click to Save", activebackground='red', font=("Helvetica", 10), command=save_expense)
save_button.grid(column=0, row=5, columnspan=2, padx=10, pady=10)

# Start the main loop
window.mainloop()
