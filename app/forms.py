from django import forms


class BlogPostForm(forms.Form):
    image = forms.URLField(
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': "URL"
        }))
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': "Title"
        }))
    companyName = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': "Name"
        }))
    salary = forms.IntegerField(
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': "150000"
        }))
    email = forms.EmailField(
        error_messages={'required': 'Please enter your email'},
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': "johnDoe@fakemail.com"
        }))

    phoneNum = forms.RegexField(
        error_messages={'required': 'Please enter your phone number'},
        regex=r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$',
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-5',
            'placeholder': "(662) 999-2323"
        }))
    author = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-5',
            'placeholder': "Author's name"
        }))
    streetNum = forms.IntegerField(
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': "123"
        }))
    streetName = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': "Evergreen Street"
        }))
    townName = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': "Oakland"
        }))
    state = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': "OK"
        }))
    zipCode = forms.IntegerField(
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-5',
            'placeholder': "99834"
        }))
    postion = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': "Postion"
        }))
    benefits = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': "Benefits"
        }))
    body = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control mb-3',
            'placeholder': "Description"
        }))

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