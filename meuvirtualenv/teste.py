x = 1
y = 2
def func1 (x, y): print ("Dentro da func1: ", x, " ", y)
func1 (x, y)

def func2 (m = 3, n = 4): print ("Dentro da func2: ", m, " ", n)
func2 ()
func2(x)
func2(y)
func2(x, y)
func2(x+7, y+9)

print ("Dentro do print externo: ", x, " ", y)

print ()

def oi(nome):
    if nome == 'Ola':
        print('Olá Ola!')
    elif nome == 'Sonja':
        print('Olá Sonja!')
    else:
        print('Olá estranho!')
    print()

oi("Ana")

def func(): 
    indice = {}
    indice['casa'] = [1,2,3]
    indice['caro'] = [1,3,4, 7]
    print(indice)

    if 3 > 2: print('Funciona!')

    if 5 > 4: 
        print('Funciona também!')

    name = 'Sonja'
    if name == 'Ola':
        print('Olá Ola!')
    elif name == "Sara":
        print ("Olá Sara")
    elif name == 'Sonja':
        print('Olá Sonja!')
    else:
        print('Olá estranho!')

    volume = 57
    if volume < 20: 
        print("Está um pouco baixo")
    elif 20 <= volume < 40: 
        print("Está bom para música ambiente")
    elif 40 <= volume < 60: 
        print("Perfeito, posso ouvir todos os detalhes")
    elif 60 <= volume < 80: 
        print("Ótimo para festas!")
    elif 80 <= volume < 100: 
        print("Está muito alto!")
    else: 
        print("Meus ouvidos doem! :(")

    volume = 15
    # Mudar o volume se estiver muito alto ou muito baixo:
    if volume < 20 or volume > 80:
        volume = 50
        print("Bem melhor!")

print ("Inicio da execução da função")
func ()
print ("Fim da execução da função\n")

oi("Sonja")

print ()

def ola(nome):
    print('Oi ' + nome + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'você']
print (girls)
for name in girls:
    ola(name)
    #print('Próxima')

