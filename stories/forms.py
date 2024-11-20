from django import forms
from .models import Story

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['description', 'content_image']
        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description de la story',
                'style': 'width: 100%; margin-bottom: 10px;'
            }),
            'content_image': forms.FileInput(attrs={
                'class': 'form-control',
                'style': 'margin-top: 10px;'
            }),
        }

    def save(self, commit=True):
        story = super().save(commit=False)
        if commit:
            story.save()
        return story