import time
from datetime import datetime as dt

# putanja do hosts datoteke, promijenite prema vašem operativnom sistemu
hosts_path = "/etc/hosts" # za linux/mac
# hosts_path = "C:\\Windows\\System32\\drivers\\etc\\hosts" # za windows

redirect = "127.0.0.1"

# web stranice koje želite blokirati
website_list = ["www.example.com", "example.com"]

def block_websites():
    with open(hosts_path, 'r+') as file:
        content = file.read()
        for website in website_list:
            if website in content:
                pass
            else:
                file.write(redirect + " " + website + "\n")

def unblock_websites():
    with open(hosts_path, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in website_list):
                file.write(line)
        file.truncate()

def add_website_to_blocklist(website):
    if website not in website_list:
        website_list.append(website)

def remove_website_from_blocklist(website):
    if website in website_list:
        website_list.remove(website)

while True:
    # vrijeme tijekom kojeg želite blokirati web stranice
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Radno vrijeme...")
        block_websites()
    else:
        print("Slobodno vrijeme...")
        unblock_websites()
    time.sleep(5)
