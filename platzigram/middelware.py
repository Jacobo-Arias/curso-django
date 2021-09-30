from django.shortcuts import redirect
from django.urls import reverse

"""platzigram middelware catalg"""

class ProfileCompletioMiddleware:
    """Profile completion middleware.

    Ensure every user that is interacting with the plataform
    have their profile picture and biography
    """


    def __init__(self,get_response):
        """Middleware initialization"""
        self.get_response = get_response

    def __call__(self,request):
        """Code to be executed for each request
        before the view is called.
        
        Esta parte de código se va a ejecutar cada vez que haya un request

        Y lo que dice es que si tiene sesión iniciada
        y no tiene foto de perfil o biografía lo va a redireccionar
        y además no está en la url de update_profile ni logout
        a la vista de update_profile
        """

        if not request.user.is_anonymous:
            profile = request.user.profile
            if not profile.picture or not profile.biography:
                if request.path not in (reverse('update_profile'),reverse("logout")): 
                    return redirect('update_profile')
        

        response = self.get_response(request)
        return response