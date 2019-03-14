from django import forms


class BlogPostForm(forms.Form):
    title = forms.CharField(
        label="Job Title:",
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    author = forms.CharField(
        label="Employer Name:",
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    location = forms.CharField(
        label='Job Location:',
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    postion = forms.CharField(
        label="Employer's Current Postion:",
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    benefits = forms.CharField(
        label="Job Benefits:",
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    body = forms.CharField(
        label="Post Body:",
        widget=forms.Textarea(attrs={'class': 'form-control mb-3'}))


class BlogCommentForm(forms.Form):
    title = forms.CharField(
        label="Comment Title:",
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    author = forms.CharField(
        label="Writer's Name:",
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    body = forms.CharField(
        label="Comment Body:",
        widget=forms.Textarea(attrs={'class': 'form-control mb-3'}))