from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
class Index(View):
    def get(self, request):
        return render(request, 'inicio/index.html')

# classe para salir del sistema
class Salir(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
               
    # Create your PANEL here.
class Panel(View):
    def get(self, request):
        return render(request, 'inicio/panel.html')
# Create una clase para el login
class Login(View):
    def get(self, request):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/core/login')
    
        form = LoginForm()
        return render(request, 'inicio/login.html',{
            'form': form,
        })
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            logueado = authenticate(request,username=username, password=password)
            if logueado is not None:
                login(request, logueado)
                return HttpResponseRedirect('/core/panel')
            else:
                return render(request, 'inicio/login.html', {
                    'form': form,
                })

  
#-----------------------Agregar Estudiante---------------------------------------------------------------------------  

class ListarEstudiantes(View):
    def get(self, request):
        #utilizar el orm de django
        estudiantes = Estudiante.objects.all()
        print(estudiantes)
        return render(request, 'estudiantes/listar_estudiantes.html', {
            'estudiantes': estudiantes,
            })
class BuscarEstudiante(View):
    def get(self, request, id_estudiante):
        estudiante = Estudiante.objects.get(id=id_estudiante),
        print(estudiante)
        return render(request, 'estudiantes/ver_estudiante.html', {
            'estudiante': estudiante,
        })

class AgregarEstudiante(View):
    def get(self, request):
       form = EstudianteForm() 
       return render(request, 'estudiantes/agregar_estudiante.html', {
           'form': form})
    def post(self, request):
        #leemos el formulario del navegador
        form = EstudianteForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            primer_nombre = form.cleaned_data['primer_nombre']
            segundo_nombre = form.cleaned_data['segundo_nombre']
            primerApellido = form.cleaned_data['primerApellido']
            segundoApellido = form.cleaned_data['segundoApellido']
            cedula_ruc = form.cleaned_data['cedula_ruc']
            fechaNacimiento = form.cleaned_data['fechaNacimiento']
            telefono = form.cleaned_data['telefono']
            celular = form.cleaned_data['celular']
            correo = form.cleaned_data['correo']
            estadoCivil = form.cleaned_data['estadoCivil']
            sexo = form.cleaned_data['sexo']
            nacionalidad = form.cleaned_data['nacionalidad']
            correo_institucional = form.cleaned_data['correo_institucional']
            codigo_estudiante = form.cleaned_data['codigo_estudiante']
            # crear el estudiante en la base de datos

            estudiante = Estudiante(
            primer_nombre = primer_nombre,
            segundo_nombre = segundo_nombre,
            primerApellido = primerApellido,
            segundoApellido = segundoApellido,
            cedula_ruc = cedula_ruc,
            fechaNacimiento = fechaNacimiento,
            telefono = telefono,
            celular = celular,
            correo = correo,
            estadoCivil = estadoCivil,
            sexo = sexo,
            nacionalidad = nacionalidad,
            correo_institucional = correo_institucional,
            codigo_estudiante = codigo_estudiante,
            )
            estudiante.save()
            form = EstudianteForm()
            return HttpResponseRedirect('listar_estudiantes')
        else:
            return render(request, 'estudiantes/nueco_estudiante.html', {
                'form': form,
            })
class EditarEstudiante(View):
    def get(self, request, id_estudiante):
        estudiante = Estudiante.objects.get(id=id_estudiante)
        form = EstudianteForm(instance=estudiante)
        return render(request, 'estudiantes/agregar_estudiante.html', {'form': form})

    def post(self, request, id_estudiante):
        #LEEMOS EL FORMULARIO DEL NAVEGADOR
        form = EstudianteForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            primer_nombre = form.cleaned_data['primer_nombre']
            segundo_nombre = form.cleaned_data['segundo_nombre']
            primerApellido = form.cleaned_data['primerApellido']
            segundoApellido = form.cleaned_data['segundoApellido']
            tipoDocumento = form.cleaned_data['tipoDocumento']
            cedula_ruc = form.cleaned_data['cedula_ruc']
            fechaNacimiento = form.cleaned_data['fechaNacimiento']
            genero = form.cleaned_data['genero']
            telefono = form.cleaned_data['telefono']
            celular = form.cleaned_data['celular']
            correo = form.cleaned_data['correo']
            estadoCivil = form.cleaned_data['estadoCivil']
            sexo = form.cleaned_data['sexo']
            nacionalidad = form.cleaned_data['nacionalidad']
            correo_institucional = form.cleaned_data['correo_institucional']
            codigo_estudiante = form.cleaned_data['codigo_estudiante']

            #ACTUALIZAR EL ESTUDIANTE EN LA BASE DE DATOS
            estudiante = Estudiante.objects.get(id=id_estudiante)
            estudiante.primer_nombre=primer_nombre
            estudiante.segundo_nombre=segundo_nombre
            estudiante.primerApellido=primerApellido
            estudiante.segundoApellido=segundoApellido
            estudiante.tipoDocumento=tipoDocumento
            estudiante.cedula_ruc=cedula_ruc
            estudiante.fechaNacimiento=fechaNacimiento
            estudiante.genero=genero
            estudiante.telefono=telefono
            estudiante.celular=celular
            estudiante.correo=correo
            estudiante.estadoCivil=estadoCivil
            estudiante.sexo=sexo
            estudiante.nacionalidad=nacionalidad
            estudiante.correo_institucional=correo_institucional
            estudiante.codigo_estudiante=codigo_estudiante
        
            estudiante.save()
            form = EstudianteForm()
            return HttpResponseRedirect('/core/lista_estudiantes')
        else:
            return render(request, 'estudiantes/nuevo_estudiante.html', {'form': form})

#ELIMINAR ESTUDIANTE

class EliminarEstudiante(View):
    def get(self, request, id_estudiante):
        estudiante = Estudiante.objects.get(id=id_estudiante)
        estudiante.delete()
        return HttpResponseRedirect('/core/lista_estudiantes')
class MostrarEstudiante(View):
    def get(self, request, id_estudiante):
        estudiante = Estudiante.objects.get(id=id_estudiante)
        form = EstudianteForm(instance=estudiante)
        return render(request, 'estudiantes/ver_estudiantes.html', {'form': form})
 #-------------------------------------------Agregar Carrera----------------------------------------------
class AgregarCarrera(View):
    def get(self, request):
        form = CarreraForm()
        return render(request, 'carreras/agregar_carrera.html', {
            'form': form
        })

    def post(self, request):
        form = CarreraForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            nombres = form.cleaned_data['nombres']
            descripcion = form.cleaned_data['descripcion']
            modalidad = form.cleaned_data['modalidad']
            anios_estudio = form.cleaned_data['anios_estudio']

            # Crear la carrera en la base de datos
            carrera = Carrera(
                nombres=nombres,
                descripcion=descripcion,
                modalidad=modalidad,
                anios_estudio=anios_estudio,
            )
            carrera.save()
            return redirect(reverse('lista_carreras'))
        else:
            return render(request, 'carreras/agregar_carrera.html', {
                'form': form
            })
            
class EditarCarreras(View):
    def get(self, request, id_carrera):
        carrera = Carrera.objects.get(id=id_carrera)
        form = CarreraForm(instance=carrera)
        return render(request, 'carreras/agregar_carrera.html', {'form': form})
    
    def post(self, request, id_carrera):
        form = CarreraForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            nombres = form.cleaned_data['nombres']
            descripcion = form.cleaned_data['descripcion']
            modalidad = form.cleaned_data['modalidad']
            anios_estudio = form.cleaned_data['anios_estudio']
            
            # Actualizar la carrera en la base de datos
            carrera = Carrera.objects.get(id=id_carrera)
            carrera.nombres=nombres
            carrera.descripcion=descripcion
            carrera.modalidad=modalidad
            carrera.anios_estudio=anios_estudio
            
            carrera.save()
            return redirect(reverse('lista_carreras'))
        

class ListarCarreras(View):
    def get(self, request):
        #utilizar el orm de django
        carreras = Carrera.objects.all()
        print(carreras)
        return render(request, 'carreras/lista_carreras.html', {
                        'carreras': carreras,
                    })
        
        
        
    
 #-------------------------------------------Agregar Asignatura----------------------------------------------
class AgregarAsignatura(View):
    def get(self, request):
        form = AsignaturaForm()
        return render(request, 'asignaturas/agregar_asignatura.html', {
            'form': form
        })
    def post(self, request):
        form = AsignaturaForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            codigo = form.cleaned_data['codigo']
            nombre = form.cleaned_data['nombre']
            creditos = form.cleaned_data['creditos']
            horasDocencia = form.cleaned_data['horasDocencia']
            horasPracticas = form.cleaned_data['horasPracticas']
            horasAutonomo = form.cleaned_data['horasAutonomo']
            estructuraCurricular = form.cleaned_data['estructuraCurricular']
            # Crear la carrera en la base de datos
            asignatura = Asignatura(
            codigo=codigo,
            nombre=nombre,
            creditos=creditos,
            horasDocencia=horasDocencia,
            horasPracticas=horasPracticas,
            horasAutonomo=horasAutonomo,
            estructuraCurricular=estructuraCurricular,
            )
            asignatura.save()
            return redirect(reverse('lista_asignaturas'))
        else:
            return render(request, 'asignaturas/agregar_asignatura.html', {
                'form': form
            })           
        #======================================configuracion de la asignatura================================================
class ListarAsignatura(View):
    def get(self, request):
        asignaturas = Asignatura.objects.all()  # Accede al modelo Asignatura correctamente
        return render(request, 'asignaturas/lista_asignaturas.html', {'asignaturas': asignaturas})
    
#-------------------------------------------Agregar Semestre----------------------------------------------
class AgregarSemestre(View):
    def get(self, request):
        form = SemestreForm()
        return render(request, 'semestres/lista_semestres.html', {
            'form': form
        })
    def post(self, request):
        form = SemestreForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            malla = form.cleaned_data['malla']
           
            # Crear la semestre en la base de datos
            semestre = Semestre(
            malla= malla,
           
            )
            semestre.save()
            return redirect(reverse('lista_semestres'))
        else:
            return render(request, 'semestres/lista_semestres.html', {
                'form': form
            })
        #======================================configuracion de la asignatura================================================
class ListarSemestre(View):
    def get(self, request):
        semestres = Semestre.objects.all()  # Accede al modelo Asignatura correctamente
        return render(request, 'semestres/lista_semestres.html', {'semestres': semestres})
     #======================================configuracion de la carrera===============================================
class ListarDocente(View):
    def get(self, request):
        #utilizar el orm de django
        docentes = Docente.objects.all()
        print(docentes)
        return render(request, 'docentes/listar_docentes.html', {
                        'carreras': docentes,
                    })