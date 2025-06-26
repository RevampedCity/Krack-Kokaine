import re
import os
import webbrowser
from tkinter import Tk, filedialog
from utils.animation import clear, wait

ORDER_LINK_REGEX = r"^https://[^/]+\.sellhub\.cx/order/[a-zA-Z0-9\-]+$"

def select_txt_file():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select .txt File with Sellhub Links", filetypes=[("Text files", "*.txt")])
    return file_path

def filter_sellhub_orders(file_path):
    if not os.path.exists(file_path):
        print(f"[!] File '{file_path}' not found.")
        return []

    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    valid = [line for line in lines if re.match(ORDER_LINK_REGEX, line)]

    with open(file_path, 'w') as f:
        for link in valid:
            f.write(link + '\n')

    print(f"[+] {len(valid)} valid order links found and saved.")
    return valid

def open_order_links(file_path):
    if not os.path.exists(file_path):
        print("[!] File not found.")
        return

    with open(file_path, 'r') as f:
        links = [line.strip() for line in f if line.strip()]

    for link in links:
        print(f"[>] Opening: {link}")
        webbrowser.open(link)
        input("[>] Press ENTER after you're done with this page...")

    print("[+] All links opened.")

def run_sellhub_tool():
    clear()
    print("[+] Please select a .txt file containing Sellhub.cx links...")
    file_path = select_txt_file()
    if not file_path:
        print("[!] No file selected.")
        return

    if input("[?] Want to save only valid SellHub order links? (y/n): ").lower().startswith('y'):
        filter_sellhub_orders(file_path)

    if input("[?] Want to open all pages now? (y/n): ").lower().startswith('y'):
        open_order_links(file_path)

    wait()
