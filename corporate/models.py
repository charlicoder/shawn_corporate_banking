from django.db import models



class Corporate(models.Model):
    "Is Company and Corporate are synonyms?"
    corporate_name = models.CharField(help_text= "Corporate Name", max_length=50, null=False, blank=False)
    registration_number = models.CharField(max_length=50, null=True, blank=True)
    entity_type = models.CharField(max_length=50, null=True, blank=True)
    company_email = models.EmailField(max_length=50, null=True, blank=True)
    company_phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    postal_code = models.CharField(max_length=50, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)

    status = models.CharField(max_length=25, null=True, blank=True)
    "How status is defined? What values it can take?"


    def __str__(self):
        return self.name



    class Bank(models.Model):
        bank_name = models.CharField(help_text= "Corporate Name", max_length=50, null=False, blank=False)    

        ENTRY_TYPE = (
            ('personal', 'Personal'),
            ('corporate', 'Corporate'),
            ('trusty', 'Trusty'),
        )

        entry_type = models.CharField(max_length=10, choices=ENTRY_TYPE, null=True, blank=True) 
        
        # Bank address goes here
        address = models.CharField(max_length=200, null=True, blank=True)
        city = models.CharField(max_length=50, null=True, blank=True)
        
        bank_swift_code = models.CharField(max_length=50, null=True, blank=True)
        routing_or_sort_code = models.CharField(max_length=50, null=True, blank=True)

        CURRENCY = (
            ('doller', 'Doller'),
            ('taka', 'TAKA'),
        )

        currency = models.CharField(max_length=10, choices=CURRENCY, null=True, blank=True)
        account_number = models.CharField(max_length=50, null=True, blank=True)
        benificiary_name = models.CharField(help_text= "Ultmete beneficiary details name.", max_length=50, null=True, blank=True)
        how_do_you_make_money = models.TextField(max_length=500, null=True, blank=True)



        def __str__(self):
            return self.bank_name