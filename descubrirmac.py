import sys
import subprocess
import platform

def obtener_mac(ip):
    """Obtener la mac de la tabla arp"""
    mac = ""
    #El try se usa para que si falla el comando, no deje de funcionar el programa
    try:
        # En comando, se ejecuta "arp -a" y guarda la salida en texto
        comando = subprocess.check_output("arp -a", shell=True, text=True)
        for linea in comando.splitlines():
            if ip in linea:
                datos = linea.split()
                for dato in datos:
                    if "-" in dato or ":" in dato:
                        mac = dato
        return mac
    except:
        return None

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
        else:
            hacerping = subprocess.Popen(["ping", "-c", "2", ip_normal], stdout=subprocess.DEVNULL, stderr= subprocess.DEVNULL)

        hacerping.wait()

        if hacerping.returncode == 0:
            print(f"{ip_normal} está encendida")

        else:
            print(f"{ip_normal} está apagada")

        #Obtener la mac
        mac = obtener_mac(ip_normal)
        if mac:
            print(f"La dirección MAC de {ip_normal} es: {mac}")
        else:
            print(f"No se pudo obtener la MAC de {ip_normal}. Asegurese de estar en la misma red.")

if __name__ == "__main__":
    main()
