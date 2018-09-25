from django import forms


class NameForm(forms.Form):
    user_name = forms.CharField(label='Name', max_length=255)
