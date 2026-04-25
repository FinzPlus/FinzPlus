import pandas as pd
from utils.simulacion import simular_Categorias
from notebook.limpieza import limpiar_datos
from utils.simularcuentas import generar_metas
from utils.simularcuentas import generar_deudas
from notebook.limpiezaDeudas import limpiar_datos_deudas
from notebook.limpiezaMetas import limpiar_datos_metas

#Llamando a las rutinas de simulacion
simulaciones=simular_Categorias(100000)
simulaciones=generar_metas (100)
simulaciones=generar_deudas (100)

#Llamando a pandas para crear data frames de los datos de entrada
categorias_ordenadas=pd.DataFrame(simulaciones)
metas_ordenadas:pd.DataFrame(simularcuentas)

#LLamando a la rutina de limpieza
categorias_limpias=limpiar_datos(categorias_ordenadas)
print(categorias_limpias)
metas_limpias=limpiar_datos_deudas(metas_ordenadas)
print(metas_limpias)
deudas_limpias=limpiar_datos_metas(deudas_ordenadas)
print(deudas_limpias)




