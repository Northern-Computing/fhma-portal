from django.db import models

# Area Serviced Models 
class AreaServiced(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Area or City Name",
        help_text="Please provide the area or city name"
    )
    zipcode = models.CharField(
        max_length=200,
        verbose_name="Area or City Zipcode",
        help_text="Please provide the area or city zipcode"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
# Ethnicity choices
class Ethnicity(models.TextChoices):
    ASIAN = 'AS', 'Asian'
    BLACK = 'BL', 'Black'
    HISPANIC = 'HI', 'Hispanic'
    WHITE = 'WH', 'White'
    OTHER = 'OT', 'Other'

# Gender choices
class Gender(models.TextChoices):
    MALE = 'MA', 'Male'
    FEMALE = 'FE', 'Female'

# Client model
class Client(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Client Name",
        help_text="Please provide the clients name"
    )
    area_serviced = models.ForeignKey(
        AreaServiced, 
        on_delete=models.CASCADE, 
        null=True,
        verbose_name="Area or City",
        help_text="Please select from the options provided"
    )
    age = models.IntegerField(
        verbose_name="Client Age",
        help_text="Please provide the clients age",
        null=True,
        blank=True
    )
    gender = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        choices=Gender.choices,
        verbose_name="What is the clients gender?",
        help_text="Please select from the options provided"
    )
    email = models.EmailField(
        max_length=200, 
        null=True, 
        blank=True,
        verbose_name="Client Email (Optional)",
        help_text="Please provide the clients email"
    )
    phone = models.CharField(
        max_length=20, 
        null=True, 
        blank=True,
        verbose_name="Client Phone (Optional)",
        help_text="Please provide the clients phone number"
    )
    address = models.CharField(
        max_length=200, 
        null=True, 
        blank=True,
        verbose_name="Client Address (Optional)",
        help_text="Please provide the clients address"
    )
    city = models.CharField(
        max_length=200, 
        null=True, 
        blank=True,
        verbose_name="Client City (Optional)",
        help_text="Please provide the clients city"
    )
    state = models.CharField(
        max_length=200, 
        null=True, 
        blank=True,
        verbose_name="Client State (Optional)",
        help_text="Please provide the clients state"
    )
    country = models.CharField(
        max_length=200, 
        null=True, 
        blank=True,
        verbose_name="Client Country (Optional)",
        help_text="Please provide the clients country"
    )
    zipcode = models.CharField(
        max_length=200, 
        null=True, 
        blank=True,
        verbose_name="Client Zipcode (Optional)",
        help_text="Please provide the clients zipcode"
    )
    ethnicity = models.CharField(
        max_length=2,
        choices=Ethnicity.choices,
        default=Ethnicity.OTHER,
        verbose_name="What is the clients ethnicity?",
        help_text="Please select from the options provided"
    )
    below_poverty_line = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="Does the client live below the poverty line (below $2500 per month)?",
        help_text="Please select Yes or No"
    )
    homeless = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="Is the client homeless?",
        help_text="Please select Yes or No"
    )
    veteran = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="Is the client a veteran?",
        help_text="Please select Yes or No"
    )
    disabled = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="Is the client disabled?",
        help_text="Please select Yes or No"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Is the client active?",
        help_text="Please select Yes or No"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

