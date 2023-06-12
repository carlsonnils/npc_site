from django.shortcuts import render

def index(request):
    print(type(render(request=request, template_name='index.html')))
    return render(request=request, template_name='index.html')
