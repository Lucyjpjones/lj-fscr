from .models import Comment, Thread
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
        self.fields['body'].widget.attrs.update(style='height: 4.5em')


class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['topic', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
