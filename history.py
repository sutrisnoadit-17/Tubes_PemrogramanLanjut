import customtkinter
from CTkTable import *
def pop():
    root = customtkinter.CTk()
    root.title("History Previous")
    value = [["Tgl","imsyak","shubuh","terbit","dhuha","dzuhur","ashr","magrib","isya"],
            [1,2,3,4,5],
            [1,2,3,4,5],
            [1,2,3,4,5],
            [1,2,3,4,5],
            [1,2,3,4,5],
            [1,2,3,4,5]]

    table = CTkTable(master=root, row=30, column=9, values=value)

    table.pack(expand=True, fill="both", padx=20, pady=20)
    root.mainloop()
