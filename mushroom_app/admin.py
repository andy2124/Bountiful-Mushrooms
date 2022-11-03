from django.contrib import admin
from.models import * #the star is a wild card giving access to the whole page of models.py 

admin.site.register(Mushroom)
# admin.site.register(PostMushroom)
