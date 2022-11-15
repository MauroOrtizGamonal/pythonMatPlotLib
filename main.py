#consume los datos del archivo inversiones
#almacena en un dataFrame el titulo, el importe y el distrito
#gráfico de dispersión de los importes de inversiones por distrito
#gráfico de barras de la inversion media de los 10 primeros distritos
#gráfico circular de las inversiones de 10 titulos

import pandas as pd
import matplotlib.pyplot as plt

def consumirDispersion():
    datos = pd.read_csv('suelo.csv')
    df=datos[['NOM_ENS', 'SUPERFICIE', 'TIPUSSOL']]
    df.plot.scatter(x='SUPERFICIE', y='TIPUSSOL', alpha=0.3)
    plt.show()

consumirDispersion()