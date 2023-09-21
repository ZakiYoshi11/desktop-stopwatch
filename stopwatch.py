import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter import font

# Variabel global untuk menyimpan waktu saat ini
current_time = 0
is_running = False

def start():
    global is_running
    if not is_running:
        is_running = True
        update()
        start_button.place_forget()  # Menghapus tombol "Start"
        stop_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Menampilkan tombol "Stop" di tengah
        reset_button.place(relx=0.5, rely=0.65, anchor=tk.CENTER)  # Menampilkan tombol "Reset" di tengah

def stop():
    global is_running
    if is_running:
        is_running = False
        stop_button.config(text="Continue")  # Mengganti teks tombol menjadi "Continue"
        start_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Menampilkan tombol "Start" di tengah
        reset_button.place(relx=0.5, rely=0.65, anchor=tk.CENTER)  # Menampilkan tombol "Reset" di tengah
    else:
        is_running = True
        stop_button.config(text="Stop")  # Mengganti teks tombol menjadi "Stop" kembali
        update()  # Melanjutkan stopwatch
        start_button.place_forget()  # Menghapus tombol "Start"
        reset_button.place_forget()  # Menghapus tombol "Reset"

def reset():
    global current_time, is_running
    current_time = 0
    is_running = False
    update_time()
    start_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Menampilkan tombol "Start" di tengah
    stop_button.config(text="Stop")  # Mengganti teks tombol "Stop"
    stop_button.place_forget()  # Menghapus tombol "Stop"
    reset_button.place_forget()  # Menghapus tombol "Reset"

def update():
    global current_time, is_running
    if is_running:
        current_time += 1  # Tambahkan satu detik
        update_time()
        root.after(10, update)  # Panggil diri sendiri setiap 10 milidetik

def update_time():
    minutes = current_time // 600
    seconds = (current_time // 10) % 60
    milliseconds = current_time % 10
    time_str = f"{minutes:02}:{seconds:02}:{milliseconds}"
    time_label.config(text=time_str)

# Membuat jendela Tkinter
root = tk.Tk()
root.title("Stopwatch App")

# Mengubah warna latar belakang
root.configure(bg="#000000")  # Warna hitam

# Membuat font tebal
bold_font = font.Font(family="Arial", size=48, weight="bold")

# Label untuk menampilkan waktu
time_label = tk.Label(root, text="00:00:00", font=bold_font, bg="#000000", fg="white")
time_label.pack(pady=20)

# Create a custom style for rounded buttons
rounded_button_style = ttk.Style()
rounded_button_style.configure(
    "Rounded.TButton",
    borderwidth=0,
    relief="flat",
    padding=(10, 5),
)

# Create rounded buttons
start_button = ttk.Button(
    root,
    text="Start",
    command=start,
    style="Rounded.TButton",
    cursor="hand2",  # Mengubah kursor menjadi tangan saat di atas tombol
)
stop_button = ttk.Button(
    root,
    text="Stop",
    command=stop,
    style="Rounded.TButton",
    cursor="hand2",
)
reset_button = ttk.Button(
    root,
    text="Reset",
    command=reset,
    style="Rounded.TButton",
    cursor="hand2",
)

# Menampilkan tombol "Start" di tengah
start_button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

# Tombol "Stop" dan "Reset" yang dihapus awalnya
stop_button.place_forget()
reset_button.place_forget()

root.mainloop()

