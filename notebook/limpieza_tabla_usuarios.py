import pandas as pd

def limpiar_simulacion(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

    # 1. Limpiar las columnas del dataframe que son palabras (String)
    columnas_texto = ["nombre_usuario", "email", "rol"]
    for columna in columnas_texto:
        data_frame_limpio[columna] = data_frame_limpio[columna].astype("string").str.strip().str.lower()

    # 2. Definir valores esperados
    roles_validos = ["admin", "cliente", "editor"]
    data_frame_limpio["rol"] = data_frame_limpio["rol"].where(data_frame_limpio["rol"].isin(roles_validos), pd.NA)

    # 3. Evaluar columnas numericas
    data_frame_limpio["id"] = pd.to_numeric(data_frame_limpio["id"])
    data_frame_limpio["id_usuario"] = pd.to_numeric(data_frame_limpio["id_usuario"])

    # 4. Evaluar columna de fecha
    data_frame_limpio["fecha_creacion"] = pd.to_datetime(data_frame_limpio["fecha_creacion"])

    # 5. Reemplazar fechas nulas con una fecha por defecto
    fecha_defecto = pd.to_datetime("2024-01-01")
    data_frame_limpio["fecha_creacion"] = data_frame_limpio["fecha_creacion"].fillna(fecha_defecto)

    # 6. Eliminar registros nulos de campos obligatorios
    columnas_obligatorias = ["id", "id_usuario", "nombre_usuario", "email", "rol"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    # 7. Eliminar valores invalidos en campos numericos
    # Filtramos para que el ID siempre sea positivo
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id_usuario"] >= 0]

    # 8. Eliminar registros duplicados
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio
