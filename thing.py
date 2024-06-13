from django.shortcuts import render
from .models import SerialNumber
from .forms import SerialSearchForm

def search_view(request):
    form = SerialSearchForm()
    results = None
    if request.method == 'GET':
        form = SerialSearchForm(request.GET)
        if form.is_valid():
            serial_number = form.cleaned_data['serial_number']
            results = SerialNumber.objects.filter(serial_number__icontains=serial_number)
    return render(request, 'search/search.html', {'form': form, 'results': results})