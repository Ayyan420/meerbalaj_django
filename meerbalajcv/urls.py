
from django.urls import path,include
from . import views

from django.contrib import admin


from django.conf import settings

from django.conf.urls import url

from django.views.static import serve


urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),

    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    
    path('', views.home , name = "Home"),
    path('admin/', views.admin_dashboard , name = "Admin"),
    path('contact_us/', views.contact_us_send , name = "contact_us_send"),


    path('meta_images/', views.admin_meta_images , name = "admin_meta_images"),
    path('add_categories/', views.add_categories , name = "add_categories"),
    path('add_portfolio_images/', views.add_portfolio_images , name = "add_portfolio_images"),
    path('add_testimonials/', views.add_testimonials , name = "add_testimonials"),
    path('add_completed_projects/', views.add_completed_projects , name = "add_completed_projects"),
    path('contact_entries/', views.admin_contact_entrie , name = "admin_contact_entrie"),
    
    path('del_contact_entries/<int:id_get>',views.del_contact_entries , name = "Del_contact_entries"),
    path('del_meta_images_entries/<int:id_get>',views.del_meta_images_entries , name = "Del_images_entries"),
    path('del_categories_entries/<int:id_get>',views.del_categories_entries , name = "Del_cat_entries"),
    path('del_port_images_entries/<int:id_get>',views.del_port_images_entries , name = "Del_port_images_entries"),
    path('del_testimonials_entries/<int:id_get>',views.del_testimonials_entries , name = "Del_testimonials_entries"),
    path('edit_testimonials_entries/<int:id_get>',views.edit_testimonials_entries , name = "Edit_testimonials_entries"),
    path('edit_completed_project/<int:id_get>',views.edit_completed_project , name = "Edit_completed_project"),
    path('edit_profile/<int:id_get>',views.edit_profile , name = "Edit_profile"),
    path('edit_educations_entries/<int:id_get>',views.edit_educations_entries , name = "Edit_educations_entries"),
    path('edit_experiences_entries/<int:id_get>',views.edit_experiences_entries , name = "Edit_experiences_entries"),
    path('upload_profile/',views.upload_profile , name = "Upload_profile"),
    path('add_completed_projects_now/',views.add_completed_projects_now , name = "Add_completed_projects_now"),
    path('add_education/', views.add_education , name = "add_education"),
    path('add_experience/', views.add_experience , name = "add_experience"),
    path('add_skill/', views.add_skill , name = "add_skill"),

    path('delete_educations_entries/<int:id_get>',views.delete_educations_entries , name = "Delete_educations_entries"),
    path('delete_experiences_entries/<int:id_get>',views.delete_experiences_entries , name = "Delete_experiences_entries"),
    path('delete_skills_entries/<int:id_get>',views.delete_skills_entries , name = "Delete_skills_entries"),
    path('edit_skills_entries/<int:id_get>',views.edit_skills_entries , name = "Edit_skills_entries"),

]



admin.site.site_header = "Meer Balaj Admin Portal"
admin.site.site_title = "Meer Balaj Admin Portal"
admin.site.index_title = "Welcome to Meer Balaj CV Admin Portal"