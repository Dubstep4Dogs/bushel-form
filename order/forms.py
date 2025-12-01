from django import forms
from .models import Order

PICKUP_TIMES = [
    ("14:00", "2:00 PM"),
    ("15:00", "3:00 PM"),
    ("16:00", "4:00 PM"),
    ("17:00", "5:00 PM"),
    ("18:00", "6:00 PM"),
    ("19:00", "7:00 PM"),
    ("20:00", "8:00 PM"),
]

class OrderForm(forms.ModelForm):
    pickup = forms.ChoiceField(choices=PICKUP_TIMES)

    class Meta:
        model = Order
        fields = '__all__'
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email",
            "phone": "Phone",
            "pickup": "Pickup Time",
            "comment": "Order",
        }
        error_messages = {
            "first_name": {
                "required": "Please enter your first name",
                "max_length": "First name is too long",
            },
            "last_name": {
                "required": "Please enter your last name",
                "max_length": "Last name is too long",
            },
            "email": {
                "required": "Please enter your email",
                "invalid": "Please enter a valid email",
            },
            "phone": {
                "required": "Please enter your phone number",
            },
            "pickup": {
                "required": "Please select a pickup date and time",
            },
            "comment": {
                "max_length": "Your comment is too long",
            },
        }
