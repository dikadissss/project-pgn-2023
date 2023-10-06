from django.shortcuts import render


# Create your views here.
def focal(request):
    context = {
        'title': 'Focal Mechanism'
    }
    return render(request, 'focal/focal.html', context)
