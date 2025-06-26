import subprocess
import sys
import os
import tempfile
import textwrap

def install_mitmproxy():
    try:
        import mitmproxy  # noqa: F401
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "mitmproxy"])

def write_mitm_script():
    script_content = textwrap.dedent('''
        from mitmproxy import http, ctx

        def response(flow: http.HTTPFlow):
            if flow.request.method == "GET" and "cryptauth.xyz/api.php" in flow.request.pretty_url:
                if flow.response and flow.response.headers.get("content-type", "").startswith("application/json"):
                    original_body = flow.response.text.strip()
                    if original_body == '{"status":"error","message":"Invalid license key"}':
                        flow.response.text = '{"status":"success"}'
                        ctx.log.info("Response modified - shutting down mitmweb.")
                        ctx.master.shutdown()
    ''')
    temp_dir = tempfile.gettempdir()
    script_path = os.path.join(temp_dir, "krack_mitm_patch.py")
    with open(script_path, "w", encoding="utf-8") as f:
        f.write(script_content)
    return script_path

def run_mitmweb(script_path):
    subprocess.run(["mitmweb", "--mode", "local", "-s", script_path])

def run_mitmproxy_patch():
    install_mitmproxy()
    script_path = write_mitm_script()
    print("\n[!] One Page Opened — Goto FILE > Install Certificate!")
    run_mitmweb(script_path)

def download_mitmproxy():
    import webbrowser
    import time
    from pathlib import Path

    print("[+] Opening mitmproxy Windows installer download page...")
    webbrowser.open("https://downloads.mitmproxy.org/12.1.1/mitmproxy-12.1.1-windows-x86_64-installer.exe")
    print("[~] Waiting for download to complete...")
    filename = "mitmproxy-12.1.1-windows-x86_64-installer.exe"
    downloads_path = str(Path.home() / "Downloads")
    filepath = os.path.join(downloads_path, filename)
    for i in range(60):
        if os.path.exists(filepath):
            print("[+] Installer found. Launching...")
            os.startfile(filepath)
            break
        time.sleep(1)
    else:
        print("[!] Could not find the downloaded installer.")

def mitmproxy_menu():
    while True:
        from utils.animation import clear, wait
        clear()
        print(r"""
╔════════════════════════════════════╗
║       Mitmproxy Patch Options     ║
╠════════════════════════════════════╣
║  [1] Run mitmweb Patch            ║
║  [2] Download mitmproxy (Windows)║
║  [0] Back to Main Menu           ║
╚════════════════════════════════════╝
        """)
        sub_choice = input("[>] Select an option: ").strip()
        if sub_choice == '1':
            run_mitmproxy_patch()
        elif sub_choice == '2':
            download_mitmproxy()
        elif sub_choice == '0':
            break
        else:
            print("[!] Invalid option.")
            wait()
