from django.db import models
from django.forms import BooleanField

# Create your models here.
class Barber(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    bio = models.TextField()
    image = models.ImageField(default='default_g5kghd.jpg', upload_to='barber_image', null=True, blank=True)
    address = models.CharField(max_length=300, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    stall = models.BooleanField(null=True, blank=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    stall = models.BooleanField(null=True, blank=True)

    @property
    def age(self):
        import datetime
        try:
            dob = self.date_of_birth
            tod = datetime.date.today()
            my_age = (tod.year-dob.year) - int((tod.month, tod.day) < (dob.month, dob.day))
        except:
            my_age = 'Blank'
        return my_age

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
        
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Skill(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
   
    
    def __str__(self):
        return self.name

LOAN_STATUS = (
        
        ('0', 'Working'),
        ('1', 'Available'),
        ('2', 'Unavailable'),
    )


class Service(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT, null=True, blank=True)
    barber = models.ForeignKey(Barber, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.IntegerField(default=0, null=True)
    status = models.CharField(max_length=3, choices=LOAN_STATUS, blank=True, default='', help_text='Barbers availability',
    )
    
    def __str__(self):
        return f'{self.skill}'

class About(models.Model):
    text = models.TextField(null=True, blank=True)



