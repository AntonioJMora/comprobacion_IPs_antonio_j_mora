# Descubrir la MAC de un dispositivo

## Datos personales
- Nombre: Antonio Jesús Mora Cabeza
- Curso: 1º DAW A

## Descripción breve del módulo.
Desarrollo de un modulo en python que compruebe que la IP sea válida, le haga ping, y además nos dé la MAC del dispositivo en caso de estar en la misma red

## Sintaxis de uso.
Para poder ejecutarlo será de la siguiente manera:
```bash
python descubrirmac.py dirección_IP

```
En caso de que funcione mostrará algo como lo siguiente:
```bash
python .\descubrirmac.py 192.168.1.1
192.168.1.1 está encendida
La dirección MAC de 192.168.1.1 es: 48-ed-e6-79-0a-10
```

Y en caso de que no mostrará lo siguiente:
```bash
python .\descubrirmac.py 172.16.2.3
172.16.2.3 está apagada
No se pudo obtener la MAC de 172.16.2.3. Asegurese de estar en la misma red.
```

## Requisitos
### Software
- Python 3.10 o superior

### Herramientas necesarias
- Terminal de comandos para ejecutar el script

### A tener en cuenta
- Ejecutar el script desde la carpeta donde se encuentre el archivo `.py` o usar la ruta hasta el archivo
