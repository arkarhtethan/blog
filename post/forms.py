from django import forms
from .models import Comment

class ShareForm(forms.Form):

    name = forms.CharField(max_length=120)

    email = forms.EmailField()

    to = forms.EmailField()

    comment = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.Form):

    name = forms.CharField(max_length=120)

    email = forms.EmailField()

    comment = forms.CharField(widget=forms.Textarea)

class CommentForm(forms.ModelForm):

    class Meta:

        model = Comment

        fields = ('email', 'body')