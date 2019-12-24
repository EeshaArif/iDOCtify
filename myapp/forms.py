from django import forms
from .models import Patient
#username: EeshaArif
#password: eesha
CHOICES=[('male','Male'),
         ('female','Female'),
         ('other', 'Other')
         ]

class PatientHistory(forms.ModelForm):
    gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'address', 'phone', 'age', 'gender',
        'email', 'image', 'occupation', 'presenting_complaint','symptom1','symptom2',
        'symptom3','symptom4','symptom5','past_medical_history','past_surgical_history',
        'past_drug_history', 'drug_allergy', 'vaccination_history','personal_history',
        'economic_status']
