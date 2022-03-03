from django import forms


class FileForm(forms.Form):
    file = forms.FileField(
        # support multilple file to upload
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
        label='Please choose your Files',
    )