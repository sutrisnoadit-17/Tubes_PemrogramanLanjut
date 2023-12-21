from loadScreen import *
from dashboard import *
if __name__ == '__main__':
    objDashboard = JadwalSholat()
    if loadingScreen():
        w.destroy()
        objDashboard.mainloop()