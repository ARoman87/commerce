from cProfile import label
from django.forms import ModelForm
from .models import Listing, User
from django import forms

CATEGORIES = [
    ("-", "-"),
    ("auto", "Auto"),
    ("books", "Books"),
    ("clothing", "Clothing"),
    ("collectibles", "Collectibles & Art"),
    ("electronics", "Electronics"),
    ("home", "Home & Garden"),
    ("movies", "Movies & Music"),
    ("sporting", "Sporting Goods"),
    ("toys", "Toys & Hobbies"),
]
 
class CreateForm(ModelForm):
    class Meta:
        model = Listing
        fields = ("title", "image", "description", "category", "bid")
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Title", "class": "create-title",}),
            "image": forms.TextInput(attrs={"placeholder": "Image URL", "class": "create-image"}),
            "description": forms.Textarea(attrs={"placeholder": "Description", "class": "create-description"}),
            "category": forms.Select(attrs={"placeholder": "Description", "class": "create-description"}, choices=CATEGORIES),
            "bid": forms.TextInput(attrs={"placeholder": "Starting Bid", "class": "create-bid",})
        }
        labels = {
            "title": "",
            "image": "",
            "description": "",
            "category": "",
            "bid": "",
        }
