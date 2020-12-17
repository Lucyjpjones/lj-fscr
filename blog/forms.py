from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

    # https://stackoverflow.com/questions/11472495/remove-labels-in-a-django-crispy-forms
    def __init__(self, *args, **kwargs):
        ''' remove any labels here if desired
        '''
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields['body'].label = ''

        # https://stackoverflow.com/questions/38684753/django-reducing-the-size-of-input-box-in-crispy-forms
        self.fields['body'].widget.attrs.update(style='height: 5.5em')
