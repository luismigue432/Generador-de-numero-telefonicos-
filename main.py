import random
import pyfiglet
from termcolor import colored
import time

# Variables y configuraciones
Bienvenida = "Numeros RD"
autor = colored("Luis Miguel de los Santos", "yellow")
n = colored("numeros", "red")

# Este script es con fines educativos, para que vean cómo las empresas generan números telefónicos
# Luis Miguel Santos, 2024

# Efecto de bienvenida
Bienvenida = pyfiglet.figlet_format(Bienvenida)
Bienvenida = colored(Bienvenida, "blue")

print(f"Autor: {autor}")
texto = Bienvenida
for char in texto:
    print(char, end='', flush=True)
    time.sleep(0.01)

print()

# Efecto de escritura en pantalla
texto = "Todo se guarda en: numeros.txt"
for char in texto:
    print(colored(char, "blue"), end='', flush=True)
    time.sleep(0.05)
print()

# Solicitud al usuario
Usuario = int(input(colored(f"Cuantos {n} quieres:  ", "blue")))

# Función para generar números
def numero():
    Reguion = random.choice(["829", "809", "849"])
    numeros_generado = random.randint(1234567, 8997689)
    numero_listos = f"{Reguion}{numeros_generado}"
    print(numero_listos)
    return numero_listos

# Guardar números generados en un archivo
with open("numeros.txt", "a") as s:
    for i in range(Usuario):
        s.write(str(numero()) + "\n")
