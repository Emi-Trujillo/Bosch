# Control PWM Raspberry Pi 4 con Tkinter

Este proyecto permite controlar el **PWM de un pin GPIO en la Raspberry Pi 4** mediante una interfaz gráfica con **Tkinter**.  
Incluye dos modos de funcionamiento:

- **Modo Tec** → Control sencillo con dos botones:  
  - **Encender (100%)**  
  - **Apagar (0%)**  

- **Modo Bosch** → Control avanzado con una barra deslizante que ajusta el ciclo de trabajo del PWM de 0% a 100%.  

La aplicación cuenta con una interfaz estética y fácil de entender, pensada para pruebas rápidas y demostraciones.

---

## 📂 Archivos

- `pwm_control.py` → versión para Raspberry Pi (usa `RPi.GPIO`)  
- `pwm_control_sim.py` → versión de simulación para PC (no requiere hardware)  

---

## 🔧 Requisitos

### Raspberry Pi
- Python 3  
- Tkinter  
- RPi.GPIO  

Instalación en Raspberry Pi:
```bash
sudo apt update
sudo apt install python3 python3-tk python3-rpi.gpio
