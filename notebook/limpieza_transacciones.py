import pandas as pd

def limpiar_transacciones(df_sucio):
    df_limpio = df_sucio.copy()

    # 1. Limpiar las columnas que son palabras (String)
    # Según tu imagen: 'tipo' y 'descripcion' son los VARCHAR principales
    columnas_texto = ["tipo", "descripcion"]
    for columna in columnas_texto:
        df_limpio[columna] = df_limpio[columna].astype("string").str.strip().str.lower()

    # 2. Definir valores esperados
    # En finanzas el 'tipo' suele ser cerrado: ingreso o egreso
    tipos_validos = ["ingreso", "egreso"]
    df_limpio["tipo"] = df_limpio["tipo"].where(df_limpio["tipo"].isin(tipos_validos), pd.NA)

    # 3. Evaluar columnas numericas
    # Convertimos todos los IDs y el Monto (Decimal en tu imagen)
    df_limpio["id"] = pd.to_numeric(df_limpio["id"])
    df_limpio["usuario_id"] = pd.to_numeric(df_limpio["usuario_id"])
    df_limpio["monto"] = pd.to_numeric(df_limpio["monto"])

    # 4. Evaluar columna de fecha
    df_limpio["fecha"] = pd.to_datetime(df_limpio["fecha"])

    # 5. Reemplazar fechas nulas con una fecha por defecto
    fecha_defecto = pd.to_datetime("2024-01-01")
    df_limpio["fecha"] = df_limpio["fecha"].fillna(fecha_defecto)

    # 6. Eliminar registros nulos de campos obligatorios
    columnas_obligatorias = ["id", "usuario_id", "monto", "tipo"]
    df_limpio = df_limpio.dropna(subset=columnas_obligatorias)

    # 7. Eliminar valores invalidos en campos numericos
    df_limpio = df_limpio[df_limpio["usuario_id"] > 0]
    df_limpio = df_limpio[df_limpio["monto"] > 0]

    # 8. Eliminar registros duplicados
    df_limpio = df_limpio.drop_duplicates()

    return df_limpio
