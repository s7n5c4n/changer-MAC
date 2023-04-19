import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help = "Interface para cambiar Direccion MAC" )
parser.add_option("-m", "--mac", dest ="new_mac", help = "Nueva Direccion MAC")

(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

print("[+] cambiando direccion mac para "+ interface + " a " + new_mac)

def changer_mac (interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])



changer_mac(options.interface, options.new_mac)


