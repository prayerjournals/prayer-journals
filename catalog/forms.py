
from django import forms
from .models import Note
from django.forms.widgets import ClearableFileInput


class MyImageWidget(ClearableFileInput):
    template_name = "widgets/image_widget.html"


class NoteForm(forms.ModelForm):
    title = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'placeholder': 'Title'}))

    body = forms.CharField(max_length=4000, label="Item Description.", required=False, 
                           widget=forms.Textarea(attrs={'placeholder': 'Start writing here...'}))

    image1 = forms.ImageField(widget=MyImageWidget, label='', required=False)  
 
    class Meta:
        model = Note
        fields = ('title', 'body', 'image1', )
