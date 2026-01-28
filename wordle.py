import random

posibles_palabras= ['arbol','plata', 'perros', 'gatos','barco']

posibles_palabras= random.choice (posibles_palabras).upper #---> la funcion ramdon.choise para elegir una palabra al azar y .upper para transformar las palabras a mausculas

intentos_maximos= 6 #----> definimos con una variable los intentos maximos
intentos_reaizados= 0 #----> establecemos el contador de intentos

while intentos_reaizados < intentos_maximos :  #----> creamos el bucle para dar logica al juego
    
    intentos= input('Ingrese una palabra de 5 letras').upper()

    if len(intentos) != 5 or not intentos.isalpha():
        print("Intento inválido. Debe ser una palabra de 5 letras.")
        continue  # Vuelve al inicio del bucle
