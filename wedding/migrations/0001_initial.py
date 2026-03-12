from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="RSVPSubmission",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("full_name", models.CharField(max_length=150, verbose_name="Nome e cognome")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("phone", models.CharField(blank=True, max_length=30, verbose_name="Telefono")),
                ("attending", models.CharField(choices=[("yes", "Sì, sarò presente"), ("no", "No, non potrò esserci")], max_length=3, verbose_name="Parteciperai?")),
                ("guest_count", models.PositiveSmallIntegerField(default=0, verbose_name="Numero accompagnatori")),
                ("children_present", models.BooleanField(default=False, verbose_name="Presenza bambini")),
                ("menu_choice", models.CharField(choices=[("classic", "Menu classico"), ("vegetarian", "Menu vegetariano"), ("vegan", "Menu vegano"), ("fish", "Menu pesce")], max_length=20, verbose_name="Scelta menu")),
                ("allergies", models.TextField(blank=True, verbose_name="Allergie o intolleranze")),
                ("special_needs", models.TextField(blank=True, verbose_name="Necessità particolari")),
                ("message", models.TextField(blank=True, verbose_name="Messaggio per gli sposi")),
                ("privacy_accepted", models.BooleanField(default=False, verbose_name="Privacy accettata")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Creato il")),
            ],
            options={
                "verbose_name": "RSVP",
                "verbose_name_plural": "RSVP",
                "ordering": ["-created_at"],
            },
        ),
    ]
