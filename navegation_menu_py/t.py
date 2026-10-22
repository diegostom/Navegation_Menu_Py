from navegation_menu_py import MenuConsola
import time
import random

def saludar():
    print("¡Hola! Estás usando navegación por flechas.")

def mostrar_sistema():
    print("Configuración del sistema: Todo funcionando en orden.")

import random

def game():
    print("Adivina el numero")
    print("Numero del 1 al 100, para salir escribir salir")
    
    # Generar el número secreto
    ns = random.randint(1, 100)
    
    while True:
        entrada = input("Numero: ").strip().lower()
        
        # 1. Verificar primero si quiere salir
        if entrada == "salir":
            print("Saliste del juego.")
            break
            
        # 2. Convertir el texto a número para poder compararlo
        try:
            plr = int(entrada)
        except ValueError:
            print("Por favor, introduce un número válido o escribe 'salir'.")
            continue
            
        # 3. Ahora las comparaciones funcionarán perfectamente sin romper el menú
        if plr > ns:
            print("El número secreto es menor.")
        elif plr < ns:
            print("El número secreto es mayor.")
        else:
            print("¡Felicidades! Adivinaste el número.")
            break


# ¡Aquí el programador puede personalizar su indicador favorito!
menu = MenuConsola("Panel de Control Interactivo", indicador="-")

menu.agregar_opcion("Mostrar Saludo", saludar)
menu.agregar_opcion("Ver Estado del Sistema", mostrar_sistema)
menu.agregar_opcion("Adivina el Numero", game)

menu.mostrar()
