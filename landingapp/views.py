from django.shortcuts import render
from .forms import WaitlistForm

def landing_page(request):
    success = False
    if request.method == "POST":
        form = WaitlistForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = WaitlistForm()
    else:
        form = WaitlistForm()
    return render(request, "landingapp/index.html", {"form": form, "success": success})