import time
import serial

PORT = "/dev/tty.usbmodem2086347857411"   # troque para a porta do transmissor (ex.: "COM5" no Windows)
BAUD = 115_200          # mantenha no mesmo valor configurado no firmware

def send_command(ser, robot_id, vx, vy, vtheta, kicker=0, theta=None, theta_target=None):
    theta_str = "null" if theta is None else str(theta)
    theta_target_str = "null" if theta_target is None else str(theta_target)
    line = f"{robot_id},{vx},{vy},{vtheta},{kicker},{theta_str},{theta_target_str}\n"
    ser.write(line.encode("ascii"))
    ser.flush()

def main():
    with serial.Serial(PORT, BAUD, timeout=1) as ser:
        time.sleep(2)  # dá tempo para o dispositivo enumerar/resetar

        print("Enviando sequência de comandos...")
        for step in range(20):
            send_command(
                ser,
                robot_id=1,           # ID do robô
                vx=200 + step * 10,   # acelera um pouco a cada envio
                vy=0,
                vtheta=0,
                kicker=step % 2,
                theta=None,
                theta_target=None
            )
            time.sleep(0.1)          # 100 ms entre pacotes

        print("Sequência concluída.")

if __name__ == "__main__":
    main()
