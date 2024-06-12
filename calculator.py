
#Vamos criar uma função para a calculadora e vamos montar ela, passando como os parametros os atributos que vamos utilizar na montagem dessa calculadora => numberOne, numberTwo, operator. 
def calculator(numberOne, numberTwo, operator):
  #Vamos verificar com o if se o usuário escolheu o operador "+", vamos somar o atributo numberOne com o atributo numberTwo. 
  if operator == "+" :
    return numberOne + numberTwo
  #Se o usuário não escolher o operador "+", mas escolher o operador "-", vamos subtrair o atributo numberOne com o atributo numberTwo. 
  elif operator == "-" :
    return numberOne - numberTwo
  #Se o usuário não escolher o operador "-", mas escolher o operador "*", vamos multiplicar o atributo numberOne com o atributo numberTwo. 
  elif operator == "*" :
    return numberOne * numberTwo
  #Se o usuário não escolher o operador "*", mas escolher o operador "/", vamos dividir o atributo numberOne com o atributo numberTwo. 
  elif operator == "/" : 
    #Aqui dentro vamos fazer mais uma verificação: se um dos dois números inseridos forem diferente de zero, a operação de divisão será feita normalmente.
    if numberTwo != 0:
      return numberOne / numberTwo
    #Se um dos dois números inseridos forem iguais a zero, a operação de divisão dará um erro! 
    else: 
      return "Erro: Divisão por zero!"
    #Se o usuário inserir um operador inválido, também aparecerá uma mensagem de erro! 
  else: 
    return "Operador inválido!"
  
  
  #Agora vamos criar uma função para verificarmos as informações que vamos solicitar aos clientes e para tratar possíveis excessões e erros dessas informações.
def verification():
    try:
      numberOne = int(input("Insira um número:"));
      operator = input("Escolha um operador: +, -, *, /: ")
      numberTwo = int(input("Insira um segundo número:")); 
      #Aqui vamos chamar a função calculator que construimos a calculadora com os operadores.
      return calculator(numberOne, numberTwo, operator)
    except ValueError:
      return "Erro! Entrada inválida, Por favor insira um número válidos!" 
    
    #Vamos chamar a função verification, em que verificamos as informações solicitadas e tratamos uma possível erro ou excessão e vamos colocar em uma variável. 
resultado = verification()
#Vamos usar a propriedade print, com a string de saída e a variável resultado onde está a função verification onde colocamos as verificações.
print("O resultado da operação é :", resultado)


  

