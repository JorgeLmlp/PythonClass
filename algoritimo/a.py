matriz = [

]

linhas = int(input('digite a quantidade de linhas'))
colunas = int(input('digite o numero de colunas: '))
for i in range linhas:
    row = []    
    for j in range colunas:
        valor = input(f"digite o valor da linha {i} coluna: {j}")
        valores = input(f"digite os respectivos valores da linha numero: {i}")
        row.append(valor)
    matriz.append(row)

personagem = [0,0] 


def andarEsquerda():
    if personagem[1] > 0 and personagem[0] < colunas:
        personagem[0] +=1
    
def andarCima():
    if personagem[0] > 0 and personagem[0] < linhas:
        personagem[0] +=1
    
def andarBaixo():
    if personagem[0] < linhas
        personagem[0] +=1
    
def andarDireita():         
    if personagem[1] < linhas and personagem[0] < colunas:
        personagem[0] +=1
        
        
escolha = int(input("digite sua escolha"))
pontuacao = 0
match(escolha):
    case 1:
        andarEsquerda()
        pontuacao += matriz[personagem[1]]
    case 2: 
        andarCima()
        pontuacao += matriz[personagem[0]]
    case 3 : 
        andarBaixo()
        pontuacao += matriz[personagem[0]]
    case 4:
        andarDireita()        
        pontuacao += matriz[personagem[1]]
                
        
        
 
 
        