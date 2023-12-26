import customtkinter
from CTkTable import *
import pandas as pd
from config.api import toArr
root = customtkinter.CTk()
def pop():
    csv_file_path = 'file/prev.csv'
    value= toArr(csv_file_path)
    elementHead = ["Row","Tanggal","imsyak","shubuh","terbit","dhuha","dzuhur","ashr","magrib","isya"]
    if value is not None:
        value.insert(0,elementHead)
    # value = [["Tgl","imsyak","shubuh","terbit","dhuha","dzuhur","ashr","magrib","isya"],
    #         [1,2,3,4,5],
    #         [1,2,3,4,5],
    #         [1,2,3,4,5],
    #         [1,2,3,4,5],
    #         [1,2,3,4,5],
    #         [1,2,3,4,5]]

    table = CTkTable(master=root, row=len(value), column=9, values=value)

    table.pack(expand=True, fill="both", padx=20, pady=20)
    root.mainloop()
    destHis()
def destHis():
    root.withdraw()

if __name__ == '__main__':
    pop()