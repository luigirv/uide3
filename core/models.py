from django.db import models
from datetime import date

# Create your models here.

class Carrera(models.Model):
    nombres = models.CharField(verbose_name="Nombre de la carrera", max_length=50)
    descripcion = models.CharField(verbose_name="Descripcion de la carrera", max_length=250)
    modalidad = models.CharField(verbose_name="Modalidad de la carrera", max_length=50)
    anios_estudio = models.IntegerField(verbose_name="Anios de la carrera")
    # agregamos la relacion de muchos a muchos 
    
    
    def __str__(self):
        return self.nombres
    
class Malla(models.Model):
    nombre = models.CharField(verbose_name="Nombre de la malla", max_length=50)
    fechaAprobacion = models.DateField(verbose_name="Fecha de aprobacion", auto_now_add=True)
    aniosAprobados = models.IntegerField(verbose_name="Anios de vgencia de la malla")
    fechaCreacion = models.DateField(verbose_name="Fecha de creacion", auto_now_add=True)
    #tengo una referencia la carrera
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, verbose_name="Agregar Carrera", null= True, blank = True)
    semestres = models.ManyToManyField("Semestre",verbose_name="Agregar Semestre", related_name= "Semestre", null = True,blank=True)



    def __str__(self):
        return f"La Malla {self.nombre} ha sido aprobada por el tiempo de {self.aniosAprobados} anios"
    
class Semestre(models.Model):
    nombre = models.CharField(verbose_name="Nombre del semestre", max_length=50)
    numeroSemestre = models.IntegerField(verbose_name="Numero de semestre")
    #relacion con la malla
    malla = models.ForeignKey(Malla, on_delete=models.CASCADE, verbose_name="Agregar la malla a la que pertenece el semestre", null=True,blank=True)

    def __str__(self):
        return f"El semestre {self.nombre} tiene el numero {self.numeroSemestre}"

opciones_estructura_curricular = [
    ("1", "Unidad Basica"),
    ("2", "Unidad Profesional"),
    ("3", "Unidad de integracion curricular"),
]

class Asignatura(models.Model):
    codigo = models.CharField(verbose_name="Codigo de las asignatura", max_length=10)
    nombre = models.CharField(verbose_name="Nombre de la asignatura", max_length=100)
    creditos = models.IntegerField(verbose_name="Numero de creditos")
    horasDocencia = models.IntegerField(verbose_name="Numero de horas de docencia")
    horasPracticas = models.IntegerField(verbose_name="Numero de horas de practicas")
    horasAutonomo = models.IntegerField(verbose_name="Numero de horas de autonomo")
    estructuraCurricular = models.CharField(verbose_name="Estructura Curriculas", max_length=100, choices=opciones_estructura_curricular)

    #relacion con el semestre
    semestre = models.ForeignKey("Semestre", on_delete=models.PROTECT)
    #relacion con la malla
    malla = models.ManyToManyField("Malla", verbose_name="Selecciona las mallas a las que tiene acceso las asignaturas")
    

    def __str__(self):
        return f"La asignatura {self.nombre} tiene el codigo {self.codigo}"
    

class Paralelo(models.Model):
    nombre = models.CharField(verbose_name="Nombre del paralelo", max_length=50)
    numeroParalelo = models.IntegerField(verbose_name="Numero de paralelo")
    def __str__(self):
        return f"El paralelo {self.nombre} - {self.numeroParalelo}"

opcion_dia = [
    ("0","Domingo"),
    ("1","Lunes"),
    ("2","Martes"),
    ("3","Miercoles"),
    ("4","Jueves"),
    ("5","Viernes"),
    ("6","Sabado"),
]
class Horario(models.Model):
    dia = models.CharField(verbose_name="Dia de la semana", max_length=10, choices=opcion_dia)
    horaInicio = models.TimeField(verbose_name="Hora de inicio")
    horaFin = models.TimeField(verbose_name="Hora de fin")
    numeroHoras = models.IntegerField(verbose_name="numero de horas")
    def __str__(self):
        return f"dia: {self.dia} i: {self.horaInicio} f: {self.horaFin}"
    
class Aula(models.Model):
    nombre = models.CharField(verbose_name="Nombre del aula", max_length=50)
    capacidad = models.IntegerField(verbose_name="Capacidad del aula")
    def __str__(self):
        return self.nombre

