from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.

class Index(TemplateView):
    template_name = 'home/index.html'



def Upload(request):
    image = request.POST.get('image')

    return render(request, 'home/upload_image.html')
    
    