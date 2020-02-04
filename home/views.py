from django.shortcuts import render

from django.views.generic import TemplateView
import os

from home import forms

# Create your views here.

class Index(TemplateView):
    template_name = 'home/index.html'



def Upload(request):
    # image = request.POST.get('image')



    if request.method == 'POST': 
        form = forms.ImgForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            os.system("python darknet/r2unfile.py")

            return render(request, 'home/upload_image.html') 
    else: 
        form = forms.ImgForm() 
    return render(request, 'home/upload_image.html', {'form' : form})

    # print(image)


    # return render(request, 'home/upload_image.html')


    
    