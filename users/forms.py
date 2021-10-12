""" User forms """

# Django
from django import forms

# Models
from django.contrib.auth.models import User
from users.models import Profile


class ProfileForm(forms.Form):
    """los campos que tendrá el formulario"""

    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()

class SingupForm(forms.Form):
    """form de singup"""

    username = forms.CharField(
        label=False,
        min_length=4,
        max_length=50,
        widget = forms.TextInput(
            attrs = {
                'placeholder':'username',
                'class':'form-coontrol',
                'required':True
            }
        )
    )

    # Los widgets son una representación de django de un elemento html
    # y puede contener ciertas validaciones
    # El widget PasswordInput agrega al campo que es tipo password y no muestra
    # la contraseña
    password = forms.CharField(
        label=False,
        max_length=70,
        widget=forms.PasswordInput(
            attrs = {
                'placeholder':'password',
                'class':'form-coontrol',
                'required':True
            }
        )
    )
    password_confirmation = forms.CharField(
        label=False,
        max_length=70,
        widget=forms.PasswordInput(
            attrs = {
                'placeholder':'confirm password',
                'class':'form-coontrol',
                'required':True
            }
        )
    )

    first_name = forms.CharField(
        label=False,
        min_length=2,
        max_length=50,
        widget = forms.TextInput(
            attrs = {
                'placeholder':'firstname',
                'class':'form-coontrol',
                'required':True
            }
        )
    )
    last_name = forms.CharField(
        label=False,
        min_length=2,
        max_length=50,
        widget = forms.TextInput(
            attrs = {
                'placeholder':'lastname',
                'class':'form-coontrol',
                'required':True
            }
        )
    )

    email = forms.CharField(
        label=False,
        min_length=6,
        max_length=70,
        widget=forms.EmailInput(
            attrs = {
                'placeholder':'email',
                'class':'form-coontrol',
                'required':True
            }
        )
    )


    # Para validar los campos se usa crea una funcion que sea
    # clean_[campo_a_validar]
    def clean_username(self):
        """Username debe ser único."""
        username = self.cleaned_data['username']
        # se usa filter porque si se usa get saltaría una excepcion
        query = User.objects.filter(username=username).exists()
        if query:
            # Django se encarga de levantar la excepción hasta el HTML
            # y de esta forma no nos toca hacerlo manual
            raise forms.ValidationError("Ya existe un perfil con ese username")
        return username
    

    # Cuando se deben validar campos que dependen de otros, 
    # como es el caso de password y password_confirmation se deben
    # hacer en el metodo clean que es el ultimo que es llamado por django
    def clean(self):
        """Veify password confirmacion match."""
        #como no se quiere sobreescribir por completo el metodo
        # traemos los datos que clean traería por defecto
        # con super()

        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError("Las contraseñas no coinciden")
        
        return data
    
    def save(self):
        """Guardar los datos en la base de datos
        create user and profile
        """
        data = self.cleaned_data
        data.pop('password_confirmation')
        
        user = User.objects.create_user(**data)

        profile = Profile(user)

        profile.save()