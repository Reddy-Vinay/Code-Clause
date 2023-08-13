import tkinter as tk
from tkinter import messagebox

class MailApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mail Application")
        
        self.label = tk.Label(root, text="Welcome to the Mail App")
        self.label.pack(pady=10)
        
        self.sender_label = tk.Label(root, text="Sender:")
        self.sender_label.pack()
        self.sender_entry = tk.Entry(root)
        self.sender_entry.pack()
        
        self.receiver_label = tk.Label(root, text="Receiver:")
        self.receiver_label.pack()
        self.receiver_entry = tk.Entry(root)
        self.receiver_entry.pack()
        
        self.subject_label = tk.Label(root, text="Subject:")
        self.subject_label.pack()
        self.subject_entry = tk.Entry(root)
        self.subject_entry.pack()
        
        self.message_label = tk.Label(root, text="Message:")
        self.message_label.pack()
        self.message_text = tk.Text(root, height=5, width=30)
        self.message_text.pack()
        
        self.send_button = tk.Button(root, text="Send", command=self.send_mail)
        self.send_button.pack(pady=10)
        
    def send_mail(self):
        sender = self.sender_entry.get()
        receiver = self.receiver_entry.get()
        subject = self.subject_entry.get()
        message = self.message_text.get("1.0", "end-1c")
        
        if sender and receiver and subject and message:
            # Here, you would typically implement the email sending logic.
            # For this example, we'll just display a message.
            messagebox.showinfo("Mail Sent", "Mail sent successfully!")
        else:
            messagebox.showwarning("Missing Information", "Please fill in all fields.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MailApp(root)
    root.mainloop()