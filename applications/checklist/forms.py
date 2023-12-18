from django import forms
from applications.checklist.models import Toast


class AllForm(forms.ModelForm):
    class Meta:
        model = Toast
        fields = "__all__"
        # fields = [
        #     "user", "group", "shift", "siren_one", "siren_two", "siren_three", "siren_four",
        #     "seiscomp_one", "seiscomp_two", "seiscomp_three", "toast_one", "toast_two",
        #     "disseminate_one", "disseminate_two", "tsp_one", "tsp_two",
        #     "wrs", "temperature1", "temperature2"
        # ]


class UserForm(forms.ModelForm):
    class Meta:
        model = Toast
        fields = ['user', 'group', 'shift', 'datetime']
        widgets = {
            'user': forms.Select(
                attrs={
                    'class': 'form-select'
                }),
            'group': forms.Select(
                attrs={
                    'class': 'form-select'
                }),
            'shift': forms.Select(
                attrs={
                    'class': 'form-select'
                }),
            'datetime': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        # print(self.fields['shift'].empty_string)
        # self.fields['shift'].empty_value = "(Silahkan Pilihft)"
        # print(self.fields['shift'].empty_value)
        self.fields['user'].empty_label = "Silahkan Pilih Nama Operator"
        self.fields['group'].empty_label = "Silahkan Pilih Nama Kelompok"


class SirenForm(forms.ModelForm):
    class Meta:
        model = Toast
        fields = ["siren_one", "siren_two", "siren_three", "siren_four"]
        widgets = {
            "siren_one": forms.RadioSelect(),
            "siren_two": forms.RadioSelect(),
            "siren_three": forms.RadioSelect(),
            "siren_four": forms.RadioSelect()
        }
        help_texts = {
            "siren_one": "Komputer sirine dalam keadaan siap (tidak hang)",
            "siren_two": "Aplikasi sirine dalam keadaan siap (tidak hang)",
            "siren_three": "Checklist salah satu sirine, contoh pemda Padang apakah sirine berubah dari merah menjadi "
                           "kuning? Lakukan untuk pemda dan bmkg  regional lainnya.",
            "siren_four": "Aplikasi Log Note sirine bisa diakses (http://192.168.1.1/bmkg/login/login.php) "
                          "Username: admin, Password: admin"
        }


class SeiscompForm(forms.ModelForm):
    class Meta:
        model = Toast
        fields = ["seiscomp_one", "seiscomp_two", "seiscomp_three"]
        widgets = {
            "seiscomp_one": forms.RadioSelect(),
            "seiscomp_two": forms.RadioSelect(),
            "seiscomp_three": forms.RadioSelect()
        }
        help_texts = {
            "seiscomp_one": "Komputer seiscomp dalam keadaan siap (tidak hang)",
            "seiscomp_two": "Feature seiscomp dapat digunakan (SCOLV, SCRTTV, DLL)",
            "seiscomp_three": "Apakah kondisi sinyal seiscomp masuk"
        }


class ToastForm(forms.ModelForm):
    class Meta:
        model = Toast
        fields = ["toast_one", "toast_two"]
        widgets = {
            "toast_one": forms.RadioSelect(),
            "toast_two": forms.RadioSelect(),
        }
        help_texts = {
            "toast_one": "Komputer TOAST dalam keadaan siap (tidak hang)",
            "toast_two": "Apakah aplikasi TOAST dapat digunakan",
        }


class DisseminateForm(forms.ModelForm):
    class Meta:
        model = Toast
        fields = ["disseminate_one", "disseminate_two"]
        widgets = {
            "disseminate_one": forms.RadioSelect(),
            "disseminate_two": forms.RadioSelect(),
        }
        help_texts = {
            "disseminate_one": "Komputer disseminasi dalam keadaan siap (tidak hang)",
            "disseminate_two": "Aplikasi disseminasi telah ditutup",
        }


class TSPForm(forms.ModelForm):
    class Meta:
        model = Toast
        fields = ["tsp_one", "tsp_two"]
        widgets = {
            "tsp_one": forms.RadioSelect(),
            "tsp_two": forms.RadioSelect(),
        }
        help_texts = {
            "tsp_one": "Komputer TSP dalam keadaan siap (tidak hang)",
            "tsp_two": "Aplikasi TSP telah ditutup",
        }


class WRSForm(forms.ModelForm):
    class Meta:
        model = Toast
        fields = ["wrs"]
        widgets = {
            "wrs": forms.RadioSelect(),
        }
        help_texts = {
            "wrs": "Display Aplikasi WRS NG dalam keadaan aktif",
        }


class TemperatureForm(forms.ModelForm):
    class Meta:
        model = Toast
        fields = ["temperature1", "temperature2"]
        widgets = {
            "temperature1": forms.TextInput(
                attrs={
                    'class': 'form-control text-center',
                    # 'style': "font-size: 12px"
                }
            ),
            "temperature2": forms.TextInput(
                attrs={
                    'class': 'form-control text-center',
                    # 'style': "font-size: 14px"
                }
            ),
        }
        help_texts = {
            "temperature1": "Display Aplikasi WRS NG dalam keadaan aktif",
        }
