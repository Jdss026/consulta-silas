import tkinter as tk
from tkinter import ttk
from json_parser import listarObras

def on_select(event):
    selected_option = combo.get()
    print("Selected option:", selected_option)

def on_key_release(event):
    search_text = combo.get()
    matching_options = [option for option in options if search_text.lower() in option.lower()]
    update_listbox(matching_options)

def update_listbox(matching_options):
    listbox.delete(0, tk.END)
    for option in matching_options:
        listbox.insert(tk.END, option)

def on_listbox_select(event):
    selected_option = listbox.get(listbox.curselection())
    combo.set(selected_option)

# Create a window
window = tk.Tk()

# Create a Combobox
combo = ttk.Combobox(window, width=20)
combo.bind("<<ComboboxSelected>>", on_select)
combo.bind("<KeyRelease>", on_key_release)
combo.pack()

# Options for the dropdown menu
options = listarObras()

# Create a Listbox for displaying the options
listbox = tk.Listbox(window, width=60, height=30)
listbox.bind("<<ListboxSelect>>", on_listbox_select)
listbox.pack()

# Start the event loop
window.mainloop()
