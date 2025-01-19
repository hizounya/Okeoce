from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306256293',
        'name': 'Darren',
        'class': 'OKE OCE'
    }

    return render(request, "main.html", context)