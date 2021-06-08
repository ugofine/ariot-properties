from django.db import models

# Create your models here.

class Property(models.Model):

    PURPOSE = (
       ('Sale', 'Sale'),
        ('Rent', 'Rent'), 
        ('Lease','Lease'),
    )

    ROOMS = (
        ('1', '1'),
       ('2', '2'),
        ('3', '3'), 
        ('4', '4'),
    
    )

    LOCATION = (
        ('lagos', 'lagos'),
       ('Abuja', 'Abuja'),
        ('Enugu', 'Enugu'), 
        ('Portharcourt', 'Portharcourt'),
    
    )



    name = models.CharField(max_length=100)
    description = models.TextField()
    purpose = models.CharField(choices=PURPOSE, max_length=50)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', blank ="True"  )
    price = models.DecimalField(max_digits=8, decimal_places=2)
    room = models.CharField(choices=ROOMS,max_length=20 )
    location = models.CharField(choices=LOCATION,max_length=20, blank=True)


    def __str__(self):
        return self.name
      
