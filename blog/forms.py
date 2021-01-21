from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

    def __init__(self, *args, **kwargs):
        ''' Labels removed from body field on comment form
        [Code taken from 'https://stackoverflow.com/questions/
        11472495/remove-labels-in-a-django-crispy-forms']
        Reduced height of body field on comment form
        [Code taken from 'https://stackoverflow.com/questions/
        38684753/django-reducing-the-size-of-input-box-in-crispy-forms']
        '''
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields['body'].label = ''

        self.fields['body'].widget.attrs.update(style='height: 5.5em')
