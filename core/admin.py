from django.contrib import admin
# Habilitar las clases que se visualicen en la interfaz
from .models import Carrera, Malla, Semestre, Asignatura, Paralelo, Horario, Aula, Estudiante, Docente, Administrativo, Matricula, PeriodoAcademico, AsignaturaPareleloAula
# Register your models here.

class CarreraAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'modalidad', 'anios_estudio')
    search_fields = ('nombres',)
    ordering = ('nombres','modalidad',)
class MallaAdmin(admin.ModelAdmin):
    list_display = ('nombre','fechaAprobacion','carrera')
    search_fields = ('nombre','carrera',)
    ordering = ('nombre','fechaAprobacion',)
    filter_horizontal = ('semestres',)

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('primerApellido', 'segundoApellido', 'primer_nombre', 'cedula_ruc', 'estadoCivil', 'edad',)
    search_fields = ('primerApellido', 'primer_nombre', 'cedula_ruc',)
    ordering = ('primerApellido', 'primer_nombre',)
    list_filter = ('primerApellido','primer_nombre',)
    list_editable = ('estadoCivil',)
    fieldsets = (
        ('INFORMACION INSTITUCIONAL ', {
            'fields': ('correo_institucional','codigo_estudiante',)  
        }),
        ('INFORMACION PERSONAL ', {
            'fields': ('primerApellido','segundoApellido', 'primer_nombre','segundo_nombre', 'tipoDocumento','cedula_ruc',)  
        }),
        ('Datos Personales', {
             'fields': ('estadoCivil', 'fechaNacimiento', 'genero', 'sexo','nacionalidad')
        }),
        ('Datos de contacto', {
            'fields': ('telefono', 'celular', 'correo',)
        }),
       
    )
    

class DocenteAdmin(admin.ModelAdmin):
    list_display = ('primerApellido', 'segundoApellido', 'primer_nombre', 'cedula_ruc', 'estadoCivil')
    search_fields = ('primerApellido', 'primer_nombre', 'cedula_ruc',)
    ordering = ('primerApellido', 'primer_nombre',)
    list_filter = ('primerApellido','primer_nombre',)
    fieldsets = (
        ('INFORMACION INSTITUCIONAL ', {
            'fields': ('correo_institucional',)  
        }),
        ('INFORMACION PERSONAL ', {
            'fields': ('primerApellido','segundoApellido', 'primer_nombre','segundo_nombre', 'tipoDocumento','cedula_ruc',)  
        }),
        ('Datos Personales', {
             'fields': ('estadoCivil', 'fechaNacimiento', 'genero', 'sexo','nacionalidad')
        }),
        ('Datos de contacto', {
            'fields': ('telefono', 'celular', 'correo',)
        }),
       
    )


class AdministrativoAdmin(admin.ModelAdmin):
    list_display = ('primerApellido', 'segundoApellido', 'primer_nombre', 'cedula_ruc', 'estadoCivil')
    search_fields = ('primerApellido', 'primer_nombre', 'cedula_ruc',)
    ordering = ('primerApellido', 'primer_nombre',)
    list_filter = ('primerApellido','primer_nombre',)
    fieldsets = (
        ('INFORMACION INSTITUCIONAL ', {
            'fields': ('correo_institucional',)  
        }),
        ('INFORMACION PERSONAL ', {
            'fields': ('primerApellido','segundoApellido', 'primer_nombre','segundo_nombre', 'tipoDocumento','cedula_ruc',)  
        }),
        ('Datos Personales', {
             'fields': ('estadoCivil', 'fechaNacimiento', 'genero', 'sexo','nacionalidad')
        }),
        ('Datos de contacto', {
            'fields': ('telefono', 'celular', 'correo',)
        }),
       
    )


admin.site.register(Carrera, CarreraAdmin)
admin.site.register(Malla, MallaAdmin)
admin.site.register(Semestre)
admin.site.register(Asignatura)
admin.site.register(Paralelo)
admin.site.register(Horario)
admin.site.register(Aula)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Docente, DocenteAdmin)
admin.site.register(Administrativo, AdministrativoAdmin)
admin.site.register(Matricula)
admin.site.register(PeriodoAcademico)
admin.site.register(AsignaturaPareleloAula)

