import tkinter as tk
from tkinter import messagebox
import cx_Oracle


# Function to submit the form data to the database
def submit():
    # Get the form data
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    arrival_date = arrival_date_entry.get()
    departure_date = departure_date_entry.get()

    # Database connection parameters
    username = 'your_username'
    password = 'your_password'
    host = 'your_host'
    port = 'your_port'
    service_name = 'your_service_name'

    # Create a connection to the Oracle database
    dsn_tns = cx_Oracle.makedsn(host, port, service_name=service_name)
    connection = cx_Oracle.connect(user=username, password=password, dsn=dsn_tns)

    try:
        # Create a cursor
        cursor = connection.cursor()

        # Execute the INSERT statement
        cursor.execute(
            "INSERT INTO hotel_guests (name, email, phone, arrival_date, departure_date) VALUES (:1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'), TO_DATE(:5, 'YYYY-MM-DD'))",
            (name, email, phone, arrival_date, departure_date))

        # Commit the transaction
        connection.commit()

        # Display confirmation message
        messagebox.showinfo("Success", "Check-in successful for {}!".format(name))

    except cx_Oracle.Error as error:
        # Rollback in case of any error
        connection.rollback()
        messagebox.showerror("Error", "Database Error: {}".format(error))

    finally:
        # Close cursor and connection
        cursor.close()
        connection.close()


# Create main window
root = tk.Tk()
root.title("Hotel Check-in")

# Create labels
tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
tk.Label(root, text="Email:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
tk.Label(root, text="Phone:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
tk.Label(root, text="Arrival Date:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
tk.Label(root, text="Departure Date:").grid(row=4, column=0, padx=5, pady=5, sticky="e")

# Create entry fields
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=5, pady=5)
phone_entry = tk.Entry(root)
phone_entry.grid(row=2, column=1, padx=5, pady=5)
arrival_date_entry = tk.Entry(root)
arrival_date_entry.grid(row=3, column=1, padx=5, pady=5)
departure_date_entry = tk.Entry(root)
departure_date_entry.grid(row=4, column=1, padx=5, pady=5)

# Create submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

# Run the application
root.mainloop()
