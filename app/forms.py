from django import forms


class BlogPostForm(forms.Form):
    image = forms.URLField(
        label="User Image:",
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    title = forms.CharField(
        label="Job Title:",
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    companyName = forms.CharField(
        label="Company Name:",
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    author = forms.CharField(
        label="Employer Name:",
        widget=forms.TextInput(attrs={'class': 'form-control mb-5'}))
    streetNum = forms.CharField(
        label='Street number:',
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    streetName = forms.CharField(
        label='Street name:',
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    townName = forms.CharField(
        label='Town Name:',
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    state = forms.CharField(
        label='State:',
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    zipCode = forms.CharField(
        label="Zip Code: ",
        widget=forms.TextInput(attrs={'class': 'form-control mb-5'}))
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