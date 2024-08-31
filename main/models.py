from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone




class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
        ('Rather Not Say', 'Rather Not Say'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dp = models.ImageField(upload_to="user_dp/", default="user_dp/user.jpg")
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, blank=True, null=True)
    institute = models.CharField(max_length=100, blank=True, null=True)
    whatsapp_no = models.CharField(max_length=15, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='Rather Not Say')
    fathers_name = models.CharField(max_length=100, blank=True, null=True)
    mothers_name = models.CharField(max_length=100, blank=True, null=True)
    course = models.CharField(max_length=100, blank=True, null=True)
    semester = models.CharField(max_length=10, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.user.username

class Institute(models.Model):
    name = models.CharField(max_length=255, unique=True)
    zip_code = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Amenity(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='amenity_icons/', blank=True, null=True)
    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='food_icons/', blank=True, null=True)
    def __str__(self):
        return self.name



class Property(models.Model):
    PROPERTY_TYPES = (
        ('hostel', 'Hostel'),
        ('pg', 'PG'),
        ('flat', 'Flat'),
    )
    name = models.CharField(max_length=255)
    locality = models.CharField(max_length=255, default="Gr. Noida")
    description = models.CharField(max_length=255, default="We're dedicated to give you best customer service")
    new_price = models.DecimalField(max_digits=10, decimal_places=0, default=100000)
    old_price = models.DecimalField(max_digits=10, decimal_places=0, default=120000)
    property_type = models.CharField(max_length=10, choices=PROPERTY_TYPES)
    images = models.ImageField(upload_to='property_images/', blank=True, null=True)
    nearby_institutes = models.ManyToManyField(Institute, through='PropertyInstitute')
    amenities = models.ManyToManyField(Amenity, blank=True, related_name='properties')
    bus_availability = models.BooleanField(default=False)
    food_type = models.ManyToManyField(Food, blank=True, related_name='properties')
    laundry_service = models.TextField(blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Both', 'Both')], default="Both")
    housekeeping = models.BooleanField(default=False)
    staff = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Both', 'Both')], default="Both")
    hostel_timing = models.TimeField(blank=True, null=True)
    other_facilities = models.TextField(blank=True)
    nearby_market = models.TextField(blank=True)
    nearby_metro_station = models.CharField(max_length=255, blank=True)
    food_menu = models.ImageField(upload_to='food_menu/', blank=True, null=True)
    contact_name = models.CharField(max_length=255, default="NixStays Team")
    contact_number = models.CharField(max_length=15, default="8449922025")
    owner_name = models.CharField(max_length=255, default="NixStays Team")
    owner_number = models.CharField(max_length=15, default="8449922025")
    address = models.TextField()
    zip_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('property_detail', args=[str(self.id)])

class PropertyInstitute(models.Model):
    property = models.ForeignKey(Property, related_name='property_inst', on_delete=models.CASCADE)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    distance = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return f"{self.property.name} - {self.institute.name} - {self.distance}km"

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='property_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')
    def __str__(self):
        return self.property.name

class RoomType(models.Model):
    property = models.ForeignKey(Property, related_name='room_types', on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    ac_price = models.DecimalField(max_digits=10, decimal_places=2)
    non_ac_price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.property.name} - {self.type} - AC: {self.ac_price}, Non-AC: {self.non_ac_price}"

class Consultation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    date_time = models.DateTimeField()
    institute = models.CharField(max_length=100)
    custom_msg = models.TextField()
    def __str__(self):
        return self.name

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    date_reserved = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} - {self.property.name}"

class Testimonials(models.Model):
    image = models.ImageField(upload_to='testimonials/', default="testimonials/user.jpg")
    name = models.CharField(max_length=255)
    sub_head = models.CharField(max_length=255)
    msg = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.name} - {self.sub_head}"

