from django.shortcuts import render
# from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from . import models
from django.shortcuts import  get_object_or_404



# #-------------------------------------------------------------------
#Start-home
def home(request):
    all_tags = models.Hashtags.objects.all()
    context = {
        'all_tags' : all_tags,
    }
    return render(request , 'home.html' , context)


def detail(request,slug):
    one_tag = models.Hashtags.objects.get(slug=slug)
    context = {
        'one_tag':one_tag
    }
    return render(request,'one_tag.html' ,context)
# #end-home
# # #-------------------------------------------------------------------
# # #-------------------------------------------------------------------
# #Start-Popular
#
def Popular(request):
    popular = models.Popular.objects.all()
    context={
        'popular':popular
    }
    return render(request , 'popular.html' , context)
# ######################
def Det_Popular(request,slug):
    det_popular = models.Popular.objects.get(slug=slug)
    context={
        'det_popular':det_popular
    }
    return render(request,'det_popular.html',context)
#  #end-Popular
# #
# # #Start-Nature
# #tags__name='popular'
def Nature(request):
    nature = models.Nature.objects.filter(tags="Nature")
    context={
        'nature':nature
    }
    return render(request , 'nature.html' , context)

def Det_Nature(request,slug):
    det_nature = models.Nature.objects.get(slug=slug)
    context={
        'det_nature':det_nature
    }
    return render(request,'det_nature.html',context)
# # #end-Nature
# # #-------------------------------------------------------------------
# #
# # #Start-Weather_Seasons
# #
def Weather_Seasons(request):
    weather_seasons = models.Weather_Seasons.objects.filter(tags="Weather/Seasons")
    context={
        'weather_seasons':weather_seasons
    }
    return render(request , 'weather_seasons.html' , context)
def Det_Weather_Seasons(request,slug):
    det_weather_seasons = models.Weather_Seasons.objects.get(slug=slug)
    context={
        'det_weather_seasons':det_weather_seasons
    }
    return render(request,'det_weather_seasons.html',context)
# # #end-Weather_Seasons
# # #-------------------------------------------------------------------
# #
# # #Start-Animals
# #
def Animals(request):
    animals = models.Animals.objects.filter(tags="Animals")
    context={
        'animals':animals
    }
    return render(request , 'animals.html' , context)
def Det_Animals(request,slug):
    det_animals = models.Animals.objects.get(slug=slug)
    context={
        'det_animals':det_animals
    }
    return render(request,'det_animals.html',context)
# # #end-Animals
# # #-------------------------------------------------------------------
# #
# # #Start-Social_People
# #
def Social_People(request):
    social_people = models.Social_People.objects.filter(tags="Social/People")
    context={
        'social_people':social_people
    }
    return render(request , 'social_people.html' , context)
def Det_Social_People(request,slug):
    det_social_people = models.Social_People.objects.get(slug=slug)
    context={
        'det_social_people':det_social_people
    }
    return render(request,'det_social_people.html',context)
# # #end-Social_People
# # #-------------------------------------------------------------------
# #
# # #Start-Holidays_Celebrations
# #
def Holidays_Celebrations(request):
    holidays_celebrations = models.holidays_celebrations.objects.filter(tags="Holidays/Celebrations")
    context={
        'holidays_celebrations':holidays_celebrations
    }
    return render(request , 'holidays_celebrations.html' , context)
def Det_Holidays_Celebrations(request,slug):
    det_holidays_celebrations = models.holidays_celebrations.objects.get(slug=slug)
    context={
        'det_holidays_celebrations':det_holidays_celebrations
    }
    return render(request,'det_holidays_celebrations.html',context)
# # #end-Holidays_Celebrations
# # #-------------------------------------------------------------------
# #
# # #Start-Family
# #
def Family(request):
    family = models.Family.objects.filter(tags="Family")
    context={
        'family':family
    }
    return render(request , 'family.html' , context)
def Det_Family(request,slug):
    det_family = models.Family.objects.get(slug=slug)
    context={
        'det_family':det_family
    }
    return render(request,'det_family.html',context)
# # #end-Family
# # #-------------------------------------------------------------------
# #
# # #Start-Art_Photography
# #
def Art_Photography(request):
    art_Photography = models.Art_Photography.objects.filter(tags="Art/Photography")
    context={
        'art_Photography':art_Photography
    }
    return render(request , 'art_Photography.html' , context)
def Det_Art_Photography(request,slug):
    det_art_photography = models.Art_Photography.objects.get(slug=slug)
    context={
        'det_art_photography':det_art_photography
    }
    return render(request,'det_art_photography.html',context)
# # #end-Art_Photography
# # #-------------------------------------------------------------------
# #
# # #Start-Urban
# #
def Urban(request):
    urban = models.Urban.objects.filter(tags="Urban")
    context={
        'urban':urban
    }
    return render(request , 'urban.html' , context)
def Det_Urban(request,slug):
    det_urban = models.Urban.objects.get(slug=slug)
    context={
        'det_urban':det_urban
    }
    return render(request,'det_urban.html',context)
