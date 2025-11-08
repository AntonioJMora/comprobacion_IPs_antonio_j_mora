import sys
import subprocess
import platform
def main():
    ip_normal = sys.argv[1]
    ip = ip_normal.split(".")

    if len(ip) != 4:
        print("IP inválida: debe tener 4 octetos")
        return
    else:
        for parte in ip:
            if not parte.isdigit():
                print("Los caracteres solo pueden ser números y .")
                print("Ejemplo: 192.168.1.2")
                return
            else:
                parte = int(parte)
                if parte < 0 or parte > 255:
                    print("La IP es inválida, se sale del rango de IPs.")
                    print("Consejo: cada octeto debe estar entre 0 y 255")
                    return
        plataforma = platform.system()

        if plataforma == "Windows":
            hacerping = subprocess.Popen(["ping", "-n", "2", ip_normal], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            while hacerping.poll() == None:
                print(".")
        else:
            hacerping = subprocess.Popen(["ping", "-c", "2", ip_normal], stdout=subprocess.DEVNULL, stderr= subprocess.DEVNULL)

        hacerping.wait()

        if hacerping.returncode == 0:
            print(f"{ip_normal} está encendida")
        else:
            print(f"{ip_normal} está apagada")

if __name__ == "__main__":
    main()
