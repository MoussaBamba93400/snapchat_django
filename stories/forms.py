from django import forms
from .models import Story

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['content_url', 'content_image']

    def save(self, commit=True):
        story = super().save(commit=False)
        if commit:
            story.save()
        return story