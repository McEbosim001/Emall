from django.shortcuts import render, redirect
from .forms import WaitlistForm

def landing_page(request):
    if request.method == 'POST':
        form = WaitlistForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'landingapp/index.html', {'form': form})  # or a success page
    else:
        form = WaitlistForm()
    return render(request, 'landingapp/index.html', {'form': form})
