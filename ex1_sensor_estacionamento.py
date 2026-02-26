"""
EXERCICIO

Desenhe (ou descreva) o fluxo para um sensor de ré de um carro: 
- O sensor lê a distância. 
- Se a distância for menor que 0.5m: Tocar bipe contínuo e exibir "PARE". 
- Se estiver entre 0.5m e 2m: Tocar bipe intermitente. 
- Senão: Não emitir som.
"""
import random

while True:
    distancia = random.randint(0, 5)
    print(distancia)

    if distancia <= 2 and distancia >= 0.5:
        print("SOM: bipe")

    elif distancia < 0.5:
        print("PARE!!!")
        print("SOM: bipe contínuo!")
        break

    else:
        print("fora do alcance")