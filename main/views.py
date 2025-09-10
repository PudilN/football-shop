from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app' : 'Chill Kicks',
        'name': 'Ainur Fadhil',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)