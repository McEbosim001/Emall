from django.shortcuts import render, redirect
from .forms import WaitlistForm

def landing_page(request):
    submitted = False

    if request.method == 'POST':
        form = WaitlistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/?submitted=True')
    else:
        form = WaitlistForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'landingapp/index.html', {'form': form, 'submitted': submitted})
