import tkinter as tk
from tkinter import messagebox

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        return False
    
    def sacar(self, valor):
        if valor > self.saldo:
            return False, "Saldo insuficiente!"
        elif valor <= 0:
            return False, "Valor inválido para saque!"
        else:
            self.saldo -= valor
            return True, "Saque realizado com sucesso!"
    
    def exibir_saldo(self):
        return f"Saldo de {self.titular}: R${self.saldo:.2f}"

# Funções para integração com Tkinter
def criar_conta():
    nome = entry_titular.get()
    if nome:
        global conta
        conta = ContaBancaria(nome)
        messagebox.showinfo("Sucesso", f"Conta criada para {nome} com saldo inicial R$0.00")
    else:
        messagebox.showwarning("Erro", "Por favor, insira um nome para o titular.")

def depositar():
    if conta is None:
        messagebox.showwarning("Erro", "Nenhuma conta criada!")
        return
    try:
        valor = float(entry_valor.get())
        if conta.depositar(valor):
            messagebox.showinfo("Sucesso", f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            messagebox.showwarning("Erro", "Valor inválido para depósito.")
    except ValueError:
        messagebox.showwarning("Erro", "Por favor, insira um valor válido.")

def sacar():
    if conta is None:
        messagebox.showwarning("Erro", "Nenhuma conta criada!")
        return
    try:
        valor = float(entry_valor.get())
        sucesso, mensagem = conta.sacar(valor)
        if sucesso:
            messagebox.showinfo("Sucesso", mensagem)
        else:
            messagebox.showwarning("Erro", mensagem)
    except ValueError:
        messagebox.showwarning("Erro", "Por favor, insira um valor válido.")

def exibir_saldo():
    if conta is None:
        messagebox.showwarning("Erro", "Nenhuma conta criada!")
    else:
        saldo = conta.exibir_saldo()
        messagebox.showinfo("Saldo", saldo)


root = tk.Tk()
root.title("Sistema Bancário - Tkinter")


conta = None


frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

label_titular = tk.Label(frame, text="Nome do Titular:")
label_titular.grid(row=0, column=0, sticky="e")
entry_titular = tk.Entry(frame, width=30)
entry_titular.grid(row=0, column=1)

label_valor = tk.Label(frame, text="Valor (R$):")
label_valor.grid(row=1, column=0, sticky="e")
entry_valor = tk.Entry(frame, width=30)
entry_valor.grid(row=1, column=1)

btn_criar = tk.Button(frame, text="Criar Conta", command=criar_conta, width=20)
btn_criar.grid(row=2, column=0, pady=10)

btn_depositar = tk.Button(frame, text="Depositar", command=depositar, width=20)
btn_depositar.grid(row=2, column=1, pady=10)

btn_sacar = tk.Button(frame, text="Sacar", command=sacar, width=20)
btn_sacar.grid(row=3, column=0, pady=10)

btn_saldo = tk.Button(frame, text="Exibir Saldo", command=exibir_saldo, width=20)
btn_saldo.grid(row=3, column=1, pady=10)

root.mainloop()
