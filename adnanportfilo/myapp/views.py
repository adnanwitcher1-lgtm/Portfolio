from django.shortcuts import render
from django.http import JsonResponse
from .models import Project  # ✅ Sirf Project import kiya

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def home(request):
    # ✅ HANDLE CONTACT FORM (AJAX POST)
    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        print(name, email, subject, message)  # You can save later

        return JsonResponse({
            "status": "success",
            "message": "Message sent successfully!"
        })

    # ✅ NORMAL PAGE LOAD - Sirf Projects
    projects = Project.objects.all()

    context = {
        'projects': projects,
        # 'pics' wala line hata diya
    }

    return render(request, 'index.html', context)

def nav(request):
    return render(request, 'nav.html')

def footer(request):
    return render(request, 'footer.html')