from django import forms    
from .models import *
from django.forms.widgets import DateInput
class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'
        labels = {
            'primer_nombre': 'Ingresar el Primer Nombre',
            'segundo_nombre': 'Ingresar el Segundo Nombre',
            'primerApellido': 'Ingresa el Primer Apellido',
            'segundoApellido': 'Ingresa el segundo Apellido',
            'cedula_ruc': 'Ingresa tu Cedula o RUC',
            'telefono': 'Ingresa tu numero de Telefono',
            'celular': 'Ingresa tu numero de Celular',
            'correo': 'Ingresa tu Correo',
            'estadoCivil': 'Ingresa tu Estado Civil',
            'sexo': 'Ingresa tu sexo',
            'nacionalidad': 'Ingresa tu Nacionalidad',
            'correo_institucional': 'Ingresa tu correo Institucional',
            'codigo_estudiante': 'Ingresa el codigo de estudiante',
        }
        widgets = {
            'fechaNacimiento': DateInput(attrs={'type': 'date'}),
        }
class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = '__all__'
        labels = {
            'nombres': 'Ingresar el Nombres',
            'descripcion': 'Ingresar la Descripcion',
            'modalidad': 'Ingresa la modalidad',
            'anios_estudio': 'Ingresa anios de estudio',
        }
        #----------------------------Asignatura--------------------------------------------------
class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = '__all__'
        labels = {
            'codigo': 'codigo',
            'nombre':'nombre',
            'creditos':'creditos',
            'horasDocencia':'horasDocencia',
            'horasPracticas':'horasPracticas',
            'horasAutonomo':'horasAutonomo',
            'estructuraCurricular':'estructuraCurricular',
        }
        #----------------------------Semestre--------------------------------------------------
class SemestreForm(forms.ModelForm):
    class Meta:
        model = Semestre
        fields = '__all__'
        labels = {
            'malla': 'malla',
            
        }    
        #----------------------------Docente--------------------------------------------------
class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'
        labels = {
            'correo_institucional': 'correo_institucional',
        }  
  #----------------------------Docente--------------------------------------------------
class LoginForm(forms.Form):
          label="Tu nombre de usuario",
          widget= forms.TextInput(
              attrs={
                  'placeholder':'Tu nombre de usuario',
                  'class': 'form-control underline mb-3', 
                  'id': 'usuarname',
                  'type': 'text',
                  }
          )