from django.shortcuts import render, redirect
from applications.account.models import CustomUser
from applications.checklist.models import Group
from applications.checklist.forms import SirenForm, AllForm,  \
    SeiscompForm, ToastForm, UserForm, DisseminateForm, TSPForm, WRSForm, TemperatureForm
from applications.checklist.models import Toast


# Create your views here.
def toast(request):
    if request.method == "POST":
        form = AllForm(request.POST)
        # print(form)
        if form.is_valid():
            print("tes")
            form.save()
        else:
            print(form.errors)

            # return redirect()
    else:
        tos = Toast.objects.filter(user__last_name="Saputra")
        print(tos[0].user.full_name())
        # print(all)
    context = {
        'sub': 'Checklist',
        'title': 'Toast',
        'sirens': SirenForm,
        'seiscomps': SeiscompForm,
        'toasts': ToastForm,
        'disseminates': DisseminateForm,
        'tsps': TSPForm,
        'wrss': WRSForm,
        'temperatures': TemperatureForm,
        'users': UserForm()
        # 'users': users,
        # 'groups': groups
    }

    return render(request, 'checklist/toast.html', context)