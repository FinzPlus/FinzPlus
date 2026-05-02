import pandas as pd
from utils.simulacion import simular_Categorias
from utils.simularcuentas import generar_metas, generar_deudas
from utils.simular_usuarios import generar_usuarios
from utils.simulacion_transacciones import generar_transacciones
from rutinas.simular_cuentas import simular_cuentas_sucias
from notebook.limpieza import limpiar_datos
from notebook.limpiezaDeudas import limpiar_datos_deudas
from notebook.limpiezaMetas import limpiar_datos_metas
from notebook.limpieza_tabla_usuarios import limpiar_usuarios
from notebook.limpieza_transacciones import limpiar_transacciones
from notebook.descripcion_usuarios import describir_datos
from notebook.descripcion_transacciones import describir_transacciones
from notebook.descripcionDeudas import describir_deudas
from notebook.descripcionMetas import describir_metas
from rutinas.limpiar_cuentas import limpiar_cuentas

# Generar datos simulados
categorias_simuladas = simular_Categorias(1000)
metas_simuladas = generar_metas(1000)
deudas_simuladas = generar_deudas(1000)
usuarios_simulados = generar_usuarios(1000)
transacciones_simuladas = generar_transacciones(1000)
cuentas_simuladas = simular_cuentas_sucias(1000)

# Convertir a DataFrame
categorias_ordenadas = pd.DataFrame(categorias_simuladas)
metas_ordenadas = pd.DataFrame(metas_simuladas)
deudas_ordenadas = pd.DataFrame(deudas_simuladas)
usuarios_ordenados = pd.DataFrame(usuarios_simulados)
transacciones_ordenadas = pd.DataFrame(transacciones_simuladas)
cuentas_ordenadas = pd.DataFrame(cuentas_simuladas)

# Limpiar los datos
categorias_limpias = limpiar_datos(categorias_ordenadas)
metas_limpias = limpiar_datos_metas(metas_ordenadas)
deudas_limpias = limpiar_datos_deudas(deudas_ordenadas)
usuarios_limpios = limpiar_usuarios(usuarios_ordenados)
transacciones_limpias = limpiar_transacciones(transacciones_ordenadas)
cuentas_limpias = limpiar_cuentas(cuentas_ordenadas)

# Mostrar resultados resumidos

def mostrar_resumen(nombre, original, limpio):
    print(f"--- {nombre} ---")
    print(original.head())
    print(f"Registros originales: {len(original)}, registros limpios: {len(limpio)}")
    print(f"{nombre} limpios: {limpio.shape}")
    print(limpio.head(5))
    print()

mostrar_resumen("Categorías", categorias_ordenadas, categorias_limpias)
mostrar_resumen("Metas", metas_ordenadas, metas_limpias)
mostrar_resumen("Deudas", deudas_ordenadas, deudas_limpias)
mostrar_resumen("Usuarios", usuarios_ordenados, usuarios_limpios)
mostrar_resumen("Transacciones", transacciones_ordenadas, transacciones_limpias)
mostrar_resumen("Cuentas", cuentas_ordenadas, cuentas_limpias)

print("--- Descripción detallada de cada tabla ---")
print()

print("=== Categorías ===")
print("Columnas:", list(categorias_limpias.columns))
print(categorias_limpias.describe(include='all'))
print()

print("=== Metas ===")
describir_metas(metas_limpias)
print()

print("=== Deudas ===")
describir_deudas(deudas_limpias)
print()

print("=== Usuarios ===")
describir_datos(usuarios_limpios)
print()

print("=== Transacciones ===")
describir_transacciones(transacciones_limpias)
print()

print("=== Cuentas ===")
print(f"Número de filas: {cuentas_limpias.shape[0]}")
print(f"Número de columnas: {cuentas_limpias.shape[1]}")
print(f"Columnas disponibles: {list(cuentas_limpias.columns)}")
print(cuentas_limpias[['id', 'usuario_id', 'saldo_actual']].describe(include='all'))




