from django import forms
from blog.models import Contact
from django.utils.translation import gettext_lazy as _


class CommentForm(forms.Form):
    def is_valid(self):
        result = super().is_valid()
        # loop on *all* fields if key '__all__' found else only on errors:
        for x in self.fields if "__all__" in self.errors else self.errors:
            attrs = self.fields[x].widget.attrs
            attrs.update({"class": attrs.get("class", "") + " is-invalid"})
        return result

    author = forms.CharField(
        label="Your Name",
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your Name"}
        ),
    )
    body = forms.CharField(
        label="Comment",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Leave a comment!",
                "rows": "3",
            }
        ),
    )

class ContactForm(forms.ModelForm):
    def is_valid(self):
        result = super().is_valid()
        # loop on *all* fields if key '__all__' found else only on errors:
        for x in self.fields if "__all__" in self.errors else self.errors:
            attrs = self.fields[x].widget.attrs
            attrs.update({"class": attrs.get("class", "") + " is-invalid"})
        return result

    class Meta:
        model = Contact
        fields = ["name", "email", "phone", "address", "message","userfile"]
        labels = {
            "name": _("Your Name"),
            "email": _("Your Email Address"),
            "phone": _("Your Phone Number"),
            "address": _("Your Address"),
            "message": _("Your Message"),
            "userfile": _("Select Your File"),
        }
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Your Name"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Enter Your Email Address"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Your Phone Number"}
            ),
            "address": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Your Address"}
            ),
            "message": forms.Textarea( 
                attrs={ "class": "form-control", "placeholder": "Enter Your Message", "rows": "5"}
            ),
            "userfile": forms.FileInput( 
                attrs={ "class": "form-control", "placeholder": "Please Select file"}
            ),
        }
    
