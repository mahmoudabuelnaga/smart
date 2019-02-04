from django.contrib import admin
from . import models
# from .models import Popular
# from .models import Nature
# from .models import Weather_Seasons
# from .models import Animals
# from .models import Social_People
# from .models import Holidays_Celebrations
# from .models import Family
# from .models import Art_Photography
# from .models import Urban
# from .models import Food
# from .models import Fashion
# from .models import Celebrities
# from .models import Entertainment
# from .models import Follow_Shoutout_Like_Comment
# from .models import Travel_Active_Sports
# from .models import Electronics
# from .models import Textart
# from .models import Other
# Register your models here.
admin.site.register(models.Hashtags)
admin.site.register(models.Popular)
admin.site.register(models.Nature)
admin.site.register(models.Weather_Seasons)
admin.site.register(models.Animals)
admin.site.register(models.Social_People)
admin.site.register(models.Holidays_Celebrations)
admin.site.register(models.Family)
admin.site.register(models.Art_Photography)
admin.site.register(models.Urban)
admin.site.register(models.Food)
admin.site.register(models.Fashion)
admin.site.register(models.Celebrities)
admin.site.register(models.Entertainment)
admin.site.register(models.Follow_Shoutout_Like_Comment)
admin.site.register(models.Travel_Active_Sports)
admin.site.register(models.Electronics)
admin.site.register(models.Textart)
admin.site.register(models.Other)
