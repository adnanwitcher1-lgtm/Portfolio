from django.shortcuts import render
from .models import Project, ProfilePicture

# Create your views here.
def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def home(request):
    projects = Project.objects.all()          # Fetch all projects
    pics = ProfilePicture.objects.all()[:1]       # Fetch all profile pictures
    
    context = {
        'projects': projects,
        'pics': pics
    }
    
    return render(request, 'index.html', context)


def nav(request):
    return render(request, 'nav.html')

def footer(request):
    return render(request, 'footer.html')

 
