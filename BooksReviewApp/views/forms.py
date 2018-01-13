from django import forms
from ..models import BookRequest, Review


class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class BookRequestForm(forms.ModelForm):
    class Meta(object):
        model = BookRequest
        fields = ['writer','book_name']



class ReviewForm(forms.ModelForm):
    review_text =  forms.CharField(label='review_text', widget=forms.Textarea)
    class Meta(object):
        model = Review
        fields = ['book_pk', 'rating']
    
    

    """
        def __init__(self, *args, **kwargs):
            super(ReviewForm , self).__init__(*args, **kwargs)
            self.fields['book_pk'].intial = kwargs['book_pk']
    """
    
    
    
class CommentForm(forms.Form):
    author = forms.CharField(label='author')
    book = forms.CharField(label='book name')
    text = forms.CharField(label='recenzie', widget=forms.Textarea)