from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    telegram = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state_province = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    
    IE = (
        ('director', 'Directory'),
        ('shareholder', 'Shareholder'),
        ('trusty', 'Trusty'),
        ('owner', 'owner'),
        ('other', 'other'),
    )

    are_you_ie = models.CharField(help_text='Are you at a IE ( Director )', max_length=20, choices=IE, null=True, blank=True)
    are_u_signatory = models.BooleanField(help_text='Do you have signatory power?', null=True, blank=True)
    
    parcetage_of_owenership = models.PositiveSmallIntegerField(null=True, blank=True)


    def __str__(self):
        return self.first_name

