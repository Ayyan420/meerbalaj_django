# Flow of full Digi CV

# profile model 
    
#     inlcudes  name title 
#     inlcudes  multi line title 
#     inlcudes  phone email social links
#     includes despcriptions 
#     includes   name title,DOB,LANG,NAT,INTRST



# Education, Skill model

#     multi models
#         education
#         experience
#         skills bars



# Bar Images Model
#     complte projects
#     clients
#     awards



# Works & Reviews Model


# Items Filters Model


# Bar Images Model

# Contact Model 





from django.http import HttpResponse
import csv
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect 
from django.utils import timezone
from meerbalajcv.models import *
import datetime
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from meerbalajcv.forms import *
from django.http import FileResponse


@csrf_exempt
def home(request):

    profile_data = Profile.objects.all()
    title=""
    for x in profile_data:
        title = str(x.name)
    
    education_data = Education.objects.all()
    experience_data = Experience.objects.all()
    skill_data = Skill.objects.all()
    testimonial_data = Testimonial.objects.all()
    categorie_data = Categorie.objects.all()
    portfolio_Image_data = Portfolio_Image.objects.all()
    line_bar_imgs_data = Line_Bar_Image.objects.all()



    projects= ""
    projects_icon= ""
    projects_color= ""
    count_projects= 0
    clients= ""
    clients_icon= ""
    clients_color= ""
    count_clients=0
    awards= ""
    awards_icon= ""
    awards_color= ""
    award_count= 0

    bar_Image_data = Bar_Image.objects.all()

    if bar_Image_data:
        list_len = len(bar_Image_data)
        if list_len ==1:
            projects= str(bar_Image_data[0].completed_before_name) 
            count_projects= int(bar_Image_data[0].completed_before_count)
            projects_icon= str(bar_Image_data[0].mark)
            projects_color= str(bar_Image_data[0].color)

        if list_len ==2:
            projects= str(bar_Image_data[0].completed_before_name) 
            count_projects= int(bar_Image_data[0].completed_before_count)
            projects_icon= str(bar_Image_data[0].mark)
            projects_color= str(bar_Image_data[0].color)
            clients= str(bar_Image_data[1].completed_before_name)
            count_clients=int(bar_Image_data[1].completed_before_count)
            clients_icon=str(bar_Image_data[1].mark)
            clients_color=str(bar_Image_data[1].color)

        if list_len ==3:
            projects= str(bar_Image_data[0].completed_before_name) 
            count_projects= int(bar_Image_data[0].completed_before_count)
            projects_icon= str(bar_Image_data[0].mark)
            projects_color= str(bar_Image_data[0].color)
            clients= str(bar_Image_data[1].completed_before_name)
            count_clients=int(bar_Image_data[1].completed_before_count)
            clients_icon=str(bar_Image_data[1].mark)
            clients_color=str(bar_Image_data[1].color)
            awards= str(bar_Image_data[2].completed_before_name)
            award_count= int(bar_Image_data[2].completed_before_count)
            awards_icon= str(bar_Image_data[2].mark)
            awards_color= str(bar_Image_data[2].color)



    bar_Image_data_dict = {
    "projects": projects,
    "count_projects": count_projects,
    "clients": clients,
    "count_clients": count_clients,
    "awards": awards,
    "award_count": award_count,
    "projects_icon": projects_icon,
    "clients_icon": clients_icon,
    "awards_icon": awards_icon,
    "projects_color": projects_color,
    "clients_color": clients_color,
    "awards_color": awards_color,
    }



    context = {

    'title':title,
    'profile_data':profile_data,
    'education_data':education_data,
    'skill_data':skill_data,
    'experience_data':experience_data,
    'experience_data':experience_data,
    'testimonial_data':testimonial_data,
    'bar_Image_data_dict':bar_Image_data_dict,
    'categorie_data':categorie_data,
    'portfolio_Image_data':portfolio_Image_data,
    'line_bar_imgs_data':line_bar_imgs_data,

    }

    return render(request,"meerbalajcv/main/index.html",context)


