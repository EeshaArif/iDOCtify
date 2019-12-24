from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator


#username: EeshaArif
#password: eesha
class Patient(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length = 150)
    address = models.CharField(max_length = 200, default = '')
    phone = models.CharField(max_length = 20)
    age = models.IntegerField(default = 0)
    gender = models.CharField(max_length = 6)
    email = models.EmailField(default = '')
    image = models.FileField(upload_to='images/', default = '')
    occupation = models.CharField(max_length = 100, null = True, blank = True)
    presenting_complaint = models.TextField(null = True, blank = True)

    #Symptoms/
    symptom1 = models.CharField(max_length = 50, null = True, blank = True)
    symptom2 = models.CharField(max_length = 50, null = True, blank = True)
    symptom3 = models.CharField(max_length = 50, null = True, blank = True)
    symptom4 = models.CharField(max_length = 50, null = True, blank = True)
    symptom5 = models.CharField(max_length = 50, null = True, blank = True)

    past_medical_history = models.TextField(null = True, blank = True)
    past_surgical_history =models.TextField(null = True, blank = True)
    past_drug_history = models.TextField(null = True, blank = True)
    drug_allergy = models.TextField(null = True, blank = True)
    vaccination_history = models.TextField(null = True, blank = True)
    personal_history = models.TextField(null = True, blank = True)
    economic_status = models.TextField(null = True, blank = True)

    def __str__(self):
        return '%s %s' %(self.first_name, self.last_name)
