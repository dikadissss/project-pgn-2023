from django.shortcuts import render


# Create your views here.
def toast(request):
    context = {
        'sub': 'Checklist',
        'title': 'Toast',
    }
    return render(request, 'checklist/toast.html', context)