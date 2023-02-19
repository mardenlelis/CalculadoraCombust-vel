from calculo import Calculo

def main():
    print(
        """
        Esta aplicação tem como finalidade demonstrar os valores que serão gastos 
        com combustível durante uma viagem, com base no consumo do seu veículo, e 
        com a distância determinada por você!        
        """
    )

    print("Os combustíveis disponíveis para este cálculo são:")
    print("    ° Álcool")
    print("    ° Díesel")
    print("    ° Gasolina")

    print(" ")

    try:
        distancia = float(input('Qual a distância em Quilômetros a ser percorrida?'))
        consumo_alcool = float(input('Qual o consumo em litros de Álcool por Kilometro percorrido?'))
        consumo_gasolina = float(input('Qual o consumo em litros de Gasolina por Kilometro percorrido?'))
        consumo_diesel = float(input('Qual o consumo em litros de Gasolina por Kilometro percorrido?'))

        calculo = Calculo()

        print(
            calculo.calcular_gasto(distancia, consumo_alcool, consumo_gasolina, consumo_diesel)
        )
    except ValueError as erro:
        print('O valor recebido não é válido. Favor inserir o valor corretamente.')


if __name__ == '__main__':
    main()



