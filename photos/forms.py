from django import forms;

class PhotoForm(forms.Form):
    title = forms.CharField(max_length=100)
    desc = forms.CharField(max_length=300)
    typeface_id = forms.IntegerField()
    photo = forms.FileField()