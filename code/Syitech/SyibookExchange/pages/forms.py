from django import forms
from .models import *


class PostForm(forms.ModelForm):
    content = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={"placeholder": "There is a higher chance of selling your product if you mention the following: condition, year bought, your contact info, or anything else that’s important/relevant", }
        ),
    )

    class Meta:
        model = Post
        fields = ['title',
                  'author', 'price', 'content', 'image']
