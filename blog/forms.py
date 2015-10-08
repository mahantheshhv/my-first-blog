from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','todays_Accomplishment','status','Activities_in_progress','problems')