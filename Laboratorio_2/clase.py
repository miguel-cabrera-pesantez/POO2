from estudiante import devolverMaterias

def estudianteRegistradoMateria(nombreEstudiante, nombreMateria):
    materias = devolverMaterias(nombreEstudiante)
    
    if materias is None:
        return False

    return nombreMateria in materias