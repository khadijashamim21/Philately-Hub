from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth import get_user_model
User = get_user_model()


# Password for test user is Harry$$$***)))

# Create your views here.

from django.template import TemplateDoesNotExist

def index(request):
    template_name = 'home/login.html'  # Adjusted to correct path
    
    try:
        # Try to load the template to see if it exists
        from django.template.loader import get_template
        get_template(template_name)
        print(f"Template '{template_name}' found.")
    except TemplateDoesNotExist:
        print(f"Template '{template_name}' does not exist.")

    return render(request, template_name)



def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'home/login.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")
