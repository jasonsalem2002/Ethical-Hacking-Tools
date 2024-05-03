from termcolor import colored, cprint
import argparse, subprocess

def displayHeader():
        cprint(
            """\
   __     ______     __  __     _____     ______     __   __                                          
  /\ \   /\  __ \   /\ \_\ \   /\  __-.  /\  __ \   /\ "-.\ \                                         
 _\_\ \  \ \  __ \  \ \____ \  \ \ \/\ \ \ \ \/\ \  \ \ \-.  \                                        
/\_____\  \ \_\ \_\  \/\_____\  \ \____-  \ \_____\  \ \_\\"\_\                                       
\/_____/   \/_/\/_/   \/_____/   \/____/   \/_____/   \/_/ \/_/                                       
                                                                                                      
 __    __     ______     ______     __  __     ______     __   __     ______     ______     ______    
/\ "-./  \   /\  __ \   /\  ___\   /\ \_\ \   /\  __ \   /\ "-.\ \   /\  ___\   /\  ___\   /\  == \   
\ \ \-./\ \  \ \  __ \  \ \ \____  \ \  __ \  \ \  __ \  \ \ \-.  \  \ \ \__ \  \ \  __\   \ \  __<   
 \ \_\ \ \_\  \ \_\ \_\  \ \_____\  \ \_\ \_\  \ \_\ \_\  \ \_\\"\_\  \ \_____\  \ \_____\  \ \_\ \_\ 
  \/_/  \/_/   \/_/\/_/   \/_____/   \/_/\/_/   \/_/\/_/   \/_/ \/_/   \/_____/   \/_____/   \/_/ /_/ 
                                                                                                                                                                                                                                                                                            

            by Jay and DonC\n""",'green')
        
displayHeader()

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_argument("-m", "--mac", dest="new_mac", help="New MAC address")
    options = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new MAC address, use --help for more info.")
    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    
if __name__ == '__main__':
    options = get_arguments()
    change_mac(options.interface, options.new_mac)
    print("[+] MAC address changed to " + options.new_mac)