import pandas as pd
import matplotlib.pyplot as plt

def consumirHistograma():
    datos=pd.read_csv('casasboston.csv')
    #print(datos)
    df=datos[['RM', 'CRIM', 'TOWN', 'TAX']]
    #print(df)
    df.TAX.plot.hist()
    plt.show()

#consumirHistograma()

def consumirDispersion():
    datos = pd.read_csv('casasboston.csv')
    #print(datos)
    df=datos[['RM', 'CRIM', 'TOWN', 'TAX', 'MEDV']]
    #print(df)
    df.plot.scatter(x='CRIM', y='MEDV', alpha=0.3)
    plt.show()

#consumirDispersion()

def consumirBarras():
    datos=pd.read_csv('casasboston.csv')
    #print(datos)
    df = datos[['RM', 'CRIM', 'TOWN', 'TAX', 'MEDV']]
    #print(df)
    valor_por_ciudad = df.groupby('TOWN')['MEDV'].mean()
    valor_por_ciudad.head(10).plot.barh()
    df.plot.barh
    plt.show()

#consumirDispersion()

def consumirCajas():
    datos=pd.read_csv('casasboston.csv')
    #print(datos)
    df = datos[['RM', 'CRIM', 'TOWN', 'TAX', 'MEDV']]
    #print(df)
    df.head(10).boxplot (column='CRIM',by='MENDY', figsize=(8, 6))
    plt.show()

#consumirCajas()

def consumirCircular():
    datos=pd.read_csv('casasboston.csv')
    df = datos[['RM', 'CRIM', 'TOWN', 'TAX', 'MEDV']]
    df.CRIM.head(10).value_counts().plot.pie()
    plt.show()

consumirCircular()