# # #end-Urban
# # #-------------------------------------------------------------------
# #
# # #Start-Food
# #
def Food(request):
    food = models.Food.objects.filter(tags="Food")
    context={
        'food':food
    }
    return render(request , 'food.html' , context)
def Det_Food(request,slug):
    det_food = models.Food.objects.get(slug=slug)
    context={
        'det_food':det_food
    }
    return render(request,'det_food.html',context)
# # #end-Food
# # #-------------------------------------------------------------------
# #
# # #Start-Fashion
# #
def Fashion(request):
    fashion = models.Fashion.objects.filter(tags="Fashion")
    context={
        'fashion':fashion
    }
    return render(request , 'fashion.html' , context)
def Det_Fashion(request,slug):
    det_fashion = models.Fashion.objects.get(slug=slug)
    context={
        'det_fashion':det_fashion
    }
    return render(request,'det_fashion.html',context)
# # #end-Fashion
# # #-------------------------------------------------------------------
# #
# # #Start-Celebrities
# #
def Celebrities(request):
    celebrities = models.Celebrities.objects.filter(tags="Celebrities")
    context={
        'celebrities':celebrities
    }
    return render(request , 'celebrities.html' , context)
def Det_Celebrities(request,slug):
    det_celebrities = models.Celebrities.objects.get(slug=slug)
    context={
        'det_celebrities':det_celebrities
    }
    return render(request,'det_celebrities.html',context)
# # #end-Celebrities
# # #-------------------------------------------------------------------
# #
# # #Start-Entertainment
# #
def Entertainment(request):
    entertainment = models.Entertainment.objects.filter(tags="Entertainment")
    context={
        'entertainment':entertainment
    }
    return render(request , 'entertainment.html' , context)
def Det_Entertainment(request,slug):
    det_entertainment = models.Entertainment.objects.get(slug=slug)
    context={
        'det_entertainment':det_entertainment
    }
    return render(request,'det_entertainment.html',context)
# # #end-Entertainment
# # #-------------------------------------------------------------------
# #
# # #Start-Follow_Shoutout_Like_Comment
# #
def Follow_Shoutout_Like_Comment(request):
    follow_shoutout_like_comment = models.Follow_Shoutout_Like_Comment.objects.filter(tags="Follow/Shoutout/Like/Comment")
    context={
        'follow_shoutout_like_comment':follow_shoutout_like_comment
    }
    return render(request , 'follow_shoutout_like_comment.html' , context)
def Det_Follow_Shoutout_Like_Comment(request,slug):
    det_follow_shoutout_like_comment = models.Follow_Shoutout_Like_Comment.objects.get(slug=slug)
    context={
        'det_follow_shoutout_like_comment':det_follow_shoutout_like_comment
    }
    return render(request,'det_follow_shoutout_like_comment.html',context)
# # #end-Follow_Shoutout_Like_Comment
# # #-------------------------------------------------------------------
# #
# # #Start-Travel_Active_Sports
# #
def Travel_Active_Sports(request):
    travel_active_sports = models.Travel_Active_Sports.objects.filter(tags="Travel/active/Sports")
    context={
        'travel_active_sports':travel_active_sports
    }
    return render(request , 'travel_active_sports.html' , context)
def Det_Travel_Active_Sports(request,slug):
    det_travel_active_sports = models.Travel_Active_Sports.objects.get(slug=slug)
    context={
        'det_travel_active_sports':det_travel_active_sports
    }
    return render(request,'det_travel_active_sports.html',context)
# # #end-Travel_Active_Sports
# # #-------------------------------------------------------------------
# #
# # #Start-Electronics
# #
def Electronics(request):
    electronics = models.Electronics.objects.filter(tags="Electronics")
    context={
        'electronics':electronics
    }
    return render(request , 'electronics.html' , context)
def Det_Electronics(request,slug):
    det_electronics = models.Electronics.objects.get(slug=slug)
    context={
        'det_electronics':det_electronics
    }
    return render(request,'det_electronics.html',context)
# # #end-Electronics
# # #-------------------------------------------------------------------
# #
# # #Start-Textart
# #
def Textart(request):
    textart = models.Textart.objects.filter(tags="Text Art")
    context={
        'textart':textart
    }
    return render(request , 'textart.html' , context)
def Det_Textart(request,slug):
    det_textart = models.Textart.objects.get(slug=slug)
    context={
        'det_textart':det_textart
    }
    return render(request,'det_textart.html',context)
# # #end-Textart
# # #-------------------------------------------------------------------
# #
# # #Start-other
# #
def Other(request):
    other = models.Other.objects.filter(tags="Other")
    context={
        'other':other
    }
    return render(request , 'other.html' , context)
def Det_Other(request,slug):
    det_other = models.Other.objects.get(slug=slug)
    context={
        'det_other':det_other
    }
    return render(request,'det_other.html',context)
# # #end-other
# #-------------------------------------------------------------------
#
#
#
#
# # def listing(request):
# #     contact_list = hashtags.objects.all()
# #     paginator = Paginator(contact_list, 15) # Show 25 contacts per page
# #
# #     page = request.GET.get('page')
# #     hashtags = paginator.get_page(page)
# #     context ={
# #         'contacts': contacts
# #     }
# #     return render(request, 'list.html', context)
