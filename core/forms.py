from django import forms
from django.core.mail.message import EmailMessage

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea())

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        content = f'Name: {name}, E-mail: {email}, Subjetc: {subject}, Message: {message}'

        mail = EmailMessage(
            subject=subject,
            body=content,
            from_email='contact@fusion.com.br',
            to=['contact@fusion.com.br',],
            headers={'Reply-To': email}
        )
        mail.send()