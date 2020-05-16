from django import forms

from .models import Cart


class CartForm(forms.ModelForm):

    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'type title'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'row': 15}))
    price = forms.DecimalField(required=True, initial=12.34)
    emails = forms.CharField(required=True)

    class Meta:
        model = Cart
        fields = [
            'title',
            'description',
            'price',
            'emails'
        ]

    def clean_emails(self, *args, **kwargs):
        emails = self.cleaned_data.get('emails')
        if not emails.endswith('.edu'):
            raise forms.ValidationError('This is not the type of emails')
        else:
            return emails
