from django.contrib import admin

from .models import RSVPSubmission


@admin.register(RSVPSubmission)
class RSVPSubmissionAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "email",
        "attending",
        "guest_count",
        "children_present",
        "menu_choice",
        "created_at",
    )
    list_filter = ("attending", "children_present", "menu_choice", "created_at")
    search_fields = ("full_name", "email", "phone")
    readonly_fields = ("created_at",)
