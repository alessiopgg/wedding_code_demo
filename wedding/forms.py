from django import forms

from .models import RSVPSubmission


class RSVPForm(forms.ModelForm):
    class Meta:
        model = RSVPSubmission
        fields = [
            "full_name",
            "email",
            "phone",
            "attending",
            "guest_count",
            "children_present",
            "menu_choice",
            "allergies",
            "special_needs",
            "message",
            "privacy_accepted",
        ]
        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nome e cognome"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "nome@email.it"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Telefono (facoltativo)"}),
            "attending": forms.RadioSelect(),
            "guest_count": forms.NumberInput(attrs={"class": "form-control", "min": "0", "max": "10"}),
            "children_present": forms.CheckboxInput(attrs={"class": "checkbox-input"}),
            "menu_choice": forms.Select(attrs={"class": "form-control"}),
            "allergies": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Indica eventuali allergie o intolleranze"}),
            "special_needs": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Accessibilità, transfer, necessità particolari..."}),
            "message": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Scrivi un messaggio per gli sposi"}),
            "privacy_accepted": forms.CheckboxInput(attrs={"class": "checkbox-input"}),
        }
        labels = {
            "guest_count": "Numero accompagnatori",
            "children_present": "Ci saranno bambini?",
        }
        help_texts = {
            "guest_count": "Indica solo eventuali accompagnatori aggiuntivi, esclusa la tua presenza.",
        }

    def clean_guest_count(self):
        guest_count = self.cleaned_data.get("guest_count", 0)
        if guest_count < 0:
            raise forms.ValidationError("Il numero di accompagnatori non può essere negativo.")
        if guest_count > 10:
            raise forms.ValidationError("Per gruppi superiori a 10 persone contattaci direttamente.")
        return guest_count

    def clean_privacy_accepted(self):
        value = self.cleaned_data.get("privacy_accepted")
        if not value:
            raise forms.ValidationError("Per inviare la conferma è necessario accettare la privacy.")
        return value

    def clean(self):
        cleaned_data = super().clean()
        attending = cleaned_data.get("attending")

        if attending == "no":
            cleaned_data["guest_count"] = 0
            cleaned_data["menu_choice"] = "classic"

        return cleaned_data
