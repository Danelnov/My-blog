from django import forms
from django.db.models import fields
from .models import Post


# !if you try to upload an image in the form, it will not be read
# FIXME make the form load the images
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'category', 'image')