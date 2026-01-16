from django import forms
from .models import CourtBooking
from django.utils import timezone

class CourtBookingForm(forms.ModelForm):
    class Meta:
        model = CourtBooking
        fields = ['court_number', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < timezone.now().date():
            raise forms.ValidationError("Booking date cannot be in the past.")
        return date
