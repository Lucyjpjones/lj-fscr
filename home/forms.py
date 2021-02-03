from django import forms

QUERIES = (
    ('', 'Select Option'),
    ('Strength and conditioning', 'Strength and conditioning question'),
    ('Physiotherapy or rehab', 'Physiotherapy or rehab question'),
    ('More info about programmes', 'More info about our programmes'),
    ('Something else', 'Something else'),
)


class ContactForm(forms.Form):
    contact_name = forms.CharField(label='Full Name', max_length=100,
                                   widget=forms.TextInput())
    contact_email = forms.EmailField(label='Email Address',
                                     widget=forms.TextInput())
    query = forms.ChoiceField(label='What does your query relate to?',
                              widget=forms.Select(
                                attrs={'class': 'selectpicker'}),
                              choices=QUERIES)
    message = forms.CharField(label='What is your message?',
                              widget=forms.Textarea(
                                  attrs={'style': 'height:6em'}))
