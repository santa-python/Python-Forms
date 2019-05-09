import tkinter as tk

gui=tk.Tk()

gui.title("Formulario Calculadora")
gui.geometry("500x500")

class Calculadora(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.create_widgets()
		self.pack()

	def soma(self, a, b):
		print(a + b)

	def subtrai(self,a,b):
		return a - b

	def multiplica(self,a,b):
		return a * b

	def divide(self,a,b):
		return a / b

	def create_widgets(self):
		self.entrada1 = tk.Entry(self)
		self.entrada1.pack()

		self.entrada2 = tk.Entry(self)
		self.entrada2.pack()

		self.conteudo1 = tk.StringVar(self)
		self.conteudo2 = tk.StringVar(self)

		self.entrada1["textvariable"] = self.conteudo1
		self.entrada2["textvariable"] = self.conteudo2

		self.button1 = tk.Button(self)
		self.button1["text"] = "Somar"
		self.button1["command"] = lambda: self.soma(float(self.conteudo1.get()), float(self.conteudo2.get()))
		self.button1.pack()

		self.button2 = tk.Button(self)
		self.button2["text"] = "Subtrair"
		self.button2["command"] = lambda: self.subtrai(float(self.conteudo1.get()), float(self.conteudo2.get()))
		self.button2.pack()

		self.button3 = tk.Button(self)
		self.button3["text"] = "Multiplicar"
		self.button3["command"] = lambda: self.multiplica(float(self.conteudo1.get()), float(self.conteudo2.get()))
		self.button3.pack()

		self.button4 = tl.Button(self)
		self.button4["text"] = "Dividir"
		self.button4["command"] = lambda: self.multiplica(float(self.conteudo1.get()), float(self.conteudo2.get()))
		self.button4.pack()


gui.mainloop()