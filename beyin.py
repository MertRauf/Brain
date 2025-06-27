# -*- coding: utf-8 -*-
import serial
import tkinter as tk
from tkinter import messagebox, ttk, Toplevel
from PIL import Image, ImageTk
import time

class BrainControlApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Brain Functions Simulation")
        self.root.attributes('-fullscreen', True)
        self.ser = None
        self.theme = "light"
        self.education_mode = False

        # Theme colors
        self.themes = {
            "light": {"bg": "#F0F0F0", "panel": "#E0E0E0", "btn": "#D3D3D3", "text": "black"},
            "dark": {"bg": "#2F2F2F", "panel": "#404040", "btn": "#5C5C5C", "text": "white"},
            "red": {"bg": "#FFCCCC", "panel": "#FF9999", "btn": "#FF6666", "text": "black"}
        }

        # Screen dimensions
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()

        # Left panel
        self.left_frame = tk.Frame(root, bg=self.themes[self.theme]["panel"], width=self.screen_width//6)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Canvas for brain image
        self.canvas = tk.Canvas(root, bg=self.themes[self.theme]["bg"], width=self.screen_width*5//6, height=self.screen_height, highlightthickness=0)
        self.canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Apply theme
        self.apply_theme()

        # Port input field
        tk.Label(self.left_frame, text="Arduino Port:", bg=self.themes[self.theme]["panel"], fg=self.themes[self.theme]["text"], font=("Helvetica", 14, "bold")).pack(pady=10)
        self.port_entry = tk.Entry(self.left_frame, font=("Helvetica", 12), bg="white", fg=self.themes[self.theme]["text"], insertbackground=self.themes[self.theme]["text"])
        self.port_entry.pack(pady=10, padx=10, fill=tk.X)
        self.port_entry.insert(0, "COM5")

        # Status label
        self.status_label = tk.Label(self.left_frame, text="Status: Not Connected", fg=self.themes[self.theme]["text"], bg=self.themes[self.theme]["panel"], font=("Helvetica", 12))
        self.status_label.pack(pady=10)

        # Button style
        style = ttk.Style()
        style.configure("Custom.TButton", font=("Helvetica", 16, "bold"), padding=10, background=self.themes[self.theme]["btn"], foreground=self.themes[self.theme]["text"])
        style.map("Custom.TButton", background=[("active", self.get_active_btn_color())])

        # Buttons
        self.connect_btn = ttk.Button(self.left_frame, text="🔗 Connect", style="Custom.TButton", command=self.connect_arduino)
        self.connect_btn.pack(pady=10, padx=10, fill=tk.X)

        self.vision_btn = ttk.Button(self.left_frame, text="👁️ Vision", style="Custom.TButton", command=self.show_vision_info)
        self.vision_btn.pack(pady=10, padx=10, fill=tk.X)

        self.hearing_btn = ttk.Button(self.left_frame, text="👂 Hearing", style="Custom.TButton", command=self.show_hearing_info)
        self.hearing_btn.pack(pady=10, padx=10, fill=tk.X)

        self.speech_btn = ttk.Button(self.left_frame, text="💬 Speech", style="Custom.TButton", command=self.show_speech_info)
        self.speech_btn.pack(pady=10, padx=10, fill=tk.X)

        self.movement_btn = ttk.Button(self.left_frame, text="🏃 Movement", style="Custom.TButton", command=self.show_movement_info)
        self.movement_btn.pack(pady=10, padx=10, fill=tk.X)

        self.smell_btn = ttk.Button(self.left_frame, text="👃 Smell", style="Custom.TButton", command=self.show_smell_info)
        self.smell_btn.pack(pady=10, padx=10, fill=tk.X)

        self.settings_btn = ttk.Button(self.left_frame, text="⚙️ Settings", style="Custom.TButton", command=self.open_settings)
        self.settings_btn.pack(pady=10, padx=10, fill=tk.X)

        self.education_btn = ttk.Button(self.left_frame, text="📚 Education Mode", style="Custom.TButton", command=self.toggle_education_mode)
        self.education_btn.pack(pady=10, padx=10, fill=tk.X)

        self.exit_btn = ttk.Button(self.left_frame, text="🚪 Exit", style="Custom.TButton", command=self.quit_app)
        self.exit_btn.pack(pady=10, padx=10, fill=tk.X)

        # Bind Escape key to exit
        self.root.bind('<Escape>', lambda event: self.quit_app())

        # Load brain image
        self.load_brain_image()

        # Check connection status
        self.check_connection()

    def apply_theme(self):
        theme = self.themes[self.theme]
        self.root.configure(bg=theme["bg"])
        self.left_frame.configure(bg=theme["panel"])
        self.canvas.configure(bg=theme["bg"])
        for widget in self.left_frame.winfo_children():
            if isinstance(widget, tk.Label):
                widget.configure(bg=theme["panel"], fg=theme["text"])
            elif isinstance(widget, tk.Entry):
                widget.configure(bg="white", fg=theme["text"], insertbackground=theme["text"])
            elif isinstance(widget, ttk.Button):
                style = ttk.Style()
                style.configure("Custom.TButton", background=theme["btn"], foreground=theme["text"])
                style.map("Custom.TButton", background=[("active", self.get_active_btn_color())])

    def get_active_btn_color(self):
        base = self.themes[self.theme]["btn"]
        if self.theme == "light":
            return "#C0C0C0"
        elif self.theme == "dark":
            return "#737373"
        else:  # red
            return "#FF3333"

    def load_brain_image(self):
        try:
            image = Image.open("brain_sagittal.png")
            image = image.resize((int(self.screen_width*5//6), self.screen_height), Image.Resampling.LANCZOS)
            self.brain_image = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.brain_image)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load brain image: {e}")

    def open_settings(self):
        settings_window = Toplevel(self.root)
        settings_window.title("Settings")
        settings_window.geometry("300x300")
        settings_window.configure(bg=self.themes[self.theme]["panel"])

        tk.Label(settings_window, text="Theme Selection:", bg=self.themes[self.theme]["panel"], fg=self.themes[self.theme]["text"], font=("Helvetica", 12, "bold")).pack(pady=10)
        theme_var = tk.StringVar(value=self.theme)
        tk.Radiobutton(settings_window, text="Light", variable=theme_var, value="light", bg=self.themes[self.theme]["panel"], fg=self.themes[self.theme]["text"], selectcolor=self.themes[self.theme]["btn"], command=lambda: self.set_theme("light")).pack(anchor=tk.W, padx=20)
        tk.Radiobutton(settings_window, text="Dark", variable=theme_var, value="dark", bg=self.themes[self.theme]["panel"], fg=self.themes[self.theme]["text"], selectcolor=self.themes[self.theme]["btn"], command=lambda: self.set_theme("dark")).pack(anchor=tk.W, padx=20)
        tk.Radiobutton(settings_window, text="Red", variable=theme_var, value="red", bg=self.themes[self.theme]["panel"], fg=self.themes[self.theme]["text"], selectcolor=self.themes[self.theme]["btn"], command=lambda: self.set_theme("red")).pack(anchor=tk.W, padx=20)

        tk.Button(settings_window, text="Close", command=settings_window.destroy, bg=self.themes[self.theme]["btn"], fg=self.themes[self.theme]["text"], font=("Helvetica", 12, "bold")).pack(pady=20)

    def set_theme(self, theme):
        self.theme = theme
        self.apply_theme()

    def toggle_education_mode(self):
        self.education_mode = not self.education_mode
        if self.education_mode:
            self.education_btn.configure(text="📚 Education Mode (On)")
        else:
            self.education_btn.configure(text="📚 Education Mode")

    def show_vision_info(self):
        if self.education_mode:
            self.show_education_info("Vision", [
                "• The optic nerve carries visual signals from the eye to the brain.",
                "• The thalamus relays signals as a relay center.",
                "• The occipital lobe processes visual information."
            ])
        else:
            self.send_command('V')

    def show_hearing_info(self):
        if self.education_mode:
            self.show_education_info("Hearing", [
                "• The auditory nerve carries sound signals from the ear to the brain.",
                "• The thalamus relays sound signals.",
                "• The temporal lobe processes auditory information."
            ])
        else:
            self.send_command('H')

    def show_speech_info(self):
        if self.education_mode:
            self.show_education_info("Speech", [
                "• Broca's area controls speech production.",
                "• Wernicke's area supports language comprehension and production.",
                "• Neural pathways connect these regions."
            ])
        else:
            self.send_command('S')

    def show_movement_info(self):
        if self.education_mode:
            self.show_education_info("Movement", [
                "• The motor cortex initiates body movements.",
                "• The parietal lobe processes sensory feedback.",
                "• The thalamus coordinates motor signals."
            ])
        else:
            self.send_command('M')

    def show_smell_info(self):
        if self.education_mode:
            self.show_education_info("Smell", [
                "• The olfactory bulb detects smell signals.",
                "• The piriform cortex processes smell information.",
                "• The thalamus is bypassed, with direct processing."
            ])
        else:
            self.send_command('O')

    def show_education_info(self, title, items):
        info_window = Toplevel(self.root)
        info_window.title("Education Mode")
        info_window.geometry("400x300")
        info_window.configure(bg=self.themes[self.theme]["panel"])

        tk.Label(info_window, text=title, bg=self.themes[self.theme]["panel"], fg=self.themes[self.theme]["text"], font=("Helvetica", 14, "bold")).pack(pady=10)
        for item in items:
            tk.Label(info_window, text=item, bg=self.themes[self.theme]["panel"], fg=self.themes[self.theme]["text"], font=("Helvetica", 12), justify=tk.LEFT).pack(anchor=tk.W, padx=20, pady=5)
        tk.Button(info_window, text="Close", command=info_window.destroy, bg=self.themes[self.theme]["btn"], fg=self.themes[self.theme]["text"], font=("Helvetica", 12, "bold")).pack(pady=10)

    def connect_arduino(self):
        port = self.port_entry.get()
        try:
            self.ser = serial.Serial(port, 9600, timeout=1)
            time.sleep(2)
            self.status_label.config(text="Status: Connected", fg=self.themes[self.theme]["text"])
            self.read_arduino_response()
        except Exception as e:
            messagebox.showerror("Error", f"Connection failed: {e}")
            self.status_label.config(text="Status: Not Connected", fg=self.themes[self.theme]["text"])

    def check_connection(self):
        if self.ser and not self.ser.is_open:
            self.status_label.config(text="Status: Not Connected")
            self.connect_arduino()
        self.root.after(5000, self.check_connection)

    def read_arduino_response(self):
        if self.ser and self.ser.in_waiting > 0:
            response = self.ser.readline().decode('utf-8').strip()
            if response and "Test Completed" in response:
                self.status_label.config(text="Status: Connected")
        self.root.after(100, self.read_arduino_response)

    def send_command(self, command):
        if self.ser and self.ser.is_open:
            try:
                self.ser.write((command + '\n').encode())
                return True
            except Exception as e:
                messagebox.showerror("Error", f"Command could not be sent: {e}")
                self.status_label.config(text="Status: Not Connected")
                return False
        else:
            messagebox.showwarning("Warning", "Connect to Arduino first!")
            return False

    def quit_app(self):
        if self.ser and self.ser.is_open:
            self.ser.close()
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = BrainControlApp(root)
    root.mainloop()