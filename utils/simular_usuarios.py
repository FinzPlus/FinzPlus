from datetime import datetime, timedelta
import random

def generar_usuarios(num_usuarios):

    #Semuilla para generar datos aleatorios

    nombres_h = ["Juan", "Carlos", "Luis", "Miguel", "Pedro", "Jorge", "Andrés", "Miguel", "Anderson"]
    nombres_m = ["María", "Ana", "Sofía", "Laura", "Lucía", "Elena", "Marta", "Daniela", "Maria Alejandra"]
    apellidos = ["García", "Pérez", "López", "Martínez", "Sánchez", "Gómez", "Díaz", "Fernández", "Romero", "Vargas"]
    dominios=["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "icloud.com"]
    roles_base = ["Admin", "Cliente", "Premium"]
    generos_base = ["Masculino", "Femenino", "Otro"]
    fechaInicio=datetime(2024,1, 1)
    

    usuarios = []
    for i in range(num_usuarios):
        genero = random.choice(generos_base)
        
        if genero == "Masculino":
            nombre = random.choice(nombres_h)
        elif genero == "Femenino":
            nombre = random.choice(nombres_m)
        else:
            nombre = random.choice(nombres_h + nombres_m) # Mezcla para 'Otro'

        apellido = random.choice(apellidos)
        nombre_completo = f"{nombre} {apellido}"
        
        email_base= nombre_completo.lower().replace(" ", ".")

        usuario={
            "id": i,
            "id_usuario": random.randint(9999,99999999),
            "nombre_usuario": nombre_completo,
            "email": f"{email_base}@{random.choice(dominios)}",
            "rol": random.choice(roles_base), 
            "fecha_creacion": (fechaInicio + timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d"),
            "password": hash(random.randint(100000, 999999))
        }

        #Inyetamos algunos errores controlados
        probabilidad_error = random.random()

        if probabilidad_error < 0.10:            
            # ERROR - El ID se pierde (Nulo)
            usuario["id_usuario"] = None            
            
        elif probabilidad_error < 0.20:
            # ERROR - Nombre en mayúsculas locas o con espacios extras
            usuario["nombre_usuario"] = usuario["nombre_usuario"].upper()

        elif prob < 0.30:
            usuario["id_usuario"] = None
            
        elif prob < 0.40:
            usuario["genero"] = "No especificado" # Error de categoría
            
        elif prob < 0.50:
            usuario["rol"] = "Usuario_Externo" # Error de rol inválido
            
        elif probabilidad_error < 0.60:
            # ERROR 4: Rol inexistente
            usuario["rol"] = random.choice(["Desconocido", "Dueño del chuzo"])
            
        elif probabilidad_error < 0.70:
            # ERROR 5: Fecha fuera de rango o formato raro
            usuario["fecha_creacion"] = None


        usuarios.append(usuario)


    return usuarios