@csrf_exempt
def contact_us_send(request):
    if request.method=="POST":
        now_date = datetime.datetime.now()
        name_form = request.POST['name_form']
        email_from = request.POST['email_from']
        from_message = request.POST['from_message']
        contact = Contact_U.objects.create(
            contact_from_name = name_form,
            contact_from_email = email_from,
            contact_message = from_message,
            contact_us_date_time=now_date
            )
        messages.success(request, "Message Has Been Sent Successfully!")

        return redirect ("/")

    else:
        messages.success(request, "Message Sending Failed!")
        return redirect ("/")
    return redirect ("/")












# admin panel dashboard



@login_required
@csrf_exempt
def admin_dashboard(request):

    profile_data = Profile.objects.all()
    title=""
    for x in profile_data:
        title = str(x.name)

    context = {
    
    'profile_data':profile_data,
    'title':title,

    }

    return render(request,"meerbalajcv/admin/index.html",context)



@login_required
@csrf_exempt
def admin_contact_entrie(request):

    profile_data = Profile.objects.all()
    title=""
    for x in profile_data:
        title = str(x.name)

    contact_data = Contact_U.objects.all()

    context = {

    'title':title,
    'profile_data':profile_data,
    'contact_data':contact_data,

    }

    return render(request,"meerbalajcv/admin/contact_entries.html",context)




@login_required
@csrf_exempt
def del_contact_entries(request,id_get):
    query_set = Contact_U.objects.get(id=id_get)
    query_set.delete()
    return HttpResponseRedirect('/contact_entries/')



@login_required
@csrf_exempt
def admin_meta_images(request):

    profile_data = Profile.objects.all()
    meta_data = Line_Bar_Image.objects.all()
    imgs = []
  
    title=""
    for x in profile_data:
        title = str(x.name)

    for x in meta_data:
        imgs.append(x.name_img)

    if request.method == "POST":
        form = upload_meta_image(request.POST, request.FILES)
        if form.is_valid():
            if not form['name_img'].value() in imgs:
                form.save()
                return redirect("/meta_images/")

            else:
                return redirect("/meta_images/")


    else:
        form = upload_meta_image() 



    context = {

    'form':form,
    'title':title,
    'profile_data':profile_data,
    'meta_data':meta_data,
    }

    return render(request,"meerbalajcv/admin/meta_images.html",context)





@login_required
@csrf_exempt
def del_meta_images_entries(request,id_get):
    query_set = Line_Bar_Image.objects.get(id=id_get)
    query_set.delete()
    return HttpResponseRedirect('/meta_images')



@login_required
@csrf_exempt
def add_categories(request):

    profile_data = Profile.objects.all()
    
    categories_data = Categorie.objects.all()
    imgs = []
  
    title=""
    for x in profile_data:
        title = str(x.name)

    for x in categories_data:
        imgs.append(x.name_category)

    if request.method == "POST":
        form = upload_category(request.POST)
        if form.is_valid():
            if not form['name_category'].value() in imgs:
                form.save()
                return redirect("/add_categories/")

            else:
                messages.success(request, "Category %s is already present! "%form['name_category'].value())
                return redirect("/add_categories/")


    else:
        form = upload_category() 



    context = {

    'form':form,
    'title':title,
    'profile_data':profile_data,
    'categories_data':categories_data,
    }

    return render(request,"meerbalajcv/admin/categories.html",context)



@login_required
@csrf_exempt
def del_categories_entries(request,id_get):
    query_set = Categorie.objects.get(id=id_get)

    try:
        query_set.delete()

    except:
        messages.success(request, "Category %s cannot be deleted because some images are assigned to this category!"%query_set)
        return redirect("/add_categories/")

    return HttpResponseRedirect('/add_categories/')





@login_required
@csrf_exempt
def add_portfolio_images(request):

    profile_data = Profile.objects.all()
    
    portfolio_images_data = Portfolio_Image.objects.all()
    imgs = []
  
    title=""
    for x in profile_data:
        title = str(x.name)

    for x in portfolio_images_data:
        imgs.append(x.name_project)

    if request.method == "POST":
        form = upload_portfolio_image(request.POST, request.FILES)
        if form.is_valid():
            if not form['name_project'].value() in imgs:
                form.save()
                return redirect("/add_portfolio_images/")

            else:
                messages.success(request, "Image with Name %s is already present! "%form['name_project'].value())
                return redirect("/add_portfolio_images/")


    else:
        form = upload_portfolio_image() 



    context = {

    'form':form,
    'title':title,
    'profile_data':profile_data,
    'portfolio_images_data':portfolio_images_data,
    }

    return render(request,"meerbalajcv/admin/images_items.html",context)





