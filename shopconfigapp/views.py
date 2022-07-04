from django.shortcuts import render

# Create your views here.

def shopconfig(request):
    return render(request, 'shopconfigapp/test.html')