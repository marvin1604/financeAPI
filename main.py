#manejo de datos
# import numpy as np
# import pandas as pd
# #manipulacion de graficas
# import seaborn as sns
# import matplotlib.pyplot as plt
# #interaccion con Api de yahoo finance
# import yfinance as yf

class Portafolio:

    def __init__(self, input):
        self.input = input
        print(f'Portafolio - {input["portafolio_name"]} - Activo')


parametros = {
    'portafolio_name' : 'Financiero'

}
port = Portafolio(parametros)