import pandas as pd

def describir_transacciones(df_limpio_transacciones):
        print("--- RESUMEN DE LA TABLA DE TRANSACCIONES ---")
        print(f"Total de registros limpios: {df_limpio_trans.shape[0]}")

        print("\n--- ANÁLISIS FINANCIERO (MONTO) ---")
        # El describe() aquí es vital para ver el promedio de gasto/ingreso
        print(df_limpio_trans['monto'].describe())

        print("\n--- DISTRIBUCIÓN POR TIPO DE MOVIMIENTO ---")
        # Nos dirá cuántos son ingresos y cuántos egresos
        print(df_limpio_trans['tipo'].value_counts())

        print("\n--- FRECUENCIA POR CATEGORÍA ---")
        # Para saber en qué categoría hay más movimientos
        print(df_limpio_trans['categoria_id'].value_counts())

        print("\n--- PERIODO DE TIEMPO ANALIZADO ---")
        # Usamos la columna 'fecha' que es la que definiste en la simulación
        print(f"Primera transacción: {df_limpio_trans['fecha'].min()}")
        print(f"Última transacción: {df_limpio_trans['fecha'].max()}")

        print("\n--- TOTAL DE DINERO MOVILIZADO ---")
        total = df_limpio_trans['monto'].sum()
        print(f"Suma total de montos: ${total:,.2f}")
