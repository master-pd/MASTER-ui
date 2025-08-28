#!/data/data/com.termux/files/usr/bin/python3
import random, requests, time, os
from prettytable import PrettyTable

# ANSI Colors
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

UA_FILES = ["android.txt", "browsers.txt", "linkcheckers.txt"]

def banner():
    os.system("clear")
    print(CYAN + "╔══════════════════════════════════════════════╗")
    print("║              MAR PD TOOL                     ║")
    print("║         Tool No. 2 | Version 1               ║")
    print("║  Creator : MASTER 🪓                          ║")
    print("║  Created : 2025-08-28                        ║")
    print("║  Thanks for using our tool!                  ║")
    print("╚══════════════════════════════════════════════╝" + RESET)
    print()

def load_user_agents():
    user_agents = []
    for f in UA_FILES:
        if os.path.exists(f):
            with open(f, "r") as file:
                lines = [line.strip() for line in file if line.strip()]
                user_agents.extend(lines)
    return user_agents

def animate_status(success, fail, delay=0.1):
    """ নিচ থেকে ওপরে counter animation """
    os.system("clear")
    banner()
    print("\n" * 5)  # নিচে থেকে শুরু
    print(GREEN + f"✅ Success Hits : {success}" + RESET)
    print(RED + f"❌ Failed Hits  : {fail}" + RESET)
    time.sleep(delay)

def send_requests(url, user_agents, count=5):
    success, fail = 0, 0
    table = PrettyTable()
    table.field_names = ["#", "User-Agent (short)", "Status"]

    for i in range(count):
        ua = random.choice(user_agents)
        headers = {"User-Agent": ua}
        try:
            resp = requests.get(url, headers=headers, timeout=5)
            status = f"{resp.status_code}"
            success += 1
        except Exception:
            status = "Error"
            fail += 1

        table.add_row([i+1, ua[:40] + "...", status])
        animate_status(success, fail)

    print("\n" + CYAN + "══════════ FINAL REPORT ══════════" + RESET)
    print(table)
    print(GREEN + f"\n✅ Total Success: {success}" + RESET)
    print(RED + f"❌ Total Failed : {fail}" + RESET)

def show_menu():
    print(CYAN + "╔══════════════════════════════╗")
    print("║         MAIN MENU            ║")
    print("╚══════════════════════════════╝" + RESET)
    print("[1] Single Request with Random UA")
    print("[2] Multiple Requests with Random UA")
    print("[3] Show UA Count")
    print("[0] Exit")

def main():
    banner()
    user_agents = load_user_agents()
    if not user_agents:
        print("❌ No user-agent files found!")
        return
    
    url = input("🌐 Enter target URL (e.g. https://httpbin.org/headers): ")
    
    while True:
        show_menu()
        choice = input("\nEnter choice: ")
        if choice == "1":
            send_requests(url, user_agents, 1)
            input("\nPress Enter to continue...")
        elif choice == "2":
            count = int(input("How many requests? "))
            send_requests(url, user_agents, count)
            input("\nPress Enter to continue...")
        elif choice == "3":
            print(f"\n📌 Total User-Agents loaded: {len(user_agents)}")
            input("\nPress Enter to continue...")
        elif choice == "0":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice!")
            time.sleep(1)

if __name__ == "__main__":
    main()