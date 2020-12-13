from .models import Comment, Post
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
        self.fields['body'].widget.attrs.update(style='height: 4em')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