opcion_tipo_doc = [("1","Cedula"),("2","RUC"),("3","Pasaporte"),("4","DNI")]
opcion_genero = [("1","Masculino"),("2","Femenino"),("3","Otro")]
opcion_sexo = [("1","Hombre"),("2","Mujer")]
opcion_estado_civil = [
    ("1","Soltero"),
    ("2","Casado"),
    ("3","Viudo"),
    ("4","Union Libre")
]
class Persona(models.Model):
    primer_nombre = models.CharField(verbose_name="Primer nombre de la persona", max_length=30)
    segundo_nombre = models.CharField(verbose_name="Segundo nombre de la persona", max_length=30)
    primerApellido = models.CharField(verbose_name="Primer apellido de la persona", max_length=30)
    segundoApellido = models.CharField(verbose_name="Segundo apellido de la persona", max_length=30)
    tipoDocumento = models.CharField(verbose_name="Tipo de documento a registrar", max_length=30, choices=opcion_tipo_doc)
    cedula_ruc = models.CharField(verbose_name="Numero de identificacion", max_length=13)
    fechaNacimiento = models.DateField(verbose_name="Fecha de nacimiento")
    genero = models.CharField(verbose_name="Slecciona el genero", max_length=30, choices=opcion_genero)
    telefono = models.CharField(verbose_name="Telefono de casa", max_length=30)
    celular = models.CharField(verbose_name="Celular de la persona", max_length=30)
    correo = models.EmailField(verbose_name="Correo personal", max_length=30)
    estadoCivil = models.CharField(verbose_name="Estado civil", max_length=30, choices=opcion_estado_civil)
    sexo = models.CharField(verbose_name="Seleccione el sexo", max_length= 30, choices=opcion_sexo)
    nacionalidad = models.CharField(verbose_name="De que pais viene", max_length=30)
    def __str__(self):
        return f"{self.primer_nombre} {self.primerApellido} - {self.cedula_ruc}"

# en python de colocar metodos generales
def metodo():
    pass
class Estudiante(Persona):
    correo_institucional = models.EmailField(verbose_name="Correo Institucional", max_length=100)
    codigo_estudiante = models.CharField(verbose_name="Codigo de estudiante", max_length=6)
    def __str__(self):
        return f"Estudiante: {self.primer_nombre} {self.primerApellido} - {self.cedula_ruc}"
    def edad(self):
        hoy = date.today()
        edad = hoy.year - self.fechaNacimiento.year
        return edad

class Administrativo(Persona):
    correo_institucional = models.EmailField(verbose_name="Correo Institucional", max_length=100)
    def __str__(self):
        return f"Administrativo: {self.primer_nombre} {self.primerApellido} - {self.cedula_ruc}"

class Docente(Persona):
    correo_institucional = models.EmailField(verbose_name="Correo Institucional", max_length=100)
    def __str__(self):
        return f"Docente: {self.primer_nombre} {self.primerApellido} - {self.cedula_ruc}"
    
class PeriodoAcademico(models.Model):
    nombre = models.CharField(verbose_name="Nombre del periodo academico", max_length=100)
    fechaInicio = models.DateField(verbose_name="Fecha de inicio")
    fechaFin = models.DateField(verbose_name="Fecha de fin")
    def __str__(self):
        return f"Periodo academico: {self.nombre} - {self.fechaInicio} - {self.fechaFin}"

opcion_tipoPago = [("1","Contado"),("2","Credito"),("3","Transferencia")]
opcion_tipoMatricula = [("1","Ordinaria"),("2","Extraordinaria"),("3","Especial")] 
class Matricula(models.Model):
    codigo = models.CharField(verbose_name="Codigo de matricula", max_length=8)
    tipoPago = models.CharField(verbose_name="Tipo de pago", max_length=60, choices=opcion_tipoPago)
    montoPago = models.DecimalField(verbose_name="Monto de pago", max_digits=10, decimal_places=2)
    tipoMatricula = models.CharField(verbose_name="Tipo matricula", max_length=60, choices=opcion_tipoMatricula)
    # atributos relaciones
    estudiante = models.ForeignKey("Estudiante", on_delete=models.CASCADE)
    periodoAcademico = models.ForeignKey("PeriodoAcademico", on_delete=models.CASCADE)
    paralelo = models.ForeignKey("Paralelo", on_delete=models.CASCADE)
    carrera = models.ForeignKey("Carrera", on_delete=models.CASCADE)
    semestre = models.ForeignKey("Semestre", on_delete=models.CASCADE)
    def __str__(self):
        return self.codigo

class MatriculaAsignatura(models.Model):
    matricula = models.ForeignKey("Matricula", on_delete=models.CASCADE)
    asignatura = models.ForeignKey("Asignatura", on_delete=models.CASCADE)

class AsignaturaPareleloAula(models.Model):
    asignatura = models.ForeignKey("Asignatura", on_delete=models.CASCADE)
    paralelo = models.ForeignKey("Paralelo", on_delete=models.CASCADE)
    aula = models.ForeignKey("Aula", on_delete=models.CASCADE)
    horario = models.ForeignKey("Horario", on_delete=models.CASCADE)
    docente = models.ForeignKey("Docente", on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.asignatura} - {self.paralelo} - {self.aula} - {self.horario} - {self.docente}"