@login_required
@csrf_exempt
def del_port_images_entries(request,id_get):
    query_set = Portfolio_Image.objects.get(id=id_get)

    try:
        query_set.delete()

    except:
        messages.success(request, "Image %s cannot be deleted!"%query_set)
        return redirect("/add_portfolio_images/")

    return HttpResponseRedirect('/add_portfolio_images/')







@login_required
@csrf_exempt
def add_testimonials(request):

    profile_data = Profile.objects.all()
    
    testmonials_data = Testimonial.objects.all()
    imgs = []
  
    title=""
    for x in profile_data:
        title = str(x.name)

    for x in testmonials_data:
        imgs.append(x.client_feedback)

    if request.method == "POST":
        form = upload_testimonials(request.POST, request.FILES)
        if form.is_valid():
            if not form['client_feedback'].value() in imgs:
                form.save()
                return redirect("/add_testimonials/")

            else:
                messages.success(request, "A same feedback is already present with client name %s! "%form['client_name'].value())
                return redirect("/add_testimonials/")

    else:
        form = upload_testimonials() 


    test_count = testmonials_data.count()



    context = {

    'form':form,
    'title':title,
    'profile_data':profile_data,
    'testmonials_data':testmonials_data,
    'test_count':test_count,
    }

    return render(request,"meerbalajcv/admin/testimonials.html",context)





@login_required
@csrf_exempt
def del_testimonials_entries(request,id_get):
    query_set = Testimonial.objects.get(id=id_get)

    try:
        query_set.delete()

    except:
        messages.success(request, "Testimonial %s cannot be deleted!"%query_set)
        return redirect("/add_testimonials/")

    return HttpResponseRedirect('/add_testimonials/')





@login_required
@csrf_exempt
def edit_testimonials_entries(request,id_get):
    profile_data = Profile.objects.all()
  
    title=""
    for x in profile_data:
        title = str(x.name)
    query_set = Testimonial.objects.get(id=id_get)
    if request.method == "POST":
        form = edit_testimonials(request.POST, request.FILES, instance=query_set)
        if form.is_valid():
            form.save()
            messages.success(request, "Testimonial %s Successfully Updated!"%query_set)
            return redirect("/add_testimonials/")
        else:
            messages.success(request, "Testimonial %s Updation Failed!"%query_set)
            return redirect("/add_testimonials/")
    else:
        form = upload_testimonials(instance=query_set)

    context = {
    'title':title,
    'profile_data':profile_data,
    'form':form,
    }
    return render(request,"meerbalajcv/admin/edit_testimonials.html",context)



@login_required
@csrf_exempt
def add_completed_projects(request):

    profile_data = Profile.objects.all()
    
    completed_projects_data = Bar_Image.objects.all()

    list_len = len(completed_projects_data)

    title=""
    for x in profile_data:
        title = str(x.name)


        # color:#1ecab8 cell 
        # color:#1ecab8 smile 
        # color:#ff5da0 trophy

    context = {
    'title':title,
    'list_len':list_len,
    'completed_projects_data':completed_projects_data,
    'profile_data':profile_data,    
    }

    return render(request,"meerbalajcv/admin/completed_projects.html",context)


@login_required
@csrf_exempt
def edit_completed_project(request,id_get):

    profile_data = Profile.objects.all()
  
    title=""
    for x in profile_data:
        title = str(x.name)

    query_set = Bar_Image.objects.get(id=id_get)

    if request.method == "POST":
        form = Edit_completed_projects(request.POST, instance=query_set)
        if form.is_valid():
            form.save()
            messages.success(request, "%s Successfully Updated!"%query_set)
            return redirect("/add_completed_projects/")
        else:
            messages.success(request, "%s Updation Failed!"%query_set)
            return redirect("/add_completed_projects/")
    else:
        form = upload_completed_project(instance=query_set)
    
    context = {
    
    'title':title,
    'profile_data':profile_data,    
    'form':form,
    }

    return render(request,"meerbalajcv/admin/edit_completed_project.html",context)



