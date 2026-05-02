import pandas as pd

def describir_datos(df_limpio_usuarios):
    print("=== DESCRIPCIÓN DE LA TABLA USUARIOS ===")
    print(f"Número de filas: {df_limpio_usuarios.shape[0]}")
    print(f"Número de columnas: {df_limpio_usuarios.shape[1]}")
    print(f"Columnas disponibles: {list(df_limpio_usuarios.columns)}\n")
    
    print("Estadísticas de valores numéricos:")
    print(df_limpio_usuarios[['id', 'id_usuario']].describe())
    print("\n")
    
    print("Valores categóricos (Género):")
    print(df_limpio_usuarios['genero'].value_counts())
    print("\n")
    
    print("Valores categóricos (Rol):")
    print(df_limpio_usuarios['rol'].value_counts())
    print("\n")
    
    print(f"Fecha de creación más antigua: {df_limpio_usuarios['fecha_creacion'].min()}")
    print(f"Fecha de creación más reciente: {df_limpio_usuarios['fecha_creacion'].max()}")
    print("-" * 40)
