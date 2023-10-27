from tkinter import *
import ast

if __name__ == '__main__':
    ventana = Tk()
    ventana.title("Calculadora")

# Entrada
ent_texto = Entry(ventana, font = ("Calibri 20"))
ent_texto.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5)

# Funciones
def click_boton(valor):
    ent_texto.insert(END, valor)

def borrar():
    ent_texto.delete(0, END)

def hacer_operacion():
    ecuacion = ent_texto.get()
    try:
        resultado = eval(ecuacion)
        ent_texto.delete(0, END)
        ent_texto.insert(0 , resultado)
    except SyntaxError:
        ent_texto.delete(0, END)
        ent_texto.insert(0,"ERROR DE SINTAXIS")

# Botones
    # Números
boton1 = Button(ventana, text = "1", width = 5, height = 2, command = lambda: click_boton(1))
boton2= Button(ventana, text = "2", width = 5, height = 2, command = lambda: click_boton(2))
boton3 = Button(ventana, text = "3", width = 5, height = 2, command = lambda: click_boton(3))
boton4 = Button(ventana, text = "4", width = 5, height = 2, command = lambda: click_boton(4))
boton5 = Button(ventana, text = "5", width = 5, height = 2, command = lambda: click_boton(5))
boton6 = Button(ventana, text = "6", width = 5, height = 2, command = lambda: click_boton(6))
boton7 = Button(ventana, text = "7", width = 5, height = 2, command = lambda: click_boton(7))
boton8 = Button(ventana, text = "8", width = 5, height = 2, command = lambda: click_boton(8))
boton9 = Button(ventana, text = "9", width = 5, height = 2, command = lambda: click_boton(9))
boton0 = Button(ventana, text = "0", width = 15, height = 2, command = lambda: click_boton(0))
    # Acciones
boton_borrar = Button(ventana, text = "AC", width = 5, height = 2, command = lambda: borrar()) # llama a la funcion click_boton sin argumentos
boton_parentesis1 = Button(ventana, text = "(", width = 5, height = 2, command = lambda: click_boton("("))
boton_parentesis2 = Button(ventana, text = ")", width = 5, height = 2, command = lambda: click_boton(")"))
boton_punto = Button(ventana, text = ".", width = 5, height = 2, command = lambda: click_boton("."))
    # Operaciones
boton_div = Button(ventana, text = "/", width = 5, height = 2, command = lambda: click_boton("/")) # llama a la función click_boton con el argumento "/"
boton_mult = Button(ventana, text = "x", width = 5, height = 2, command = lambda: click_boton("*")) # llama a la función click_boton con el argumento "*"
boton_suma = Button(ventana, text = "+", width = 5, height = 2, command = lambda: click_boton("+")) # llama a la función click_boton con el argumento "+"
boton_resta = Button(ventana, text = "-", width = 5, height = 2, command = lambda: click_boton("-")) # llama a la función click_boton con el argumento "-"
boton_igual = Button(ventana, text = "=", width = 5, height = 2, command = lambda: hacer_operacion()) # llama a la función hacer_operacion sin argumentos

# Agregar los Botones a la pantalla
    # Fila 1
boton_borrar.grid(row = 1, column = 0, padx = 5, pady = 5)
boton_parentesis1.grid(row = 1, column = 1, padx = 5, pady = 5)
boton_parentesis2.grid(row = 1, column = 2, padx = 5, pady = 5)
boton_div.grid(row = 1, column = 3, padx = 5, pady = 5)
    # Fila 2
boton7.grid(row = 2, column = 0, padx = 5, pady = 5)
boton8.grid(row = 2, column = 1, padx = 5, pady = 5)
boton9.grid(row = 2, column = 2, padx = 5, pady = 5)
boton_mult.grid(row = 2, column = 3, padx = 5, pady = 5)
    # Fila 3
boton4.grid(row = 3, column = 0, padx = 5, pady = 5)
boton5.grid(row = 3, column = 1, padx = 5, pady = 5)
boton6.grid(row = 3, column = 2, padx = 5, pady = 5)
boton_resta.grid(row = 3, column = 3, padx = 5, pady = 5)
    # Fila 4
boton1.grid(row = 4, column = 0, padx = 5, pady = 5)
boton2.grid(row = 4, column = 1, padx = 5, pady = 5)
boton3.grid(row = 4, column = 2, padx = 5, pady = 5)
boton_suma.grid(row = 4, column = 3, padx = 5, pady = 5)
    # Fila 5
boton0.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)
boton_punto.grid(row = 5, column = 2, padx = 5, pady = 5)
boton_igual.grid(row = 5, column = 3, padx = 5, pady = 5)


ventana.mainloop()