import matplotlib.pyplot as plt
import pandas as pd
import io
import base64

class Estadistica:
    """
    Clase estadistica que se encarga de realizar diferentes
    calculos estadisticos sobre el proyecto de importacion
    """
    def __init__(self):
        self.df = pd.read_excel('info/simulacion.xlsx')
    
    def datosExcel(self):
        """
        funcion que retorna el dataframe con los datos
        """
        return self.df

    def graficoDistritoDolares(self):
        """
        Funcion que retorna la grafica referente al pais que 
        se realizan las importaciones
        """
        img = io.BytesIO()
    

        distritos = self.df['País'].unique()
        dolares = []
        for i in distritos:
            suma = self.df.loc[self.df['País'] == i, ['Total']].sum()[0]
            dolares.append(suma)

        plt.figure(figsize=(10,5))
        plt.bar(distritos, dolares, color='green')
        plt.title('Casos reportados de Dengue por Pais')
        plt.xticks(rotation=80)
        plt.ylabel('Total casos')
        plt.savefig(img, format='png')
        img.seek(0)

        img_url = base64.b64encode(img.getvalue()).decode()
        return img_url

    def graficoFrecuenciaPais(self):
        """
        Funcion que retorna la grafica de la frecuenta de los distritos
        """
        img = io.BytesIO()
        
        # x = self.df['País']
        x=self.df.loc[8:19, ['País']]
        # x[2:6]
        plt.figure(figsize=(10,5))
        plt.hist(x, bins=None, color='purple')
        plt.title('Frecuencia de casos de Dengue por 11 paises nombrados')
        plt.xticks(rotation=60)
        plt.ylabel('Frecuencia')

        plt.savefig(img, format='png')
        img.seek(0)

        img_url = base64.b64encode(img.getvalue()).decode()
        return img_url
        
    def graficoTop10Americas(self):
        """
        Funcion que devuelve un diccionario con los datos sobre los paises que
        se realizan importaciones
        """
        img = io.BytesIO()
        lista = []
        for i in self.df['País'].unique():
            dengue = self.df[self.df['País'] == i]['País'].value_counts().tolist().pop()
            paises = self.df[self.df['País'] == 'Ecuador']['País'].sum()
            lista.append((i, dengue, paises))
        lista.sort(reverse=True, key=lambda item: item[1])

        paises = [i[0] for i in lista[42:50]]
        dengue = [i[1] for i in lista[42:50]]
        plt.figure(figsize=(10,5))
        plt.bar(paises, dengue, color='pink')
        plt.ylabel('Dengue')
        plt.title('Top 8 lugares en America con más dengue')
        plt.xticks(rotation=15)
        
        plt.savefig(img, format='png')
        img.seek(0)

        img_url = base64.b64encode(img.getvalue()).decode()
        return img_url

