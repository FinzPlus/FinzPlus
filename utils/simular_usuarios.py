from datetime import datetime, timedelta
import random

def generar_usuarios(num_usuarios):

    #Semuilla para generar datos aleatorios

    nombres = ["Juan", "María", "Carlos", "Ana", "Luis", "Sofía", "Miguel", "Laura", "Pedro", "Lucía"]
    apellidos = ["García", "Pérez", "López", "Martínez", "Sánchez", "Gómez", "Díaz", "Fernández", "Romero", "Vargas"]
    dominios=["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "icloud.com"]
    roles_base = ["Admin", "Cliente", "Editor"]
    fechaInicio=datetime(2024,1, 1)
    

    usuarios = []
    for i in range(num_usuarios):
        nombre_completo=f"{random.choice(nombres)} {random.choice(apellidos)}"
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

        if probabilidad_error < 0.20:            
            # ERROR 1: El ID se pierde (Nulo)
            usuario["id_usuario"] = None
            
        elif probabilidad_error < 0.30:
            # ERROR 2: Email mal formado (Sin el @ o con espacios)
            usuario["email"] = usuario["email"].replace("@", " (at) ")
            
        elif probabilidad_error < 0.45:
            # ERROR 3: Nombre en mayúsculas locas o con espacios extras
            usuario["nombre_usuario"] = usuario["nombre_usuario"].upper()
            
        elif probabilidad_error < 0.65:
            # ERROR 4: Rol inexistente
            usuario["rol"] = random.choice(["Desconocido", "Dueño del chuzo"])
            
        elif probabilidad_error < 0.80:
            # ERROR 5: Fecha fuera de rango o formato raro
            usuario["fecha_creacion"] = None


        usuarios.append(usuario)


    return usuarios
