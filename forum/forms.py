from .models import Reply, Thread
from django import forms


class CommentForm(forms.ModelForm):
    """
    Form to add comment to thread
    """
    class Meta:
        model = Reply
        fields = ['body']

    def __init__(self, *args, **kwargs):
        """
        Labels removed from body field on comment form
        [Code taken from 'https://stackoverflow.com/questions/
        11472495/remove-labels-in-a-django-crispy-forms']
        Reduced height of body field on comment form
        [Code taken from 'https://stackoverflow.com/questions/
        38684753/django-reducing-the-size-of-input-box-in-crispy-forms']
        """
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields['body'].label = ''

        self.fields['body'].widget.attrs.update(style='height: 4.5em')


class ThreadForm(forms.ModelForm):
    """
    Form to add thread to forum
    """
    class Meta:
        model = Thread
        fields = ['topic', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
