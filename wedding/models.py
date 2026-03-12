from django.db import models


class RSVPSubmission(models.Model):
    ATTENDING_CHOICES = (
        ("yes", "Sì, sarò presente"),
        ("no", "No, non potrò esserci"),
    )

    MENU_CHOICES = (
        ("classic", "Menu classico"),
        ("vegetarian", "Menu vegetariano"),
        ("vegan", "Menu vegano"),
        ("fish", "Menu pesce"),
    )

    full_name = models.CharField("Nome e cognome", max_length=150)
    email = models.EmailField("Email")
    phone = models.CharField("Telefono", max_length=30, blank=True)
    attending = models.CharField("Parteciperai?", max_length=3, choices=ATTENDING_CHOICES)
    guest_count = models.PositiveSmallIntegerField("Numero accompagnatori", default=0)
    children_present = models.BooleanField("Presenza bambini", default=False)
    menu_choice = models.CharField("Scelta menu", max_length=20, choices=MENU_CHOICES)
    allergies = models.TextField("Allergie o intolleranze", blank=True)
    special_needs = models.TextField("Necessità particolari", blank=True)
    message = models.TextField("Messaggio per gli sposi", blank=True)
    privacy_accepted = models.BooleanField("Privacy accettata", default=False)
    created_at = models.DateTimeField("Creato il", auto_now_add=True)

    class Meta:
        verbose_name = "RSVP"
        verbose_name_plural = "RSVP"
        ordering = ["-created_at"]

    def __str__(self):
        status = "Presente" if self.attending == "yes" else "Assente"
        return f"{self.full_name} - {status}"
