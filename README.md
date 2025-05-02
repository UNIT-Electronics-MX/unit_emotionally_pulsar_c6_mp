## 📦 Unit Emotionally — PULSAR C6


Unit Emotionally is a MicroPython-based interactive project that combines the **Pulsar C6** development board with an OLED display and an MPU6050 motion sensor to create a cute emotional face that reacts to movement.

When moved gently or harshly, the character reacts with different expressions (happy, angry, sleepy, surprised), shown in real time on a 128x64 OLED screen.
<div style="width:50%;">
    <img src="/hardware/resources/AR4606_UNIT_Pulsar_Nano_C6_ESP32C6.jpg" alt="AR4606 UNIT Pulsar Nano C6 ESP32C6" style="width:100%; height:auto;" />
</div>

### 🔧 Materials

| Item | Link |
|------|------|
| OLED 128x64 I2C Display | [SSD1306 0.96"](https://uelectronics.com/producto/display-oled-azul-y-blanco-128x64-0-96-i2c-ssd1306/) |
| Qwiic I2C Bus Expander | [Unit Qwiic I2C](https://uelectronics.com/producto/unit-expansor-i2c-con-bus-qwiic/) |
| JST-SH 1.0mm Connectors | [1mm SH with Cable](https://uelectronics.com/producto/conectores-sh1-0mm-con-cable-28-awg-15cm/) |
| MPU6050 IMU (2x) | [6DOF Sensor](https://uelectronics.com/producto/imu-mpu6050-6-grados-de-libertad/) |
| PULSAR C6 Dev Board | [ESP32-C6 Nano](https://unit-electronics-mx.github.io/wiki_uelectronics/docs/Development_boards/Nano/nano_c6) |
| LiPo Battery 3.7V | [400mAh 602035](https://uelectronics.com/producto/bateria-lipo-3-7v-400mah-602035/) |


### 📂 Repository Structure

```
unit_emotionally/
├── software/
    ├── main.py          # Main application logic
    ├── mpu6050.py       # Driver for MPU6050
├── README.md
└── LICENSE
```


### Installation 

1. **Flash MicroPython** on your PULSAR C6 (ESP32-C6)
2. Copy the following files to your board using [ampy](https://github.com/scientifichackers/ampy) or `mpremote`:
   ```bash
   mpremote cp main.py :main.py
   mpremote cp mpu6050.py :mpu6050.py
   ```
3. Connect your OLED and MPU6050 via Qwiic or JST-SH 1.0mm using I2C (GPIO6=SDA, GPIO7=SCL)



### 🎬 Example

After powering the board:

- Subtle movement → 😊
- Fast motion → 😠
- Idle → 💤 with animated "ZzZ"
- Sudden tilt → 😮

OLED will display cute faces based on the motion detected by the MPU6050!


### 📝 License

This project is licensed under the [MIT License](LICENSE).
