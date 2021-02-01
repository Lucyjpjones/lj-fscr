from django import forms

QUERIES = (
    ('', 'Select Option'),
    ('SC', 'Strength and conditioning question'),
    ('PR', 'Physiotherapy or rehab question'),
    ('PR', 'More info about our programmes'),
    ('SE', 'Something else'),
)


class ContactForm(forms.Form):
    contact_name = forms.CharField(label='Full Name', max_length=100,
                                   widget=forms.TextInput())
    contact_email = forms.EmailField(label='Email Address',
                                     widget=forms.TextInput())
    query = forms.ChoiceField(label='What does your query relate to?',
                              choices=QUERIES)
    message = forms.CharField(label='What is your message?',
                              widget=forms.Textarea())
