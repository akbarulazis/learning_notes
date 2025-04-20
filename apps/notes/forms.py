# notes/forms.py
from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter note title'}),
            'content': forms.Textarea(attrs={'class': 'form-input', 'rows': 10, 'placeholder': 'Write your note here...'}),
            'status': forms.Select(attrs={'class': 'form-input'}),
        }