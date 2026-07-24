from django import forms

class HotelSearchForm(forms.Form):
    city = forms.CharField()
    room_type = forms.ChoiceField(
        choices=[
            ("standard", "Standard"),
            ("double", "Double"),
            ("deluxe", "Deluxe"),
        ]
    )
    date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"})
    )