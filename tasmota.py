import time
import requests   

debug = 0

class tasmota:
    def __init__(device, ip, user, pwd):
        device.ip = ip
        device.user = user
        device.pwd = pwd
        device.switch = ""
        device.temperature = 0.0
        
       
        
    def send(device, command):
        if debug: print ("Sending command "+ command +" to "+ device.ip)
        timeStart = time.time()
        r = requests.get (url="http://"+device.ip+"/cm?user="+device.user+"&password="+device.pwd+"&cmnd="+command)
        pollTime = str(time.time() - timeStart)
        if debug: print ("Polltime: " + pollTime)
        data = r.json() 
        return (data)
      
    def on(device):
        data = tasmota.send (device, "Power%20On")
        device.switch = data["POWER"]
        return (device.switch)
        
    def off(device):
        data = tasmota.send (device, "Power%20Off")
        device.switch = data["POWER"]
        return (device.switch)
        

    def toggle(device):
        data = tasmota.send (device, "Power%20TOGGLE")
        device.switch = data["POWER"]
        return (device.switch)
            
    def switchStatus(device):
        data = tasmota.send (device, "Power")
        device.switch = data["POWER"]
        return (device.switch)
    
    def updateTemperature(device):
        data = tasmota.send (device, "STATUS%208")
        device.temperature = (data['StatusSNS']['DS18B20']['Temperature'])
        return (device.temperature)