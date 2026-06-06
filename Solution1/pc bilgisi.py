import psutil
import platform
import socket
def cpu_bilgi():
        return psutil.cpu_percent(interval=1)
def ram_bilgisi():
    ram = psutil.virtual_memory()
    return ram.percent
def isletim_sistemi():
    return platform.system(), platform.version()
def islemci():
    return platform.processor()
def pc_adi():
    return socket.gethostname()
def ip_adresi():
    return socket.gethostbyname(socket.gethostname())
print ("CPU:", cpu_bilgi())
print ("RAM:", ram_bilgisi)
print ("OS:", isletim_sistemi())
print ("CPU Model:", islemci())
print ("Pc Adı:", pc_adi())
print ("ip adresi:", ip_adresi())