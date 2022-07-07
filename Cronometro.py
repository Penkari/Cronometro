from tkinter import *

global inicio
global contador
global minuto
global condicao

condicao = False
inicio = minuto = contador = 0

janela = Tk()
janela.geometry('180x60')
janela.resizable(width=FALSE, height=FALSE)

def tempo():
    global condicao
    global contador
    global inicio
    global minuto

    if condicao == True:

        segundo = int(inicio)

        s = int(contador)

        if s % 60 == 0 and s > 0:
            contador -= 60
            minuto += 1

        s = segundo = str(s)

        texto['text'] = segundo
        texto1['text'] = minuto

        texto.after(1000, tempo)
        contador += 1
    else:
        pass

def interruptor():
    global condicao

    if condicao == False:
        condicao = True
        tempo()
        botao['text'] = 'Pausar'
    else:
        condicao = False
        botao['text'] = 'Começar'


texto = Label(janela, text='0', font=0)
texto.grid(column=1, row=0)

texto1 = Label(janela, text='0', font=0)
texto1.grid(column=0, row=0)

botao = Button(janela, text='Começar', command=interruptor)
botao.grid(column=1, row=1)

janela.mainloop()
