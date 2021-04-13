from django import forms
from .models import Customer, PlateCustomer, Plate, PrintLami
from django.forms import inlineformset_factory


class PrintLamiCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Customer
        widgets = {
            'shipping_day': forms.DateInput(attrs={"type": "date"}),
            'shipping_time': forms.TimeInput(format="%H:%M"),
        }
        fields = ('customer_name', 'sales_staff', 'order_number', 'shipping_day', 'shipping_time',
                  'shipping_style', 'data', 'data_location', 'data_details', 'packing_type', 'output_style')


PrintLamiCreateFormSet = inlineformset_factory(
    Customer, PrintLami, fields='__all__', extra=1, max_num=20
)


class PlateCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = PlateCustomer
        widgets = {
            'shipping_day': forms.DateInput(attrs={"type": "date"}),
            'shipping_time': forms.TimeInput(format="%H:%M"),
        }
        fields = ('customer_name', 'sales_staff', 'order_number', 'shipping_day', 'shipping_time',
                  'shipping_style', 'packing_type', 'data', 'data_location', 'data_details', 'output_style')


PlateCreateFormSet = inlineformset_factory(
    PlateCustomer, Plate, fields='__all__', extra=1, max_num=20
)