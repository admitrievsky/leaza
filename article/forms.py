from django import forms


class AddForm(forms.Form):
    title = forms.CharField(label='Title')
    author_name = forms.CharField(label='Your name')
    content = forms.CharField(widget=forms.Textarea, label='Content')


class EditForm(forms.Form):
    title = forms.CharField(label='Title')
    content = forms.CharField(widget=forms.Textarea, label='Content')


class CommentAddForm(forms.Form):
    author_name = forms.CharField(label='You name')
    content = forms.CharField(widget=forms.Textarea, label='')
    parent = forms.IntegerField(required=False, widget=forms.HiddenInput)
