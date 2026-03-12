from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse

from .content import SITE_CONTENT
from .forms import RSVPForm


def home(request):
    if request.method == "POST":
        form = RSVPForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Grazie, la tua conferma è stata inviata correttamente. Non vediamo l’ora di festeggiare con te.",
            )
            return redirect(f"{reverse('wedding:home')}#rsvp")
        messages.error(request, "Controlla i campi evidenziati e riprova.")
    else:
        form = RSVPForm()

    context = {
        "site": SITE_CONTENT,
        "form": form,
    }
    return render(request, "wedding/home.html", context)
