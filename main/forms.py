from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"


    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['first_name'].label = ''

        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['last_name'].label = ''

        self.fields['guest_number'].widget.attrs['placeholder'] = 'Guest Number'
        self.fields['guest_number'].label = ''

        self.fields['comment'].widget.attrs['placeholder'] = 'Write some comment'
        self.fields['comment'].label = ''
        self.fields['comment'].widget.attrs['style'] = 'font-size: 20px;'
