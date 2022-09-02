#manejo de datos
import numpy as np
import pandas as pd
# #manipulacion de graficas
import seaborn as sns
import matplotlib.pyplot as plt
# #interaccion con Api de yahoo finance
import yfinance as yf


class Portafolio:
    #Inicializamos nuestra clase
    def __init__(self, input):
        self.input = input
        print(f'Portafolio - {input["portafolio_name"]} - Activo')

        #Descargar automaticamente los ticks
        self.ticks = {}
        

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
    
    #grafica timeseries de tick especifico
    def tick_value(self, tick):
        data = self.ticks[tick].history(period = 'YTD')
        plt.figure(figsize = (8,6))
        plt.title(f'{tick} - YTD Historical Values')
        plt.plot(data.index, data['Close'])
        plt.show()
    
    #grafica timeseries de todos los ticks del portafolio
    def ticks_values(self):
        plt.figure(figsize = (12,8))
        plt.title(f'Portafolio ticks - YTD Historical timeseries')
        for tick in self.ticks:
            data = self.ticks[tick].history(period = 'YTD')
            plt.plot(data.index, data['Close'], label= tick)
        plt.legend()       
        plt.show()

    #grafica timeseries rendimiento tick especifico
    def tick_return(self, tick):
        data = self.ticks[tick].history(period = 'YTD')
        data['returns'] = data['Close'].pct_change()
        plt.figure(figsize = (8,6))
        plt.title(f'{tick} - YTD Historical returns')
        plt.plot(data.index, data['returns'])
        plt.show()

    #obtener informacion de la correlacion entre 2 ticks
    def compare_ticks(self, tick1, tick2):
        #datos de los ticks
        data_t1 = self.ticks[tick1].history(period = "YTD")
        data_t1["returns"] = data_t1["Close"].pct_change()
        data_t2 = self.ticks[tick2].history(period = "YTD")
        data_t2["returns"] = data_t2["Close"].pct_change()

        #grafica
        plt.figure(figsize = (8,6))
        plt.title(f'correlación of return between {tick1} and {tick2}')
        plt.xlabel(tick1)
        plt.ylabel(tick2)
        
        plt.plot(data_t1["returns"], data_t2["returns"], "o")
        plt.show()
        
        #correlation index
        corr_index = data_t1["returns"].corr(data_t2["returns"])

        print(f'The correlacion index between {tick1} and {tick2} is: {corr_index}')

            

#conexion con API - Descarga market data de YAhoo Finance´s API 
# spy = yf.Ticker("SPY")
# print(spy.history(period = 'YTD'))
# data = yf.download("BTC-USD", start = '2022-01-01', end= '2022-09-02')
# print(data)

parametros = {
    'portafolio_name' : 'Financiero',
    'ticks'           : ['SPY', 'META', 'AMZN', 'TSLA', 'LIT', 'BTC-USD' ]
}


port = Portafolio(parametros)

#llamando las funciones de la aplicación
port.show_ticks(parametros)
port.download_ticks()

# print(port.ticks["BTC-USD"].history(period = 'YTD'))

port.tick_value("BTC-USD")
# port.ticks_values()
# port.tick_return("BTC-USD")
# port.compare_ticks("LIT", "TSLA")
