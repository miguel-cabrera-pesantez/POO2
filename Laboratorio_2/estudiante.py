estudiantesMaterias = {
    "Daniel": ["Matematica", "Computacion"],
    "Maria": ["Matematica", "Fisica"]
}

def devolverMaterias(nombre_estudiante):
    try:
        return estudiantesMaterias[nombre_estudiante]
    except KeyError:
        print(f"Error: El estudiante '{nombre_estudiante}' no está registrado.")
        return None