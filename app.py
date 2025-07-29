
import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
from password_checker import check_password_strength
from wordlist_generator import generate_variants, save_wordlist

app = tk.Tk()
app.title("🔐 Password Security Toolkit")
app.geometry("600x500")
app.configure(bg="#e6f0ff")

style = ttk.Style()
style.configure("TNotebook.Tab", padding=10, font=('Segoe UI', 10, 'bold'))
notebook = ttk.Notebook(app)
notebook.pack(expand=True, fill='both', padx=10, pady=10)

# ---------------- Tab 1: Password Strength Checker ----------------
tab1 = tk.Frame(notebook, bg="#fff")
notebook.add(tab1, text="🔍 Check Strength")

tk.Label(tab1, text="Enter Password:", bg="#fff", font=('Arial', 11)).pack(pady=10)
password_entry = tk.Entry(tab1, show="*", width=40, font=('Arial', 11))
password_entry.pack()

def analyze():
    pw = password_entry.get()
    data = check_password_strength(pw)
    score_label.config(text=f"Strength Score: {data['score']} (0=Weak, 4=Strong)")
    time_label.config(text=f"Estimated Crack Time: {data['crack_time']}")
    feedback_label.config(text="Feedback: " + ' '.join(data['feedback']['suggestions'] or ['Good!']))

tk.Button(tab1, text="Analyze Password", font=('Arial', 10, 'bold'), bg="#4CAF50", fg="white", command=analyze).pack(pady=10)

score_label = tk.Label(tab1, text="", bg="#fff", font=('Arial', 11))
score_label.pack()
time_label = tk.Label(tab1, text="", bg="#fff", font=('Arial', 11))
time_label.pack()
feedback_label = tk.Label(tab1, text="", bg="#fff", wraplength=500, font=('Arial', 10, 'italic'))
feedback_label.pack(pady=5)

# ---------------- Tab 2: Wordlist Generator ----------------
tab2 = tk.Frame(notebook, bg="#f9f9f9")
notebook.add(tab2, text="🛠️ Wordlist Generator")

tk.Label(tab2, text="Name:", bg="#f9f9f9", font=('Arial', 11)).pack(pady=(10, 0))
name_entry = tk.Entry(tab2, width=40, font=('Arial', 11))
name_entry.pack()

tk.Label(tab2, text="DOB (e.g., 1998 or 0101):", bg="#f9f9f9", font=('Arial', 11)).pack(pady=(10, 0))
dob_entry = tk.Entry(tab2, width=40, font=('Arial', 11))
dob_entry.pack()

tk.Label(tab2, text="Pet's Name:", bg="#f9f9f9", font=('Arial', 11)).pack(pady=(10, 0))
pet_entry = tk.Entry(tab2, width=40, font=('Arial', 11))
pet_entry.pack()

def generate_wordlist():
    details = [name_entry.get(), dob_entry.get(), pet_entry.get()]
    wordlist = generate_variants(details)
    filename = save_wordlist(wordlist)
    messagebox.showinfo("✅ Wordlist Created", f"Saved to: {filename}")

tk.Button(tab2, text="Generate Wordlist", font=('Arial', 10, 'bold'), bg="#2196F3", fg="white", command=generate_wordlist).pack(pady=15)

# ---------------- Tab 3: Password Suggestion ----------------
tab3 = tk.Frame(notebook, bg="#fff0f5")
notebook.add(tab3, text="💡 Suggest Passwords")

tk.Label(tab3, text="Strong Password Suggestions", bg="#fff0f5", font=('Arial', 12, 'bold')).pack(pady=10)

suggestions_box = tk.Text(tab3, height=8, width=50, font=('Courier', 11))
suggestions_box.pack()

def suggest_passwords():
    suggestions_box.delete("1.0", tk.END)
    for _ in range(5):
        pwd = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=12))
        suggestions_box.insert(tk.END, pwd + "\n")

tk.Button(tab3, text="Generate Suggestions", font=('Arial', 10, 'bold'), bg="#FF5722", fg="white", command=suggest_passwords).pack(pady=10)

app.mainloop()