@login_required
@csrf_exempt
def edit_profile(request,id_get):

    profile_data = Profile.objects.all()
  
    title=""
    for x in profile_data:
        title = str(x.name)

    query_set = Profile.objects.get(id=id_get)

    boolean_check = False
    if query_set.upload_cv:
        boolean_check=True
        
    if request.method == "POST":
        form = edit_profile_user(request.POST, request.FILES, instance=query_set)
        if form.is_valid():
            if form['check_remove_cv'].value() == True:
                if form['upload_cv']:
                    value = form['upload_cv'].value()
                    value.delete()

                else:
                    pass

            form.save()
            messages.success(request, "Profile %s Successfully Updated!"%query_set)
            return redirect("/admin/")
        else:
            messages.success(request, "Profile %s Updation Failed!"%query_set)
            return redirect("/admin/")
    else:
        form = upload_profile_user(instance=query_set)
    
    context = {
    
    'title':title,
    'boolean_check':boolean_check,
    'profile_data':profile_data,    
    'form':form,
    }

    return render(request,"meerbalajcv/admin/edit_profile.html",context)












@login_required
@csrf_exempt
def upload_profile(request):

    profile_data = Profile.objects.all()
    title=""
    for x in profile_data:
        title = str(x.name)



    if profile_data.count()>=1:
        return redirect('/admin/')

    else:

        if request.method == "POST":
            form = upload_profile_user(request.POST , request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Profile %s Successfully Added! "%form['name'].value())
                return redirect("/admin/")
            else:
                messages.success(request, "Profile %s Addition Failed! "%form['name'].value())
                return redirect("/admin/")
        else:
            form = upload_profile_user()



    context = {

    'form':form,
    'title':title,
    'profile_data':profile_data,
    }

    return render(request,"meerbalajcv/admin/add_profile.html",context)




@login_required
@csrf_exempt
def add_completed_projects_now(request):

    profile_data = Profile.objects.all()
    com_data = Bar_Image.objects.all()
    title=""
    for x in profile_data:
        title = str(x.name)



    if com_data.count()>=3:
        return redirect('/add_completed_projects/')

    else:

        if request.method == "POST":
            form = Add_completed_projects_form_now(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, " %s Successfully Added! "%form['completed_before_name'].value())
                return redirect("/add_completed_projects/")
            else:
                messages.success(request, " %s Addition Failed! "%form['completed_before_name'].value())
                return redirect("/add_completed_projects/")
        else:
            form = Add_completed_projects_form_now()


    context = {

    'form':form,
    'title':title,
    'profile_data':profile_data,
    }

    return render(request,"meerbalajcv/admin/add_completed_projects.html",context)





@login_required
@csrf_exempt
def add_education(request):

    profile_data = Profile.objects.all()
    
    education_data = Education.objects.all()
    names = []
  
    title=""
    for x in profile_data:
        title = str(x.name)

    for x in education_data:
        names.append(x.degree)

    if request.method == "POST":
        form = upload_education(request.POST)
        if form.is_valid():
            if not form['degree'].value() in names:
                form.save()
                return redirect("/add_education/")

            else:
                messages.success(request, " %s is already present! "%form['degree'].value())
                return redirect("/add_education/")

    else:
        form = upload_education() 



    context = {

    'form':form,
    'title':title,
    'profile_data':profile_data,
    'education_data':education_data,
    }

    return render(request,"meerbalajcv/admin/education.html",context)





@login_required
@csrf_exempt
def edit_educations_entries(request,id_get):

    profile_data = Profile.objects.all()
  
    title=""
    for x in profile_data:
        title = str(x.name)

    query_set = Education.objects.get(id=id_get)

    if request.method == "POST":
        form = edit_education_user_data(request.POST,instance=query_set)
        if form.is_valid():
            form.save()
            messages.success(request, "%s Successfully Updated!"%query_set)
            return redirect("/add_education/")
        else:
            messages.success(request, "%s Updation Failed!"%query_set)
            return redirect("/add_education/")
    else:
        form = edit_education_user_data(instance=query_set)
    
    context = {
    
    'title':title,
    'profile_data':profile_data,    
    'form':form,
    }

    return render(request,"meerbalajcv/admin/edit_education.html",context)




@login_required
@csrf_exempt
def delete_educations_entries(request,id_get):
    query_set = Education.objects.get(id=id_get)
    query_set.delete()
    return HttpResponseRedirect('/add_education/')





@login_required
@csrf_exempt
def delete_experiences_entries(request,id_get):
    query_set = Experience.objects.get(id=id_get)
    query_set.delete()
    return HttpResponseRedirect('/add_experience/')




@login_required
@csrf_exempt
def delete_skills_entries(request,id_get):
    query_set = Skill.objects.get(id=id_get)
    query_set.delete()
    return HttpResponseRedirect('/add_skill/')



@login_required
@csrf_exempt
def add_experience(request):

    profile_data = Profile.objects.all()
    
    experience_data = Experience.objects.all()
    names = []
  
    title=""
    for x in profile_data:
        title = str(x.name)

    for x in experience_data:
        names.append(x.company)

    if request.method == "POST":
        form = upload_experience(request.POST)
        if form.is_valid():
            if not form['company'].value() in names:
                form.save()
                return redirect("/add_experience/")

            else:
                messages.success(request, " %s is already present! "%form['company'].value())
                return redirect("/add_experience/")

    else:
        form = upload_experience() 



    context = {

    'form':form,
    'title':title,
    'profile_data':profile_data,
    'experience_data':experience_data,
    }

    return render(request,"meerbalajcv/admin/experience.html",context)






@login_required
@csrf_exempt
def edit_experiences_entries(request,id_get):

    profile_data = Profile.objects.all()
  
    title=""
    for x in profile_data:
        title = str(x.name)

    query_set = Experience.objects.get(id=id_get)

    if request.method == "POST":
        form = edit_experience_user_data(request.POST,instance=query_set)
        if form.is_valid():
            form.save()
            messages.success(request, "%s Successfully Updated!"%query_set)
            return redirect("/add_experience/")
        else:
            messages.success(request, "%s Updation Failed!"%query_set)
            return redirect("/add_experience/")
    else:
        form = edit_experience_user_data(instance=query_set)
    
    context = {
    
    'title':title,
    'profile_data':profile_data,    
    'form':form,
    }

    return render(request,"meerbalajcv/admin/edit_experience.html",context)








@login_required
@csrf_exempt
def add_skill(request):

    profile_data = Profile.objects.all()
    
    skill_data = Skill.objects.all()
    names = []
  
    title=""
    for x in profile_data:
        title = str(x.name)

    for x in skill_data:
        names.append(x.skill_name)

    if request.method == "POST":
        form = upload_skills(request.POST)
        if form.is_valid():
            if not form['skill_name'].value() in names:

                skillcounts = int(form['skill_count'].value())
                if skillcounts > 100:
                    messages.success(request, "Please add count between 0-100 !")
                    return redirect("/add_skill/")
                else:
                    form.save()
                    messages.success(request, "%s Successfully Added!"%form['skill_name'].value())
                    return redirect("/add_skill/")


            else:
                messages.success(request, " %s is already present! "%form['skill_name'].value())
                return redirect("/add_skill/")

    else:
        form = upload_skills() 



    context = {

    'form':form,
    'title':title,
    'profile_data':profile_data,
    'skill_data':skill_data,
    }

    return render(request,"meerbalajcv/admin/skills.html",context)






@login_required
@csrf_exempt
def edit_skills_entries(request,id_get):

    profile_data = Profile.objects.all()
  
    title=""
    for x in profile_data:
        title = str(x.name)

    query_set = Skill.objects.get(id=id_get)

    if request.method == "POST":
        form = edit_skills_user_data(request.POST,instance=query_set)
        if form.is_valid():

            skillcounts = int(form['skill_count'].value())
            if skillcounts > 100:
                messages.success(request, "Please add count between 0-100 !")
                return redirect('/edit_skills_entries/%s'%str(id_get))

            else:
                form.save()
                messages.success(request, "%s Successfully Updated!"%query_set)
                return redirect("/add_skill/")
        else:
            messages.success(request, "%s Updation Failed!"%query_set)
            return redirect("/add_skill/")
    else:
        form = edit_skills_user_data(instance=query_set)
    
    context = {
    
    'title':title,
    'profile_data':profile_data,    
    'form':form,
    }

    return render(request,"meerbalajcv/admin/edit_skill.html",context)