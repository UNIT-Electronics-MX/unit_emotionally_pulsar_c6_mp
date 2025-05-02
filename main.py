from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from mpu6050 import MPU6050
import time
import math
import framebuf

# Añade esto fuera de la función para inicializar una variable de animación
z_offset = 0
# Configuración OLED
WIDTH = 128
HEIGHT = 64
i2c = I2C(0, scl=Pin(7), sda=Pin(6))
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Inicializar MPU6050
mpu = MPU6050(i2c)

# Función para dibujar círculos rellenados
def fill_circle(oled, x0, y0, r, color):
    for y in range(-r, r):
        for x in range(-r, r):
            if x*x + y*y <= r*r:
                oled.pixel(x0 + x, y0 + y, color)

# Función para dibujar arco
def arc(oled, x0, y0, r, start_angle, end_angle, color):
    for a in range(start_angle, end_angle):
        angle = math.radians(a)
        x = int(x0 + r * math.cos(angle))
        y = int(y0 + r * math.sin(angle))
        oled.pixel(x, y, color)

# Adjuntar funciones al objeto OLED
SSD1306_I2C.fill_circle = fill_circle
SSD1306_I2C.arc = arc

# Función para dibujar emociones
def draw_emotion(emotion):
    global z_offset
    oled.fill(0)

    oled.fill(0)
    
    if emotion == "happy":
        fill_circle(oled, 40, 32, 15, 1)
        fill_circle(oled, 88, 32, 15, 1)
        fill_circle(oled, 40, 32, 5, 0)
        fill_circle(oled, 88, 32, 5, 0)
        oled.pixel(35, 25, 0)
        oled.pixel(83, 25, 0)
        oled.arc(64, 48, 10, 0, 180, 1)

    elif emotion == "sad":
        fill_circle(oled, 40, 36, 12, 1)
        fill_circle(oled, 88, 36, 12, 1)
        fill_circle(oled, 40, 40, 4, 0)
        fill_circle(oled, 88, 40, 4, 0)
        oled.line(28, 20, 52, 28, 1)
        oled.line(76, 28, 100, 20, 1)
        oled.arc(64, 54, 10, 180, 360, 1)

    elif emotion == "angry":
        fill_circle(oled, 40, 32, 12, 1)
        fill_circle(oled, 88, 32, 12, 1)
        fill_circle(oled, 40, 28, 5, 0)
        fill_circle(oled, 88, 28, 5, 0)
        oled.line(28, 20, 52, 24, 1)
        oled.line(76, 24, 100, 20, 1)
        oled.hline(54, 50, 20, 1)

    elif emotion == "surprised":
        fill_circle(oled, 40, 32, 18, 1)
        fill_circle(oled, 88, 32, 18, 1)
        fill_circle(oled, 40, 32, 6, 0)
        fill_circle(oled, 88, 32, 6, 0)
        oled.rect(58, 48, 10, 10, 1)

    elif emotion == "sleepy":
        # Ojos cerrados
        oled.hline(28, 32, 24, 1)
        oled.hline(76, 32, 24, 1)
        # Boca neutra
        oled.hline(54, 50, 20, 1)

        # Animación de "Zzz"
        oled.text("Z", 100, 20 - z_offset, 1)
        oled.text("z", 104, 10 - z_offset // 2, 1)

        # Reinicia animación en bucle
        z_offset += 1
        if z_offset > 30:
            z_offset = 0
            
    oled.show()

# Inicialización del último valor de aceleración
last_magnitude = 0

# Bucle principal
while True:
    acc_x, acc_y, acc_z = mpu.read_accel()
    magnitude = math.sqrt(acc_x**2 + acc_y**2 + acc_z**2)
    delta = abs(magnitude - last_magnitude)
    last_magnitude = magnitude

    if delta > 1.2:
        emotion = "angry"       # Movimiento brusco
    elif delta > 0.6:
        emotion = "surprised"   # Movimiento moderado
    elif delta < 0.1:
        emotion = "sleepy"      # Muy quieto
    else:
        emotion = "happy"       # Movimiento leve

    draw_emotion(emotion)
    time.sleep(1)

