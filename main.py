#manejo de datos
import numpy as np
import pandas as pd
# #manipulacion de graficas
import seaborn as sns
import matplotlib.pyplot as plt
# #interaccion con Api de yahoo finance
import yfinance as yf


class Portafolio:

    def __init__(self, input):
        self.input = input
        print(f'Portafolio - {input["portafolio_name"]} - Activo')

        #Descargar automaticamente los ticks
        self.ticks = {}
        # self.dowload_ticks()

    #muestra de ticks a mostrar
    def show_ticks(self, input):
        for i in range(len(input["ticks"])):
            tick_name = input["ticks"][i]
            print(f'{i+1} - {tick_name}')

    #descarga lista de ticks establecida en inputs
    def download_ticks(self):
        for tick in self.input["ticks"]:            
            t = yf.Ticker(tick)
            self.ticks[tick] = t
    
    #grafica 
    def tick_value(self, tick):
        data = self.ticks[tick].history(period = 'YTD')
        plt.figure(figsize = (8,6))
        plt.title(f'{tick} - YTD Historical Values')
        plt.plot(data.index, data['Close'])
        plt.show()
            


# spy = yf.Ticker("SPY")
# print(spy.history(period = 'YTD'))
# data = yf.download("BTC-USD", start = '2022-01-01', end= '2022-09-02')
# print(data)

parametros = {
    'portafolio_name' : 'Financiero',
    'ticks'           : ['SPY', 'META', 'AMZN', 'TSLA', 'BTC-USD' ]
}

port = Portafolio(parametros)
port.show_ticks(parametros)
port.download_ticks()
# print(port.ticks["BTC-USD"].history(period = 'YTD'))
port.tick_value("BTC-USD")
