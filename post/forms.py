from django import forms

class ShareForm(forms.Form):

    name = forms.CharField(max_length=120)

    email = forms.EmailField()

    to = forms.EmailField()

    comment = forms.CharField(widget=forms.Textarea)

