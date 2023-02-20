# imports

from tkinter import *
from tkinter import ttk

# Cores

Cor1 = "#0f0f0f"   # Preto
Cor2 = "#feffff"   # Branco
Cor3 = "#38576b"   # Azul
Cor4 = "#ECEFF1"   # Cinza
Cor5 = "#FFAB40"   # Laranja

# Calculadora

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=Cor1)

# Display da Calculadora

frame_tela = Frame(janela, width=235, height=50, bg=Cor3)
frame_tela.grid(row=0, column=0)

# Variavel que Guarda todos os valores

todos_valores = ""

# Criando Função


def entrar_valores(event):

    global todos_valores
    todos_valores = todos_valores + str(event)

    # Passando valor para Tela

    valor_texto.set(todos_valores)

# Função Para o Calcular

def calcular():
    resultado = eval(todos_valores)
    print(resultado)

    valor_texto.set(str(resultado))

# Função Limpa Tela, OBS: o Visualg Sempre teve

def limpar_tela():
    global todos_valores
    todos_valores =""
    valor_texto.set("")

# Corpo da Calculadora

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# Criando Labels

valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font='Ivy 18', bg=Cor3, fg=Cor2)
app_label.place(x=0, y=0)

# Botões Da Calculadora - Linha 1.

B_1 = Button(frame_corpo, command=limpar_tela, text="C", width=11, height=2, bg=Cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
B_1.place(x=0, y=0)

B_2 = Button(frame_corpo, command=lambda: entrar_valores('%'), text="%", width=5, height=2, bg=Cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
B_2.place(x=118, y=0)

B_3 = Button(frame_corpo, command=lambda: entrar_valores('/'), text="/", width=5, height=2, bg=Cor5, fg=Cor2, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
B_3.place(x=177, y=0)

# Botões Da Calculadora - Linha 2.

B_4 = Button(frame_corpo, command=lambda: entrar_valores('7'), text="7", width=5, height=2, bg=Cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
B_4.place(x=0, y=52)

B_5 = Button(frame_corpo, command=lambda: entrar_valores('8'), text="8", width=5, height=2, bg=Cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
B_5.place(x=59, y=52)

B_6 = Button(frame_corpo, command=lambda: entrar_valores('9'), text="9", width=5, height=2, bg=Cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
B_6.place(x=118, y=52)

B_7 = Button(frame_corpo, command=lambda: entrar_valores('*'), text="*", width=5, height=2, bg=Cor5, fg=Cor2, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
B_7.place(x=177, y=52)

# Botões Da Calculadora - Linha 3.

B_8 = Button(frame_corpo, command=lambda: entrar_valores('4'), text="4", width=5, height=2, bg=Cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
B_8.place(x=0, y=104)

B_9 = Button(frame_corpo, command=lambda: entrar_valores('5'), text="5", width=5, height=2, bg=Cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
B_9.place(x=59, y=104)

B_10 = Button(frame_corpo, command=lambda: entrar_valores('6'), text="6", width=5, height=2, bg=Cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
B_10.place(x=118, y=104)

B_11 = Button(frame_corpo, command=lambda: entrar_valores('-'), text="-", width=5, height=2, bg=Cor5, fg=Cor2, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
B_11.place(x=177, y=104)

# Botões da Calculadora - Linha 4.

B_12 = Button(frame_corpo, command=lambda: entrar_valores('1'), text="1", width=5, height=2, bg=Cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
B_12.place(x=0, y=156)

B_13 = Button(frame_corpo, command=lambda: entrar_valores('2'), text="2", width=5, height=2, bg=Cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
B_13.place(x=59, y=156)

B_14 = Button(frame_corpo, command=lambda: entrar_valores('3'), text="3", width=5, height=2, bg=Cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
B_14.place(x=118, y=156)

B_15 = Button(frame_corpo, command=lambda: entrar_valores('+'), text="+", width=5, height=2, bg=Cor5, fg=Cor2, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
B_15.place(x=177, y=156)

# Botões da Calculadora - Linha 5.

B_16 = Button(frame_corpo, command=lambda: entrar_valores('0'), text="0", width=11, height=2, bg=Cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
B_16.place(x=0, y=208)

B_17 = Button(frame_corpo, command=lambda: entrar_valores('.'), text=".", width=5, height=2, bg=Cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
B_17.place(x=118, y=208)

B_18 = Button(frame_corpo, command=calcular, text="=", width=5, height=2, bg=Cor5, fg=Cor2, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
B_18.place(x=177, y=208)


janela.mainloop()