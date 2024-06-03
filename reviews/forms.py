from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from .models import Review


"""class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
        "required": "Your name must not be empty",
        "max_length": "Please enter a shorter name"
    })
    review_text = forms.CharField(
        label="Your feedback", widget=forms.Textarea, max_length=300)
    rating = forms.FloatField(
        label='Rating',
        validators=[
            MinValueValidator(1.0),
            MaxValueValidator(5.0)
        ],
        widget=forms.NumberInput(attrs={'step': '0.1'})
    )"""

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        # exlcude = ["owner_comment"]
