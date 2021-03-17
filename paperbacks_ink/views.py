from django.shortcuts import render

def index(request):
    """The home page for Paperbacks Ink."""
    return render(request, 'paperbacks_ink/index.html')

def about(request):
    """Shows About page."""
    return render(request, 'paperbacks_ink/about.html')

def kaffee(request):
    """Shows Kaffee Kultur page."""
    return render(request, 'paperbacks_ink/kaffee.html')

def contact(request):
    """Shows Contact Us page."""
    return render(request, 'paperbacks_ink/contact.html')