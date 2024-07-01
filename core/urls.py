from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index.as_view(), name="index"), #EL NAME ES EL NOMBRE DE LA RUTA
    path("login", views.Login.as_view(), name="login"), 
    path("panel", views.Panel.as_view(), name="panel"), 
    path("salir", views.Salir.as_view(), name="salir"),
    #rutas estudiantes
    path("lista_estudiantes", views.ListarEstudiantes.as_view(), name="lista_estudiantes"),
    path("ver_estudiantes/<int:id_estudiante>", views.ListarEstudiantes.as_view(), name="ver_estudiantes"),
    path("actualizar_estudiante/<int:id_estudiante>", views.EditarEstudiante.as_view(), name="actualizar_estudiante"),
    path("eliminar_estudiante/<int:id_estudiante>", views.EditarEstudiante.as_view(), name="eliminar_estudiante"),
    #rutas 
    path("agregar_estudiante", views.AgregarEstudiante.as_view(), name="agregar_estudiante"),
    #rutas carreras
    path("lista_carreras", views.ListarCarreras.as_view(), name="lista_carreras"),
    path("ver_estudiantes/<int:id_carrera>", views.ListarCarreras.as_view(), name="ver_estudiantes"),
    path("actualizar_carrera/<int:id_carrera>", views.EditarCarreras.as_view(), name="actualizar_carrera"),
    path("eliminar_carrera/<int:id_carrera>", views.EditarCarreras.as_view(), name="eliminar_carrera"),
    #rutas asignaturas
    path("lista_asignaturas", views.ListarAsignatura.as_view(), name="lista_asignaturas"),
    path("ver_asignatura", views.ListarAsignatura.as_view(), name="ver_asignatura"),
    path("agregar_asignatura", views.AgregarAsignatura.as_view(), name="agregar_asignatura"),
    #rutas semestres
    path("lista_semestres", views.ListarSemestre.as_view(), name="lista_semestres"),
    path("ver_semestres", views.ListarSemestre.as_view(), name="ver_semestre"),
    path("agregar_semestre", views.AgregarSemestre.as_view(), name="agregar_semestre"),
 #rutas semestres
    path("listar_docentes", views.ListarDocente.as_view(), name="lista_semestres"),
 
]