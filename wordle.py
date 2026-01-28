import tkinter as tk
from tkinter import messagebox
import random

class WordleGUI:
    def __init__(self, master):
        self.master = master
        master.title("Wordle")

        self.lista_palabras = ["arbol", "perro", "gatos", "libro", "avion", "lunes", "canto", "verde", "salud", "cajas"]
        self.palabra_secreta = random.choice(self.lista_palabras).upper()
        self.intentos_maximos = 6
        self.intentos_realizados = 0
        self.intentos = []  # Lista para guardar los intentos

        # Crear etiquetas y campos de entrada para cada intento
        self.etiquetas = []
        self.campos_de_entrada = []
        for i in range(self.intentos_maximos):
            etiqueta = tk.Label(master, text=f"Intento {i+1}:")
            etiqueta.grid(row=i, column=0, padx=5, pady=5)
            self.etiquetas.append(etiqueta)

            campo_de_entrada = tk.Entry(master, width=6)
            campo_de_entrada.grid(row=i, column=1, padx=5, pady=5)
            self.campos_de_entrada.append(campo_de_entrada)

        # Botón para intentar adivinar
        self.boton_intentar = tk.Button(master, text="Intentar", command=self.evaluar_intento)
        self.boton_intentar.grid(row=self.intentos_maximos, column=0, columnspan=2, padx=5, pady=10)

    def evaluar_intento(self):
        """Evalúa el intento del usuario y actualiza la interfaz."""
        if self.intentos_realizados < self.intentos_maximos:
            intento = self.campos_de_entrada[self.intentos_realizados].get().upper()

            if len(intento) != 5 or not intento.isalpha():
                messagebox.showerror("Error", "Intento inválido. Debe ser una palabra de 5 letras.")
                return

            resultado = self.evaluar_intento_logica(intento, self.palabra_secreta)
            self.intentos.append(resultado)

            # Mostrar el resultado en la etiqueta
            self.etiquetas[self.intentos_realizados].config(text=f"Intento {self.intentos_realizados+1}: {resultado}")

            if intento == self.palabra_secreta:
                messagebox.showinfo("¡Felicidades!", f"Adivinaste la palabra en {self.intentos_realizados + 1} intentos.")
                self.boton_intentar.config(state=tk.DISABLED)  # Deshabilitar el botón
                return

            self.intentos_realizados += 1

            if self.intentos_realizados == self.intentos_maximos:
                messagebox.showinfo("¡Se acabaron los intentos!", f"La palabra secreta era: {self.palabra_secreta}")
                self.boton_intentar.config(state=tk.DISABLED)  # Deshabilitar el botón
        else:
            messagebox.showinfo("Juego terminado", "Ya no tienes más intentos.")

    def evaluar_intento_logica(self, intento, palabra_secreta):
        """Evalúa el intento del usuario y devuelve una cadena con el resultado."""
        resultado = ""
        for i in range(5):
            if intento[i] == palabra_secreta[i]:
                resultado += "[" + intento[i] + "]"  # Letra correcta en la posición correcta
            elif intento[i] in palabra_secreta:
                resultado += "(" + intento[i] + ")"  # Letra correcta pero en la posición incorrecta
            else:
                resultado += intento[i]  # Letra incorrecta
        return resultado

# Iniciar la interfaz gráfica
if __name__ == "__main__":
    root = tk.Tk()
    gui = WordleGUI(root)
    root.mainloop()