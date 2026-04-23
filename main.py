import pandas as pd
from utils.simulacion import simular_Categorias
from notebook.limpieza import limpiar_datos


#Llamando a las rutinas de simulacion
simulaciones=simular_Categorias(100000)

#Llamando a pandas para crear data frames de los datos de entrada
categorias_ordenadas=pd.DataFrame(simulaciones)

#LLamando a la rutina de limpieza
categorias_limpias=limpiar_datos(categorias_ordenadas)
print(categorias_limpias)



