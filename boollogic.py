from django import forms
from .models import UnitTestMeasurement

class UnitTestMeasurementForm(forms.ModelForm):
    class Meta:
        model = UnitTestMeasurement
        fields = ['unit_test_step', 'measurement_type', 'test_description', 
                  'is_populated', 'char_field1', 'char_field2', 'float_field1', 'float_field2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['unit_test_step'].required = True
        self.fields['measurement_type'].required = True
        self.fields['test_description'].required = True

        if self.instance and self.instance.measurement_type:
            if self.instance.measurement_type.unit_type == 'bool':
                self.fields['char_field1'].widget = forms.HiddenInput()
                self.fields['char_field2'].widget = forms.HiddenInput()
                self.fields['float_field1'].widget = forms.HiddenInput()
                self.fields['float_field2'].widget = forms.HiddenInput()
            else:
                self.fields['is_populated'].widget = forms.HiddenInput()