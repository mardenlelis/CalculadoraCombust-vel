class Calculo:

    def __init__(self):
        self.__valor_gasolina = 4.80
        self.__valor_alcool = 3.80
        self.__valor_diesel = 3.90

    def calcular_gasto(self, distancia, consumo_alcool, consumo_gas, consumo_dies):
        if(distancia <= 0 and (consumo_alcool <= 0) and (consumo_gas <= 0)):
            raise Exception('Os valores recebidos não podem ser menor ou igual a zero.')
        elif(distancia <= 0):
            raise Exception('O valor da distância não pode ser menor ou igual a zero.')
       
        if(consumo_gas > 0):
            gasto_gasolina = round(
            (distancia / consumo_gas) * self.__valor_gasolina, 2)
        else:
            raise Exception('Valor do consumo do combustível gasolina não informado.')

        if(consumo_alcool > 0):
            gasto_alcool = round(
            (distancia / consumo_alcool) * self.__valor_alcool, 2)
        else:
             raise Exception('Valor do consumo do combustível gasolina não informado!')

        if(consumo_dies > 0):
            gasto_diesel = round(
            (distancia / consumo_dies) * self.__valor_diesel, 2)
        else:
            gasto_diesel = 0

        return """
        O valo total gasto para cada tipo de combustível será de:
        
        Gasolina --> R$ {}
        Alcool   --> R$ {}
        Diesel   --> R$ {}
        """.format(
            gasto_gasolina, gasto_alcool, gasto_diesel
        )
        



