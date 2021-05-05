from django.shortcuts import render, redirect, get_object_or_404


def index(request):
    """The home page for Paperbacks Ink."""
    error = get_object_or_404()
    return render(request, "paperbacks_ink/index.html")


def events(request):
    """Shows Events page."""
    return render(request, "paperbacks_ink/events.html")


def kaffee(request):
    """Shows Kaffee Kultur page."""
    return render(request, "paperbacks_ink/kaffee.html")


def contact(request):
    """Shows Contact Us page."""
    return render(request, "paperbacks_ink/contact.html")
