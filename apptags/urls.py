# from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'apptags'



urlpatterns = [
    path('alltags/', views.home, name='hashtag'),
    path('<slug:slug>/' , views.detail , name='detail'),
# # #------------------------------------------------------------------------------
# # #------------------------------------------------------------------------------
    # path('alltags/', views.Alltags, name='Alltags'),
    # path('alltags/<slug:slug>/' , views.Det_Alltags , name='Det_Alltags'),
# # # #------------------------------------------------------------------------------
# # # #------------------------------------------------------------------------------

    path('popular/', views.Popular, name='Popular'),
    path('<slug:slug>/' , views.Det_Popular , name='Det_Popular'),
# # # #------------------------------------------------------------------------------
# # # #------------------------------------------------------------------------------
# # #
    path('nature/', views.Nature, name='Nature'),
    path('nature/<slug:slug>/' , views.Det_Nature , name='Det_Nature'),
# # # #------------------------------------------------------------------------------
# # # #------------------------------------------------------------------------------
# # #
    path('weather-seasons/', views.Weather_Seasons, name='Weather_Seasons'),
    path('weather-seasons/<slug:slug>/' , views.Det_Weather_Seasons , name='Det_Weather_Seasons'),
# # # #------------------------------------------------------------------------------
# # # #------------------------------------------------------------------------------
# # #
    path('animals/', views.Animals, name='Animals'),
    path('animals/<slug:slug>/' , views.Det_Animals , name='Det_Animals'),
# # # #------------------------------------------------------------------------------
# # # #------------------------------------------------------------------------------
# # #
    path('social-people/', views.Social_People, name='Social_People'),
    path('social-people/<slug:slug>/' , views.Det_Social_People , name='Det_Social_People'),
# # # #------------------------------------------------------------------------------
# # # #------------------------------------------------------------------------------
# # #
    path('holidays-celebrations/', views.Holidays_Celebrations, name='Holidays_Celebrations'),
    path('holidays-celebrations/<slug:slug>/' , views.Det_Holidays_Celebrations , name='Det_Holidays_Celebrations'),
# # # #------------------------------------------------------------------------------
# # # #------------------------------------------------------------------------------
# # #
    path('family/', views.Family, name='Family'),
    path('family/<slug:slug>/' , views.Det_Family , name='Det_Family'),
# # # #------------------------------------------------------------------------------
# # # #------------------------------------------------------------------------------
# # #
    path('art-photography/', views.Art_Photography, name='Art_Photography'),
    path('art-photography/<slug:slug>/' , views.Det_Art_Photography , name='Det_Art_Photography'),
# # # #------------------------------------------------------------------------------
# # # #------------------------------------------------------------------------------
# # #
    path('urban/', views.Urban, name='Urban'),
    path('urban/<slug:slug>/' , views.Det_Urban , name='Det_Urban'),
# # # #------------------------------------------------------------------------------
# # # #------------------------------------------------------------------------------
# # #
    path('food/', views.Food, name='Food'),
    path('food/<slug:slug>/' , views.Det_Food , name='Det_Food'),
# # # #------------------------------------------------------------------------------
# # # #------------------------------------------------------------------------------
# # #
    path('fashion/', views.Fashion, name='Fashion'),
    path('fashion/<slug:slug>/' , views.Det_Fashion , name='Det_Fashion'),
# # # #------------------------------------------------------------------------------
# # # #------------------------------------------------------------------------------
# # #
    path('celebrities/', views.Celebrities, name='Celebrities'),
    path('celebrities/<slug:slug>/' , views.Det_Celebrities , name='Det_Celebrities'),
# # # #------------------------------------------------------------------------------
# # # #------------------------------------------------------------------------------
# # #
    path('entertainment/', views.Entertainment, name='Entertainment'),
    path('entertainment/<slug:slug>/' , views.Det_Entertainment , name='Det_Entertainment'),
# # # #------------------------------------------------------------------------------
# # # #------------------------------------------------------------------------------
# # #
    path('follow-shoutout-like-comment/', views.Follow_Shoutout_Like_Comment, name='Follow_Shoutout_Like_Comment'),
    path('follow-shoutout-like-comment/<slug:slug>/' , views.Det_Follow_Shoutout_Like_Comment , name='Det_Follow_Shoutout_Like_Comment'),
# # # #------------------------------------------------------------------------------
# # # #------------------------------------------------------------------------------
# # #
    path('travel-active-sports/', views.Travel_Active_Sports, name='Travel_Active_Sports'),
    path('travel-active-sports/<slug:slug>/' , views.Det_Travel_Active_Sports , name='Det_Travel_Active_Sports'),
# # # #------------------------------------------------------------------------------
# # # #------------------------------------------------------------------------------
# # #
    path('electronics/', views.Electronics, name='Electronics'),
    path('electronics/<slug:slug>/' , views.Det_Electronics , name='Det_Electronics'),
# # # #------------------------------------------------------------------------------
# # # #------------------------------------------------------------------------------
# # #
    path('textart/', views.Textart, name='Textart'),
    path('textart/<slug:slug>/' , views.Det_Textart , name='Det_Textart'),
# # # #------------------------------------------------------------------------------
# # # #------------------------------------------------------------------------------
# # #
    path('other/', views.Other, name='Other'),
    path('other/<slug:slug>/' , views.Det_Other , name='Det_Other'),
# # #------------------------------------------------------------------------------
# # #------------------------------------------------------------------------------
# #
]
