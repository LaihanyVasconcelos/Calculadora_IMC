from tkinter import *
from tkinter import ttk 

#cores
cor1 ='#ffffff' #branco
cor2 ='#000000' #preto
cor3 ='#9703ad' #roxo


#janelas
janela = Tk()
janela.title('Calculadora de IMC')
janela.geometry('295x230')
janela.configure(bg=cor1)
janela.resizable(width=FALSE, height=FALSE) #para as dimensões da janela não ser alterada

#criando frames (para dividir a janela em duas partes)
#FRAME CIMA
frame_cima = Frame(janela, width=295, height=50, bg=cor1, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)
#FRAME BAIXO
frame_baixo = Frame(janela, width=295, height=180, bg=cor1, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

#configurando frame_cima
app_nome = Label(frame_cima, text="Calculadora de IMC", width=23, height=1, padx=0, relief='flat', anchor='center', font=('Ivy, 16 bold'), bg=cor1, fg=cor2)
#posicionar esse mesmo label no frame_cima
app_nome.place(x=0, y=0)

#criando função calcular
def calcular():
    #parte lógica
    #criando variaveis de peso, altura e imc

    peso = float(endry_peso.get())
    altura = float(entry_altura.get())

    imc = peso / altura ** 2

    resultado = imc
                #menor
    if resultado < 18.5:
        label_resultado_texto ['text'] = 'Seu IMC é: Abaixo do peso'

    elif resultado >= 18.5 and resultado < 25:
        label_resultado_texto ['text'] = 'Seu IMC é: Normal'

    elif resultado >= 25 and resultado < 30:
        label_resultado_texto ['text'] = 'Seu IMC é Sobrepeso'

    else:
        label_resultado_texto['text'] = 'Seu IMC é: Obesidade'

    #formando o resultado
    label_resultado['text'] = '{:.2f}'.format(resultado)


app_linha = Label(frame_cima, text="", width=400, height=1, padx=0, relief='flat', anchor='center', font=('Ivy, 1 '), bg=cor3, fg=cor1)
app_linha.place(x=0, y=35)

#configurando frame_baixo
#peso
label_peso = Label(frame_baixo, text="Insira seu peso", height=1, padx=0, relief='flat', anchor='center', font=('Ivy, 10 bold'), bg=cor1, fg=cor2)
label_peso.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)

endry_peso = Entry(frame_baixo, width=5, relief='solid', font=('Ivy, 10 bold'),justify='center')
endry_peso.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3)

#altura
label_altura = Label(frame_baixo, text="Insira sua altura", height=1, padx=0, relief='flat', anchor='center', font=('Ivy, 10 bold'), bg=cor1, fg=cor2)
label_altura.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)

entry_altura = Entry(frame_baixo, width=5, relief='solid', font=('Ivy, 10 bold'),justify='center')
entry_altura.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)

label_resultado = Label(frame_baixo, text="---", width=5, height=1, padx=6, pady=12, relief='flat', anchor='center', font=('Ivy, 24 bold'), bg=cor3, fg=cor1)
label_resultado.place(x=175, y=10)

#criando label de sair o resuldado escrito

label_resultado_texto = Label(frame_baixo, text="", width=37, height=1, padx=0, pady=12, relief='flat', anchor='center', font=('Ivy, 10 bold'), bg=cor1, fg=cor2)
label_resultado_texto.place(x=0, y=90)

b_calcular = Button(frame_baixo, command=calcular, text="Calcular", width=34, height=1, overrelief=SOLID, relief='raised', anchor='center', font=('Ivy, 10 bold'), bg=cor3, fg=cor1)
b_calcular.grid(row=4, column=0, sticky=NSEW, pady=60, padx=5, columnspan=30)




janela.mainloop()