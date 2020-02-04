from django import forms 
from home import models
  
class ImgForm(forms.ModelForm): 
  
    class Meta: 
        model = models.Image
        fields = ['Img']