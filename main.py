from loadScreen import *
from dashboard import *
from config.api import *
from history import *

if __name__ == '__main__':
    objDashboard = JadwalSholat()
    if loadingScreen():
        w.withdraw()
        objDashboard.mainloop()