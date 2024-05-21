from django import forms

class HelloForm(forms.Form):
    data = [("one", "item 1"),
            ("two", "item 2"),
            ("three", "item 3")]
    choice = forms.ChoiceField(label='choice',choices=data)

class SessionForm(forms.Form):
    session = forms.CharField(label='session',required=False,widget=forms.TextInput(attrs={'class':'form-control'}))