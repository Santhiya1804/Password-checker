import tkinter as tk
from tkinter import messagebox
from password_checker import check_password_strength
from wordlist_generator import generate_variants, save_wordlist

def analyze():
    pw = password_entry.get()
    data = check_password_strength(pw)
    score_label.config(text=f"Strength Score: {data['score']} (0=Weak, 4=Strong)")
    time_label.config(text=f"Estimated Crack Time: {data['crack_time']}")
    feedback_label.config(text="Feedback: " + ' '.join(data['feedback']['suggestions'] or ['Good!']))

def generate_wordlist():
    details = [name_entry.get(), dob_entry.get(), pet_entry.get()]
    wordlist = generate_variants(details)
    filename = save_wordlist(wordlist)
    messagebox.showinfo("Wordlist Created", f"Saved to: {filename}")

app = tk.Tk()
app.title("🔐 Password Strength Analyzer & Wordlist Generator")
app.geometry("500x400")
app.configure(bg="#f5f5f5")

tk.Label(app, text="Enter Password:", bg="#f5f5f5").pack()
password_entry = tk.Entry(app, show="*", width=40)
password_entry.pack()

tk.Button(app, text="Check Strength", command=analyze).pack(pady=5)
score_label = tk.Label(app, text="", bg="#f5f5f5")
score_label.pack()
time_label = tk.Label(app, text="", bg="#f5f5f5")
time_label.pack()
feedback_label = tk.Label(app, text="", wraplength=400, bg="#f5f5f5")
feedback_label.pack(pady=5)

tk.Label(app, text="\n🔧 Generate Custom Wordlist", bg="#f5f5f5", font=('Arial', 12, 'bold')).pack()

tk.Label(app, text="Name:", bg="#f5f5f5").pack()
name_entry = tk.Entry(app, width=40)
name_entry.pack()

tk.Label(app, text="DOB (eg: 1998 or 0101):", bg="#f5f5f5").pack()
dob_entry = tk.Entry(app, width=40)
dob_entry.pack()

tk.Label(app, text="Pet's Name:", bg="#f5f5f5").pack()
pet_entry = tk.Entry(app, width=40)
pet_entry.pack()

tk.Button(app, text="Generate Wordlist", command=generate_wordlist).pack(pady=10)

app.mainloop()
