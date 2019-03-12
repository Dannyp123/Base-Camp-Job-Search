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
        label='Current Postion:',
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    body = forms.CharField(
        label="Post Body:",
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))


class BlogCommentForm(forms.Form):
    title = forms.CharField(label="Title:")
    rating = forms.IntegerField(label="Rating:", max_value=5, min_value=1)
    author = forms.CharField(label="Author:")
    body = forms.CharField(
        label="Comment Body:",
        widget=forms.Textarea(attrs={'placeholder': 'Insert comment Here'}))
