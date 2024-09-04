from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306223446',
        'name': 'Nabilah Roslita Utami',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)