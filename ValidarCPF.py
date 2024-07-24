"""

Sistema de Validação de CPF

"""

soma = 0
resto = 0
cpf = str("")


# Entrada do CPF
def CPF():
	global cpf
	while True:
		cpf = input("Digite os números do CPF: ")
		if not cpf:
			print("Digite algum CPF")
		else:
			try:
				cpf = int(cpf)
				cpf = str(cpf)
				break
			except ValueError:
				print("Digite apenas números")
				pass
	return cpf


# Validador de CPF
def Validador(cpf, digito):
	global soma, resto
	soma = 0
	for i in range(digito - 1):
		soma = soma + (int(cpf[i]) * (digito - i))
	resto = ((soma % 11) * 10) % 11
	return resto


# Programa
def main():
	# Entrada do CPF
	CPF()
	# Validador de CPF
	digito1 = str(Validador(cpf, 10))
	digito2 = str(Validador(cpf, 11))
	return print("CPF válido") if cpf[9] == digito1[-1] and cpf[10] == digito2[-1] else print("CPF inválido")
	# if cpf[9] == digito1[-1] and cpf[10] == digito2[-1]:
	# 	print("CPF válido")
	# else:
	# 	print("CPF inválido")


# Saída
if __name__ == "__main__":
	main()

