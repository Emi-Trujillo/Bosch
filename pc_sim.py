import tkinter as tk
from tkinter import ttk

# ------------------- SIMULACIÓN PWM -------------------
class SimuladorPWM:
    def __init__(self, pin, frecuencia):
        self.pin = pin
        self.frecuencia = frecuencia
        self.duty = 0
        print(f"[SIM] PWM inicializado en pin {pin} a {frecuencia} Hz")

    def start(self, duty):
        self.duty = duty
        print(f"[SIM] PWM iniciado con duty cycle = {duty}%")

    def ChangeDutyCycle(self, duty):
        self.duty = float(duty)
        print(f"[SIM] Duty cycle cambiado a {self.duty:.1f}%")

    def stop(self):
        print("[SIM] PWM detenido")

# Crear simulador
pwm = SimuladorPWM(pin=18, frecuencia=1000)
pwm.start(0)

# ------------------- FUNCIONES -------------------
def set_pwm(value):
    """Configura el ciclo de trabajo (duty cycle) del PWM"""
    pwm.ChangeDutyCycle(value)

def modo_tec_on():
    """Encender al 100%"""
    set_pwm(100)

def modo_tec_off():
    """Apagar (0%)"""
    set_pwm(0)

def actualizar_bosch(valor):
    """Actualiza PWM con el valor del slider"""
    set_pwm(valor)

def cambiar_modo():
    """Cambia entre los modos de control"""
    modo = modo_selector.get()
    if modo == "Tec":
        frame_bosch.pack_forget()
        frame_tec.pack(pady=20)
    else:
        frame_tec.pack_forget()
        frame_bosch.pack(pady=20)

def cerrar():
    """Cierra la app"""
    pwm.stop()
    root.destroy()

# ------------------- INTERFAZ TKINTER -------------------
root = tk.Tk()
root.title("Simulación Control PWM Raspberry Pi 4")
root.geometry("400x300")
root.configure(bg="#1e1e2f")

# Estilos
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=10)
style.configure("TLabel", font=("Arial", 12), foreground="white", background="#1e1e2f")

# Selector de modo
ttk.Label(root, text="Selecciona el modo:").pack(pady=10)
modo_selector = ttk.Combobox(root, values=["Tec", "Bosch"], state="readonly")
modo_selector.current(0)
modo_selector.pack()
modo_selector.bind("<<ComboboxSelected>>", lambda e: cambiar_modo())

# Frame Modo Tec
frame_tec = tk.Frame(root, bg="#1e1e2f")
ttk.Label(frame_tec, text="Modo Tec: Encendido / Apagado").pack(pady=10)
ttk.Button(frame_tec, text="Encender (100%)", command=modo_tec_on).pack(pady=5)
ttk.Button(frame_tec, text="Apagar (0%)", command=modo_tec_off).pack(pady=5)
frame_tec.pack(pady=20)

# Frame Modo Bosch
frame_bosch = tk.Frame(root, bg="#1e1e2f")
ttk.Label(frame_bosch, text="Modo Bosch: Control PWM").pack(pady=10)
slider = ttk.Scale(frame_bosch, from_=0, to=100, orient="horizontal", command=actualizar_bosch)
slider.pack(pady=20, fill="x", padx=30)

# Botón salir
ttk.Button(root, text="Salir", command=cerrar).pack(side="bottom", pady=10)

# Inicia en modo Tec
cambiar_modo()

root.mainloop()
