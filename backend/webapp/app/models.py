from django.db import models

# Create your models here.
class Candidat(models.Model):
    name = models.TextField()
    lastname = models.TextField()
    email = models.EmailField()
    #phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    #phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
    phonenum = models.CharField(max_length= 17)
    dateofbirth = models.DateField()
    cv = models.FileField(upload_to= 'media')