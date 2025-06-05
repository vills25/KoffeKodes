from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta(object):
        model = Tweet
        fields = ['texts', 'photo']