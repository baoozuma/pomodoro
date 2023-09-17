import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        self.work_time = 25 * 60  # Thời gian làm việc mặc định là 25 phút
        self.break_time = 5 * 60  # Thời gian nghỉ mặc định là 5 phút
        self.remaining_time = self.work_time
        self.is_working = False

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 18), padding=10)
        self.style.configure("TLabel", font=("Helvetica", 20))

        self.font_bold = font.Font(weight="bold", size=40)

        self.label = ttk.Label(root, text="", style="TLabel")
        self.label.pack(pady=20)

        self.button_frame = ttk.Frame(root)
        self.button_frame.pack(pady=10)

        self.start_button = ttk.Button(self.button_frame, text="Bắt đầu Pomodoro", command=self.start_timer)
        self.start_button.grid(row=0, column=0, padx=10)

        self.stop_button = ttk.Button(self.button_frame, text="Dừng", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.grid(row=0, column=1, padx=10)

        self.reset_button = ttk.Button(self.button_frame, text="Đặt lại", command=self.reset_timer)
        self.reset_button.grid(row=0, column=2, padx=10)

        self.break_time_label = ttk.Label(root, text="Thời gian nghỉ (phút):", style="TLabel")
        self.break_time_label.pack()
        self.break_time_entry = ttk.Entry(root)
        self.break_time_entry.pack()
        self.break_time_entry.insert(0, "5")

        self.work_time_label = ttk.Label(root, text="Thời gian làm việc (phút):", style="TLabel")
        self.work_time_label.pack()
        self.work_time_entry = ttk.Entry(root)
        self.work_time_entry.pack()
        self.work_time_entry.insert(0, "25")

    def start_timer(self):
        if not self.is_working:
            self.is_working = True
            self.work_time = int(self.work_time_entry.get()) * 60
            self.break_time = int(self.break_time_entry.get()) * 60
            self.update_timer()
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)

    def stop_timer(self):
        if self.is_working:
            self.is_working = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def reset_timer(self):
        self.is_working = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.work_time = int(self.work_time_entry.get()) * 60
        self.break_time = int(self.break_time_entry.get()) * 60
        self.remaining_time = self.work_time
        self.update_display()

    def update_timer(self):
        if self.is_working:
            self.remaining_time -= 1
            if self.remaining_time < 0:
                self.is_working = False
                self.remaining_time = self.break_time if self.remaining_time == -1 else self.work_time
                messagebox.showinfo("Pomodoro", "Chu kỳ đã kết thúc!")

            self.update_display()
            self.root.after(1000, self.update_timer)

    def update_display(self):
        minutes, seconds = divmod(self.remaining_time, 60)
        time_str = f"{minutes:02d}:{seconds:02d}"
        self.label.config(text=time_str, font=self.font_bold)

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()
