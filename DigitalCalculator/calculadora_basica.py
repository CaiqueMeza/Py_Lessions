from tkinter import *
# from tkinter import ttk #uma parte da biblioteca que tem recursos mais avançados

#cores
cor1 = "#000000" #preto
cor2 = "#023f52" #azul escuro | visor
cor3 = "#dfe6e8" #cinza escuro | corpo
cor4 = "#0a2730" #azul escuro | botões
cor5 = "#e3a62b" #laranja | botões
cor6 = "#ffffff" #branco | caracteres

#config janela principal
janela = Tk()
janela.title("Calculadora Básica")
janela.geometry("295x346") #largura e altura padrão
janela.config(bg=cor1)

#config visor
frame_visor = Frame(janela, width='285px', height='50px', bg=cor2)
frame_visor.grid(row=0, column=0)

#config corpo
frame_corpo = Frame(janela, width='285px', height='318px', bg=cor3)
frame_corpo.grid(row=1, column=0)

#criando label
valor_texto = StringVar()
app_label = Label(frame_visor, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT,
                  font=('Ivy 18 bold'), bg=cor2, fg=cor6)
app_label.place(x=27,y=9)

#variável todos valores
todos_valores = ''

#criando função de calculo
# def entrar_valores(event):
#     global todos_valores
#     todos_valores = todos_valores + str(event)
   
#     valor_texto.set(todos_valores)

def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
   
    valor_texto.set(todos_valores)

def calcular():
    try:
        global todos_valores
        todos_valores = todos_valores.replace('x', '*')
        todos_valores = todos_valores.replace('÷', '/')
        if '**' in todos_valores:
            valor_texto.set('Equação Inválida')
        if '*-+' in todos_valores:
            valor_texto.set('Equação Inválida')
        if '*+-' in todos_valores:
            valor_texto.set('Equação Inválida')
        else:
            resultado = eval(todos_valores)
            valor_texto.set(str(resultado))
            todos_valores = str(resultado)
    except SyntaxError:
        valor_texto.set('Equação Inválida')
    except ZeroDivisionError:
        valor_texto.set('Impos. dividir por 0')

def limpar_tela():
    global todos_valores
    todos_valores =""
    valor_texto.set("")


#botões
b_clean = Button(frame_corpo, text="C", width=10, height=2, bg=cor4, fg=cor6, 
                 font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE,
                 command=limpar_tela)
b_clean.place(x='29px', y='3px')

b_percentual = Button(frame_corpo, text="%", width=5, height=2, bg=cor4, fg=cor6, 
                      font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, 
                      command= lambda: entrar_valores('%'))
b_percentual.place(x='119px', y='3px')

b_divisao = Button(frame_corpo, text="/", width=5, height=2, bg=cor5, fg=cor6, 
                   font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE,
                   command= lambda: entrar_valores('/'))
b_divisao.place(x='166px', y='3px')

b_mult = Button(frame_corpo, text="*", width=5, height=2, bg=cor5, fg=cor6, 
                   font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE,
                   command= lambda: entrar_valores('*'))
b_mult.place(x='166px', y='44px')

b_menos = Button(frame_corpo, text="-", width=5, height=2, bg=cor5, fg=cor6, 
                   font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE,
                   command= lambda: entrar_valores('-'))
b_menos.place(x='166px', y='85px')

b_mais = Button(frame_corpo, text="+", width=5, height=2, bg=cor5, fg=cor6, 
                   font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE,
                   command= lambda: entrar_valores('+'))
b_mais.place(x='166px', y='126px')

b_7 = Button(frame_corpo, text="7", width=5, height=2, bg=cor4, fg=cor6, 
                      font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE,
                      command= lambda: entrar_valores('7'))
b_7.place(x='23px', y='44px')

b_8 = Button(frame_corpo, text="8", width=5, height=2, bg=cor4, fg=cor6, 
                      font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE,
                      command= lambda: entrar_valores('8'))
b_8.place(x='71px', y='44px')

b_9 = Button(frame_corpo, text="9", width=5, height=2, bg=cor4, fg=cor6, 
                      font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE,
                      command= lambda: entrar_valores('9'))
b_9.place(x='119px', y='44px')

b_4 = Button(frame_corpo, text="4", width=5, height=2, bg=cor4, fg=cor6, 
                      font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE,
                      command= lambda: entrar_valores('4'))
b_4.place(x='23px', y='85px')

b_5 = Button(frame_corpo, text="5", width=5, height=2, bg=cor4, fg=cor6, 
                      font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE,
                      command= lambda: entrar_valores('5'))
b_5.place(x='71px', y='85px')

b_6 = Button(frame_corpo, text="6", width=5, height=2, bg=cor4, fg=cor6, 
                      font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE,
                      command= lambda: entrar_valores('6'))
b_6.place(x='119px', y='85px')

b_1 = Button(frame_corpo, text="1", width=5, height=2, bg=cor4, fg=cor6, 
                      font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE,
                      command= lambda: entrar_valores('1'))
b_1.place(x='23px', y='126px')

b_2 = Button(frame_corpo, text="2", width=5, height=2, bg=cor4, fg=cor6, 
                      font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE,
                      command= lambda: entrar_valores('2'))
b_2.place(x='71px', y='126px')

b_3 = Button(frame_corpo, text="3", width=5, height=2, bg=cor4, fg=cor6, 
                      font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE,
                      command= lambda: entrar_valores('3'))
b_3.place(x='119px', y='126px')

b_0 = Button(frame_corpo, text="0", width=10, height=2, bg=cor4, fg=cor6, 
                 font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE,
                 command= lambda: entrar_valores('0'))
b_0.place(x='29px', y='167px')

b_dot = Button(frame_corpo, text=".", width=5, height=2, bg=cor4, fg=cor6, 
                      font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE,
                      command= lambda: entrar_valores('.'))
b_dot.place(x='119px', y='167px')

b_mais = Button(frame_corpo, text="=", width=5, height=2, bg=cor5, fg=cor6, 
                   font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE,
                   command= calcular)
b_mais.place(x='166px', y='167px')



janela.mainloop() #abrir/fechar janela