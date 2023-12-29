import customtkinter
from CTkTable import *
from config.api import toArr

def pop():
    root = customtkinter.CTk()
    root.title("Selengkapnya")
    csv_file_path = 'file/prev.csv'
    value= toArr(csv_file_path)
    elementHead = ["Row","Tanggal","imsyak","shubuh","terbit","dhuha","dzuhur","ashr","magrib","isya"]
    if value is not None:
        value.insert(0,elementHead)
    table = CTkTable(master=root, row=len(value), column=9, values=value)

    table.pack(expand=True, fill="both", padx=20, pady=20)
    root.mainloop()
