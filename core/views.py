from django.shortcuts import render


# Create you views here.
def home(request):
    return render(request, 'core/home.html')
