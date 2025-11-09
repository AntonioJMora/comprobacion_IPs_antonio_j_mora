import sys
def main():
    if len(sys.argv) < 2:
        print("Error: Se necesita una IP para ejecutar el codigo")
        print("Ejecutalo así: python comprobacion.py dirección_IP")
        sys.exit(1)

    ip = sys.argv[1]
    ip = ip.split(".")

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
                
        primer_num = int(ip[0])
        clase = ""
        if primer_num >= 1 and primer_num <= 126:
            clase = "A"
        elif primer_num >= 128 and primer_num <= 191:
            clase = "B"
        elif primer_num >= 192 and primer_num <= 223:
            clase = "C"
        elif primer_num >= 224 and primer_num <= 239:
            clase = "D"
        elif primer_num >= 240 and primer_num <= 255:
            clase = "E"

    if clase == "":
        print("Error: dirección IP no pertenece a ninguna clase conocida")
    else:
        print(f"La IP es válida y su clase es: {clase}")

if __name__ == "__main__":
    main()