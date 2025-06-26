import time
from sellhub_tool import run_sellhub_tool
from mitm_patch import mitmproxy_menu
from utils.animation import skull_bump_animation, clear, wait

def main_menu():
    while True:
        clear()
        skull_bump_animation()
        print(r"""
╔════════════════════════════════════╗
║            KRACK KOKAINE           ║
╠════════════════════════════════════╣
║  [1] SellHub Order Tool           ║
║  [2] Mitmproxy Patch Tool         ║
║  [0] Exit                         ║
╚════════════════════════════════════╝
        """)
        choice = input("[>] Select an option: ").strip()
        if choice == '1':
            run_sellhub_tool()
        elif choice == '2':
            mitmproxy_menu()
        elif choice == '0':
            print("[*] Exiting...")
            time.sleep(1)
            break
        else:
            print("[!] Invalid option.")
            wait()

if __name__ == '__main__':
    main_menu()
