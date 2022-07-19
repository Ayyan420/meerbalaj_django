from django import forms
from .models import Profile
from .models import Education
from .models import Experience
from .models import Skill
from .models import Bar_Image
from .models import Testimonial
from .models import Categorie
from .models import Portfolio_Image
from .models import Line_Bar_Image
from .models import Contact_U


class upload_meta_image(forms.ModelForm):
    class Meta:
        model = Line_Bar_Image
        fields = ['name_img','bar_img']




class upload_category(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['name_category']



class upload_portfolio_image(forms.ModelForm):
    class Meta:
        model = Portfolio_Image
        fields = ['name_project','item_img','category']




class upload_testimonials(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['client_img','client_name','client_job_title','client_feedback']



class edit_testimonials(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['client_img','client_name','client_job_title','client_feedback']




class Edit_completed_projects(forms.ModelForm):
    class Meta:
        model = Bar_Image
        fields = ['completed_before_name','completed_before_count','color','mark']




class Add_completed_projects_form_now(forms.ModelForm):
    class Meta:
        model = Bar_Image
        fields = ['completed_before_name','completed_before_count','color','mark']



class upload_completed_project(forms.ModelForm):
    class Meta:
        model = Bar_Image
        fields = ['completed_before_name','completed_before_count','color','mark']



class edit_profile_user(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_img','name','multi_headline_1','multi_headline_2','multi_headline_3','phone','email','facebook','website','linkedin','bio','spoken','nationality','location','interests','DOB','upload_cv','check_remove_cv']





class upload_profile_user(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['profile_img','name','multi_headline_1','multi_headline_2','multi_headline_3','phone','email','facebook','website','linkedin','bio','spoken','nationality','location','interests','DOB','upload_cv','check_remove_cv']




class upload_education(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['From','To','learning_place','degree']



class upload_experience(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['From','To','company','job_title']


class edit_education_user_data(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['From','To','learning_place','degree']



class edit_experience_user_data(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['From','To','company','job_title']





class upload_skills(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill_name','skill_count']



class edit_skills_user_data(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill_name','skill_count']