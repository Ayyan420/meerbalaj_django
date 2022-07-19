from django.db import models
import datetime
from django.utils import timezone



class Profile(models.Model):

    check_remove_cv= models.BooleanField(blank=True, default=False)


    profile_img = models.ImageField(blank=False, null = True, upload_to = "images/%Y/%m/%d")
    name = models.CharField(max_length=50 , null=True, blank=False)
    multi_headline_1 = models.CharField(max_length=50 , null=True, blank=False)
    multi_headline_2 = models.CharField(max_length=50 , null=True, blank=True)
    multi_headline_3 = models.CharField(max_length=50 , null=True, blank=True)
    phone = models.CharField(max_length=50, blank = False, null = True)
    email = models.CharField(max_length=50, blank = False, null = True)
    facebook = models.CharField(max_length=50, blank = True, null = True)
    website = models.CharField(max_length=50, blank = True, null = True , default="https://www.eusol.net/")
    linkedin = models.CharField(max_length=50, blank = True, null = True)


    bio = models.TextField(max_length=1000, blank = False, null = True)
    spoken = models.CharField(max_length=50, blank = False, null = True)
    nationality = models.CharField(max_length=50, blank = False, null = True)
    location = models.CharField(max_length=50, blank = False, null = True)
    interests = models.CharField(max_length=50, blank = False, null = True)
    DOB = models.DateField( default= 0, auto_now_add= False, auto_now = False , blank=False)
    upload_cv = models.FileField(blank=True, null = True, upload_to = "files/%Y/%m/%d")
    
    def __str__(self):
        return self.name


class Education(models.Model):

    From = models.DateField( default= 0, auto_now_add= False, auto_now = False , blank=False)
    To = models.DateField( default= 0, auto_now_add= False, auto_now = False , blank=False)
    learning_place = models.CharField(max_length=50 , null=True, blank=False, default="School")
    degree = models.CharField(max_length=50 , null=True, blank=False , default="Matriculation")

    def __str__(self):
        return self.degree



class Experience(models.Model):

    From = models.DateField( default= 0, auto_now_add= False, auto_now = False , blank=False)
    To = models.DateField( default= 0, auto_now_add= False, auto_now = False , blank=False)
    company = models.CharField(max_length=50 , null=True, blank=False , default="Google")
    job_title = models.CharField(max_length=50 , null=True, blank=False , default="Odoo Developer")

    def __str__(self):
        return self.job_title




class Skill(models.Model):

    skill_name = models.CharField(max_length=50 , null=True, blank=False)
    skill_count = models.IntegerField( default=50, null=True, blank=False)

    def __str__(self):
        return self.skill_name



class Bar_Image(models.Model):

    completed_before_name = models.CharField(max_length=50 , null=True, blank=False, default="Completed Projects")
    completed_before_count = models.IntegerField( default=1, null=True, blank=False)
    color = models.CharField(max_length=50  , default='#f3c74d', null=True, blank=False)
    mark = models.CharField( max_length=50 , default='cell', null=True, blank=False)
    def __str__(self):
        return self.completed_before_name



class Testimonial(models.Model):

    client_img = models.ImageField(blank=False, null = True, upload_to = "images/%Y/%m/%d")
    client_name = models.CharField(max_length=50 , null=True, blank=False)
    client_job_title = models.CharField(max_length=50 , null=True, blank=False)
    client_feedback = models.TextField(max_length=1000 , null=True, blank=False)

    def __str__(self):
        return self.client_name



class Categorie(models.Model):

    name_category = models.CharField(max_length=50 , null=True, blank=False)

    def __str__(self):
        return self.name_category


class Portfolio_Image(models.Model):

    name_project = models.CharField(max_length=50 , null=True, blank=False)
    item_img = models.ImageField(blank=False, null = True, upload_to = "images/%Y/%m/%d")
    category = models.ForeignKey(Categorie, on_delete=models.PROTECT , blank=False)

    def __str__(self):
        return self.name_project



class Line_Bar_Image(models.Model):

    name_img = models.CharField(max_length=50 , null=True, blank=False)
    bar_img = models.ImageField(blank=False, null = True, upload_to = "images/%Y/%m/%d")

    def __str__(self):
        return self.name_img




class Contact_U(models.Model):

    contact_from_name = models.CharField(max_length=50 , null=True, blank=False)
    contact_from_email = models.CharField(max_length=50 , null=True, blank=False)
    contact_message = models.CharField(max_length=50 , null=True, blank=False)
    contact_us_date_time = models.DateTimeField(auto_now_add= False, auto_now = False , blank=False, default=datetime.datetime.now)

    def __str__(self):
        return self.contact_from_name
