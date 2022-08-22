from cProfile import label
from importlib.metadata import requires
from django.forms import ModelForm
from .models import Listing, User, Comments, WishList
from django import forms

CATEGORIES = [
    ("none", ""),
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

CONDITION = [
    ("new", "New"),
    ("used", "Used")
]
 
class CreateForm(ModelForm):
    class Meta:
        model = Listing
        fields = ("title", "image", "description", "category", "bid", "condition", "location")
        widgets = {
            "title": forms.TextInput(attrs={"class": "create-title",}),
            "image": forms.TextInput(attrs={"placeholder": "URL", "class": "create-image"}),
            "description": forms.Textarea(attrs={"class": "create-description"}),
            "category": forms.Select(attrs={"class": "create-category"}, choices=CATEGORIES),
            "bid": forms.TextInput(attrs={"placeholder": "$ 0", "class": "create-bid",}),
            "condition": forms.Select(attrs={"class": "create-condition"}, choices=CONDITION),
            "location": forms.TextInput(attrs={"placeholder": "City, State", "class": "create-location"})
        }
        labels = {
            "title": "",
            "image": "",
            "description": "",
            "category": "",
            "bid": "",
            "location": "",
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ("comment",)
        widgets = {
            "comment": forms.Textarea(attrs={
                "placeholder": "Leave a comment. . .",
                "required": "False",
                "class": "comment-box"   
            })
        }
        labels = {
            "comment": ""
        }
    


class WishListForm(ModelForm):
    class Meta:
        model = WishList
        fields = ("user",)