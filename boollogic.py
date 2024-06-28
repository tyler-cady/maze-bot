from django import forms
from .models import UnitTestMeasurement, MeasurementType

class UnitTestMeasurementForm(forms.ModelForm):
    class Meta:
        model = UnitTestMeasurement
        fields = ['measurement_type', 'bool_value', 'text_value']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.measurement_type:
            if self.instance.measurement_type.unit_type == 'bool':
                self.fields['text_value'].widget = forms.HiddenInput()
            else:
                self.fields['bool_value'].widget = forms.HiddenInput()