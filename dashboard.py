
import time
import customtkinter
import tkinter
from history import pop
from config.api import *
from assets.template.CTkScrollableDropdown import *

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")  

class JadwalSholat(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("Jadwal Sholat")
        self.geometry(f"{1000}x{750}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.sidebar_frame = customtkinter.CTkFrame(self, width=10, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=2)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Jadwal Sholat", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.clock_lbl = customtkinter.CTkLabel(self.sidebar_frame,font=customtkinter.CTkFont(size=20, weight="bold"))
        self.clock_lbl.grid(row=1, column=0, padx=20, pady=(20, 10))
        self.clock()
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", )
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="Scalling % :", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80", "90", "100", "110", "120"],
                                                               command=self.change_scaling_event)
        
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))
 
        self.dropdownFrame = customtkinter.CTkFrame(self)
        self.dropdownFrame.grid(row=0, column=1, padx=(20, 20), pady=(20, 100), sticky="nsew")
        self.labelDd = customtkinter.CTkLabel(self.dropdownFrame, text="Pilih Daerahmu", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.labelDd.grid(row=1, column=2, padx=(300, 30), pady=(20, 200))

        
        self.scaling_optionemenu = customtkinter.CTkComboBox(self.dropdownFrame,width=240,values=getCities())
        self.scaling_optionemenu.grid(row=1, column=2, padx=(300, 20), pady=(20, 100))
        self.cbx = CTkScrollableDropdown(self.scaling_optionemenu, values=getCities())
        
        self.buttonSubmit = customtkinter.CTkButton(self.dropdownFrame,text="Submit", command=self.displayResponse)
        self.buttonSubmit.grid(row=1, column=2, padx=(300, 20), pady=(20, 1))


        self.string_input_button = customtkinter.CTkButton(master=self, text="Selengkapnya",
                                                           command=pop)
        self.string_input_button.place(x=520,y=710)
        self.scaling_optionemenu.set("malang")
    def getValueComboBox(self):
        return self.scaling_optionemenu.get()
    
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)


    def clock(self):
        string = time.strftime('%H:%M:%S'+"  WIB")
        self.clock_lbl.configure(text = string)
        self.clock_lbl.after(1000, self.clock)
    
    def displayResponse(win):
        response = getDaily(win.getValueComboBox())
        if response is not False:
            win.dropdownFrame1 = customtkinter.CTkFrame(win)
            win.dropdownFrame1.grid(row=1, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
            labelTgl = customtkinter.CTkLabel(win.dropdownFrame1, text=f"Tanggal : {response['tanggal']} Daerah : {win.getValueComboBox()}",font=("bold", 12))
            labelTgl.place(x=320,y=10)
            labelImsyak = customtkinter.CTkLabel(win.dropdownFrame1, text=f"Imsyak  = {response['imsyak']}",font=("bold", 12))
            labelImsyak.place(x=10,y=30)
            labelShubuh = customtkinter.CTkLabel(win.dropdownFrame1, text=f"Shubuh  = {response['shubuh']}",font=("bold", 12))
            labelShubuh.place(x=10,y=50)
            labelTerbit = customtkinter.CTkLabel(win.dropdownFrame1, text=f"Terbit  = {response['terbit']}",font=("bold", 12))
            labelTerbit.place(x=10,y=70)
            labelDhuha = customtkinter.CTkLabel(win.dropdownFrame1, text=f"Dhuha  = {response['dhuha']}",font=("bold", 12))
            labelDhuha.place(x=10,y=90)
            labelDzuhur = customtkinter.CTkLabel(win.dropdownFrame1, text=f"Dzuhur  = {response['dzuhur']}",font=("bold", 12))
            labelDzuhur.place(x=10,y=110)
            labelAshr = customtkinter.CTkLabel(win.dropdownFrame1, text=f"Ashr  = {response['ashr']}",font=("bold", 12))
            labelAshr.place(x=10,y=130)
            labelMaghrib = customtkinter.CTkLabel(win.dropdownFrame1, text=f"Maghrib = {response['magrib']}",font=("bold", 12))
            labelMaghrib.place(x=10,y=150)
            labelIsya = customtkinter.CTkLabel(win.dropdownFrame1, text=f"Isya  = {response['isya']}",font=("bold", 12))
            labelIsya.place(x=10,y=170)
        