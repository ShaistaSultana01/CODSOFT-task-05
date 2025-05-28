import tkinter as tk
from tkinter import messagebox, simpledialog

contacts = []

name_var = None
phone_var = None
email_var = None
address_var = None
contact_listbox = None

def add_contact():
    name = name_var.get()
    phone = phone_var.get()
    email = email_var.get()
    address = address_var.get()

    if name and phone:
        new_contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }
        contacts.append(new_contact)
        clear_fields()
        view_contacts()
    else:
        messagebox.showwarning("Missing Info", "Please enter both name and phone.")

def view_contacts():
    contact_listbox.delete(0, tk.END)
    for number, contact in enumerate(contacts, start=1):
        display_text = f"{number}. {contact['name']} - {contact['phone']}"
        contact_listbox.insert(tk.END, display_text)

def search_contact():
    search_term = simpledialog.askstring("Search Contact", "Enter name or phone:")
    if search_term:
        contact_listbox.delete(0, tk.END)
        for number, contact in enumerate(contacts, start=1):
            if search_term.lower() in contact["name"].lower() or search_term in contact["phone"]:
                result = f"{number}. {contact['name']} - {contact['phone']}"
                contact_listbox.insert(tk.END, result)

def update_contact():
    selected = contact_listbox.curselection()
    if not selected:
        messagebox.showwarning("No Selection", "Please select a contact to update.")
        return

    index = selected[0]
    contact = contacts[index]

    contact["name"] = simpledialog.askstring("Update Name", "Name:", initialvalue=contact["name"])
    contact["phone"] = simpledialog.askstring("Update Phone", "Phone:", initialvalue=contact["phone"])
    contact["email"] = simpledialog.askstring("Update Email", "Email:", initialvalue=contact["email"])
    contact["address"] = simpledialog.askstring("Update Address", "Address:", initialvalue=contact["address"])

    view_contacts()

def delete_contact():
    selected = contact_listbox.curselection()
    if not selected:
        messagebox.showwarning("No Selection", "Please select a contact to delete.")
        return

    index = selected[0]
    contact_name = contacts[index]["name"]
    confirm = messagebox.askyesno("Delete Contact", f"Are you sure you want to delete {contact_name}?")
    
    if confirm:
        del contacts[index]
        view_contacts()


def clear_fields():
    name_var.set("")
    phone_var.set("")
    email_var.set("")
    address_var.set("")

def setup_ui(root):


    global name_var, phone_var, email_var, address_var, contact_listbox

    name_var = tk.StringVar()
    phone_var = tk.StringVar()
    email_var = tk.StringVar()
    address_var = tk.StringVar()

    tk.Label(root, text="Name").grid(row=0, column=0)
    tk.Entry(root, textvariable=name_var).grid(row=0, column=1)

    tk.Label(root, text="Phone").grid(row=1, column=0)
    tk.Entry(root, textvariable=phone_var).grid(row=1, column=1)

    tk.Label(root, text="Email").grid(row=2, column=0)
    tk.Entry(root, textvariable=email_var).grid(row=2, column=1)

    tk.Label(root, text="Address").grid(row=3, column=0)
    tk.Entry(root, textvariable=address_var).grid(row=3, column=1)

    tk.Button(root, text="Add Contact", command=add_contact).grid(row=4, column=0, columnspan=2)

    tk.Button(root, text="View Contacts", command=view_contacts).grid(row=5, column=0, columnspan=2)

    tk.Button(root, text="Search Contact", command=search_contact).grid(row=6, column=0, columnspan=2)

    tk.Button(root, text="Update Contact", command=update_contact).grid(row=7, column=0, columnspan=2)

    tk.Button(root, text="Delete Contact", command=delete_contact).grid(row=8, column=0, columnspan=2)

    contact_listbox = tk.Listbox(root, width=50)
    contact_listbox.grid(row=9, column=0, columnspan=2, pady=10)
    
root = tk.Tk()
root.title("Contact Book")
setup_ui(root)
root.mainloop()


