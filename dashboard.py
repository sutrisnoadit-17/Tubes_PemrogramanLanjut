
import time
import customtkinter
import tkinter
from history import pop

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

        self.sidebar_frame = customtkinter.CTkFrame(self, width=150, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
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

        # # batas tes
 
        self.dropdownFrame = customtkinter.CTkFrame(self)
        self.dropdownFrame.grid(row=0, column=1, padx=(20, 20), pady=(20, 100), sticky="nsew")
        self.labelDd = customtkinter.CTkLabel(self.dropdownFrame, text="Pilih Daerahmu", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.labelDd.grid(row=1, column=2, padx=(300, 30), pady=(20, 200))
        self.labelDda = customtkinter.CTkLabel(self.dropdownFrame, text="Provinsi", font=customtkinter.CTkFont(size=12))
        self.labelDda.grid(row=1, column=2, padx=(300, 20), pady=(70, 200))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.dropdownFrame, values=["??", "??", "??", "??", "??"]
                                                              )
        self.scaling_optionemenu.grid(row=1, column=2, padx=(300, 20), pady=(20, 100))
        self.labelDda2 = customtkinter.CTkLabel(self.dropdownFrame, text="Kab/Kota", font=customtkinter.CTkFont(size=12))
        self.labelDda2.grid(row=1, column=2, padx=(300, 20), pady=(18, 40))
        self.scaling_optionemenu2 = customtkinter.CTkOptionMenu(self.dropdownFrame, values=["??", "??", "??", "??", "??", "??"]
                                                              )
        self.scaling_optionemenu2.grid(row=1, column=2, padx=(300, 20), pady=(20, 1))
        self.buttonSubmit = customtkinter.CTkButton(self.dropdownFrame,text="Submit", command=self.sidebar_button_event)
        self.buttonSubmit.grid(row=1, column=2, padx=(300, 20), pady=(100, 1))
        #response form
        # labelTgl = customtkinter.CTkLabel(self, text="Output",font=("bold", 20))
        # labelTgl.place(x=350,y=350)
        self.dropdownFrame1 = customtkinter.CTkFrame(self)
        self.dropdownFrame1.grid(row=1, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        labelTgl = customtkinter.CTkLabel(self.dropdownFrame1, text="Tanggal : ??",font=("bold", 12))
        labelTgl.place(x=350,y=10)
        labelImsyak = customtkinter.CTkLabel(self.dropdownFrame1, text="Imsyak  =",font=("bold", 12))
        labelImsyak.place(x=10,y=30)
        labelShubuh = customtkinter.CTkLabel(self.dropdownFrame1, text="Shubuh  =",font=("bold", 12))
        labelShubuh.place(x=10,y=50)
        labelTerbit = customtkinter.CTkLabel(self.dropdownFrame1, text="Terbit  =",font=("bold", 12))
        labelTerbit.place(x=10,y=70)
        labelDhuha = customtkinter.CTkLabel(self.dropdownFrame1, text="Dhuha  =",font=("bold", 12))
        labelDhuha.place(x=10,y=90)
        labelDzuhur = customtkinter.CTkLabel(self.dropdownFrame1, text="Dzuhur  =",font=("bold", 12))
        labelDzuhur.place(x=10,y=110)
        labelAshr = customtkinter.CTkLabel(self.dropdownFrame1, text="Ashr  =",font=("bold", 12))
        labelAshr.place(x=10,y=130)
        labelMaghrib = customtkinter.CTkLabel(self.dropdownFrame1, text="Maghrib =",font=("bold", 12))
        labelMaghrib.place(x=10,y=150)
        labelIsya = customtkinter.CTkLabel(self.dropdownFrame1, text="Isya  =",font=("bold", 12))
        labelIsya.place(x=10,y=170)
        self.string_input_button = customtkinter.CTkButton(master=self, text="Selengkapnya",
                                                           command=pop)
        self.string_input_button.place(x=520,y=710)


    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def clock(self):
        string = time.strftime('%H:%M:%S'+"  WIB")
        self.clock_lbl.configure(text = string)
        self.clock_lbl.after(1000, self.clock)
        