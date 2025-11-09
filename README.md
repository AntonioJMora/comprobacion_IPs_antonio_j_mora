# Comprobación de IPs.

## Datos personales.
- Nombre: Antonio Jesús Mora Cabeza
- Curso: 1º DAW A

## Descripción breve del módulo.
Desarrollo de un módulo en python que reciba una dirección IP del usuario y la compruebe, diciéndole si la IP es válida y en caso de serlo, darle también la clase que es según el primer octeto.

## Sintaxis de uso.
Para poder ejecutarlo será de la siguiente manera:
```bash
python comprobacion.py dirección_IP

```
Por ejemplo:

- En caso de estar bien:
```bash
python .\comprobacion.py 192.168.5.4
La IP es válida y su clase es: C
```
- Si no se le pasa ninguna IP:
```bash
python .\comprobacion.py 
Error: Se necesita una IP para ejecutar el codigo
Ejecutalo así: python comprobacion.py dirección_IP
```
- Si la IP dada no tiene 4 octetos
```bash
python .\comprobacion.py 191.232.23 
IP inválida: debe tener 4 octetos
```
- Si no todos son letras
```bash
python .\comprobacion.py hola.192.123.12
Los caracteres solo pueden ser números y .
Ejemplo: 192.168.1.2
```

## Reglas de validación y clasificación por clases.
### Reglas de Validacion:
|Validacion| Condición | Mensaje de error |
|----------| ----------|------------------|
| Cantidad de octetos | Tiene que haber 4 octetos | IP inválida: debe tener 4 octetos |
| Formato | Solo pueden haber números y puntos | Los caracteres solo pueden ser números y . Ejemplo: 192.168.1.2|
| Rango de IP | Los numeros deben estar entre 0 y 255 | La IP es inválida, se sale del rango de IPs. Consejo: cada octeto debe estar entre 0 y 255" |
|Argumentos | Deben estar el nombre del codigo y la IP | Error: Se necesita una IP para ejecutar el codigoEjecutalo así: python comprobacion.py dirección_IP |

### Clasificación por clases:
|Clase | Rango de los octetos | Descripción |
|------|----------------------|-------------|
|A| 1 - 126 | Destinadas a grandes redes |
|B| 128 - 191 | Utilizadas por organizaciones de tamaño mediano |
| C | 192 - 223 | Se utilizan comúnmente en redes más pequeñas |
| D | 224 - 239 | Se reservan para fines especiales y se utilizan principalmente para la multidifusión |
| E | 240 - 255 | Se reservan para fines especiales y no se utilizan para la asignación normal de direcciones IP |

## Casos de prueba
| IP de entrada | Resultado | Salida |
|---------------|-------------------|-------------|
| 10.0.0.1| Clase A | La IP es válida y su clase es: A |
| 172.16.0.5 | Clase B | La IP es válida y su clase es: B |
| 192.168.1.1 | Clase C | La IP es válida y su clase es: C |
| 225.10.10.10 | Clase D | La IP es válida y su clase es: D |
| 245.1.1.1 | Clase E | La IP es válida y su clase es: E |
| 127.0.0.1 | Loopback | Error: dirección IP no pertenece a ninguna clase conocida |
| 300.1.1.1 | Fuera de rango | La IP es inválida, se sale del rango de IPs.|
| 192.168.1| Formato incorrecto | IP inválida: debe tener 4 octetos |
| abc.def.ghi.jkl | No se permiten letras | Los caracteres solo pueden ser números y . |
| (sin argumentos)  | Falta de IP | Error: Se necesita una IP para ejecutar el codigo |

## Requisitos
### Software
- Python 3.10 o superior

### Herramientas necesarias
- Terminal de comandos para ejecutar el script

### A tener en cuenta
- Ejecutar el script desde la carpeta donde se encuentre el archivo `.py` o usar la ruta hasta el archivo
