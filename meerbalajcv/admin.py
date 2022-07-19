# Register your models here.


from django.contrib import admin
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



admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Bar_Image)
admin.site.register(Testimonial)
admin.site.register(Categorie)
admin.site.register(Portfolio_Image)
admin.site.register(Line_Bar_Image)
admin.site.register(Contact_U)

admin.site.site_header = "Meer Balaj Admin Portal"
admin.site.site_title = "Meer Balaj Admin Portal"
admin.site.index_title = "Welcome to Meer Balaj CV Admin Portal"