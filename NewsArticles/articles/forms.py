from django import forms

class UploadImageForm(forms.Form):
    imgfile         =   forms.ImageField(label = 'Choose your image',
                                          help_text = 'The image should have one face in it.')