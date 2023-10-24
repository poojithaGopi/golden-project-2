import tkinter as tk
from tkinter import messagebox


class MailApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Mail Application")

        self.label_to = tk.Label(root, text="To:")
        self.label_to.pack()
        self.entry_to = tk.Entry(root, width=40)
        self.entry_to.pack(pady=10)

        self.label_subject = tk.Label(root, text="Subject:")
        self.label_subject.pack()
        self.entry_subject = tk.Entry(root, width=40)
        self.entry_subject.pack(pady=10)

        self.label_message = tk.Label(root, text="Message:")
        self.label_message.pack()
        self.text_message = tk.Text(root, width=40, height=10)
        self.text_message.pack(pady=10)

        self.send_button = tk.Button(root, text="Send Email", command=self.send_email)
        self.send_button.pack(pady=20)

    def send_email(self):
        recipient = self.entry_to.get()
        subject = self.entry_subject.get()
        message = self.text_message.get("1.0", tk.END)

        # Here, you would integrate with an email service's API to send the email.
        # For simplicity, we are just printing the email details.
        print(f"Recipient: {recipient}")
        print(f"Subject: {subject}")
        print(f"Message: {message}")

        messagebox.showinfo("Success", "Email sent successfully!")


# Create the main window
root = tk.Tk()
mail_app = MailApplication(root)
root.config(background="brown")
root.mainloop()
