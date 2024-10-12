# Colocar exceptions nas funções da classe Funcionario.
# Obrigar o self.diasTrabalhados a ser int.

class Funcionario:
    def __init__(self):
        self.cargo = input("Digite 'S' se voce for supervisor ou 'O' se for operador: ").lower()
        # Considero que o funcionário padrão é um operador da madrugada
        self.salario = 1800.0
        self.salarioPHora = self.salario / (15.0 * 6.0)
        self.setSalarios()
        if(self.cargo == 'o'): 
            self.turno = input("Digite 'N' se seu turno for noturno ou 'M' se for de madrugada: ").lower()
            self.horasPorDiaComAddNot = 5.0
            self.setHoras()
        else: self.horasPorDiaComAddNot = 7.0
        self.diasTrabalhados = 15
        self.addNotTotal = self.calcular()

    def setSalarios(self):
        if(self.cargo == 's'): 
            print("Você é supervisor.")
            self.salario = 2500
            self.salarioPHora = self.salario / (15 * 12)
        elif(self.cargo == 'o'): print("Você é operador.")
        else: 
            self.cargo = input("Digite apenas 'S' ou 'O', por favor: ").lower()
            self.setSalarios()

    def setHoras(self):
        if(self.turno == "n"): self.horasPorDiaComAddNot = 2.25
        elif(self.turno != "m"):
            self.turno = input("Digite apenas 'N' ou 'M', por favor: ").lower()
            self.setHoras
            
    def calcular(self):
        try:
            self.diasTrabalhados = int(input("Quantos dias você trabalhou neste mês? "))
            return float(self.diasTrabalhados) * self.horasPorDiaComAddNot * self.salarioPHora * 0.2
        except ValueError:
            print("Digite um numeral, por favor.")
            self.addNotTotal = self.calcular()