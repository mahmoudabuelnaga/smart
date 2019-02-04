from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.text import slugify
# Create your models here.



class Hashtags(models.Model):
    user    = models.ForeignKey(User , on_delete=models.CASCADE)
    title   = models.CharField(blank=True, max_length=100)
    slug    = models.SlugField(null=True,blank=True)
    content = models.TextField(blank=True)
    date    = models.DateTimeField(blank=True, default=datetime.datetime.now)
    img     = models.ImageField(upload_to="img-tags")
    tags    = models.CharField(blank=True, max_length=100)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Hashtags,self).save(*args,**kwargs)

    def __str__(self):
        return self.title


class Popular(models.Model):
    user     = models.ForeignKey(User , on_delete=models.CASCADE)
    hashtag = models.ForeignKey(Hashtags , on_delete=models.CASCADE)
    # title    = models.CharField(blank=True, max_length=100)
    slug    = models.SlugField(null=True,blank=True)
    content = models.TextField(blank=True)
    date    = models.DateTimeField(blank=True, default=datetime.datetime.now)
    img     = models.ImageField(upload_to="img-tags")
    tags    = models.CharField(blank=True, max_length=100)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.hashtag)
        super(Popular,self).save(*args,**kwargs)

    def __str__(self):
        return self.hashtag

class Nature(models.Model):
    user    = models.ForeignKey(User , on_delete=models.CASCADE)
    hashtag = models.ForeignKey(Hashtags , on_delete=models.CASCADE)
    # title   = models.CharField(blank=True, max_length=100)
    slug    = models.SlugField(null=True,blank=True)
    content = models.TextField(blank=True)
    date    = models.DateTimeField(blank=True, default=datetime.datetime.now)
    img     = models.ImageField(upload_to="img-tags")
    tags    = models.CharField(blank=True, max_length=100)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.hashtag)
        super(Nature,self).save(*args,**kwargs)

    def __str__(self):
        return self.hashtag

class Weather_Seasons(models.Model):
    user    = models.ForeignKey(User , on_delete=models.CASCADE)
    hashtag = models.ForeignKey(Hashtags , on_delete=models.CASCADE)
    # title   = models.CharField(blank=True, max_length=100)
    slug    = models.SlugField(null=True,blank=True)
    content = models.TextField(blank=True)
    date    = models.DateTimeField(blank=True, default=datetime.datetime.now)
    img     = models.ImageField(upload_to="img-tags")
    tags    = models.CharField(blank=True, max_length=100)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.hashtag)
        super(Weather_Seasons,self).save(*args,**kwargs)

    def __str__(self):
        return self.hashtag

class Animals(models.Model):
    user    = models.ForeignKey(User , on_delete=models.CASCADE)
    hashtag = models.ForeignKey(Hashtags , on_delete=models.CASCADE)
    # title   = models.CharField(blank=True, max_length=100)
    slug    = models.SlugField(null=True,blank=True)
    content = models.TextField(blank=True)
    date    = models.DateTimeField(blank=True, default=datetime.datetime.now)
    img     = models.ImageField(upload_to="img-tags")
    tags    = models.CharField(blank=True, max_length=100)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.hashtag)
        super(Animals,self).save(*args,**kwargs)

    def __str__(self):
        return self.hashtag

class Social_People(models.Model):
    user    = models.ForeignKey(User , on_delete=models.CASCADE)
    hashtag = models.ForeignKey(Hashtags , on_delete=models.CASCADE)
    # title   = models.CharField(blank=True, max_length=100)
    slug    = models.SlugField(null=True,blank=True)
    content = models.TextField(blank=True)
    date    = models.DateTimeField(blank=True, default=datetime.datetime.now)
    img     = models.ImageField(upload_to="img-tags")
    tags    = models.CharField(blank=True, max_length=100)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.hashtag)
        super(Social_People,self).save(*args,**kwargs)

    def __str__(self):
        return self.hashtag

class Holidays_Celebrations(models.Model):
    user    = models.ForeignKey(User , on_delete=models.CASCADE)
    hashtag = models.ForeignKey(Hashtags , on_delete=models.CASCADE)
    # title   = models.CharField(blank=True, max_length=100)
    slug    = models.SlugField(null=True,blank=True)
    content = models.TextField(blank=True)
    date    = models.DateTimeField(blank=True, default=datetime.datetime.now)
    img     = models.ImageField(upload_to="img-tags")
    tags    = models.CharField(blank=True, max_length=100)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.hashtag)
        super(Holidays_Celebrations,self).save(*args,**kwargs)

    def __str__(self):
        return self.hashtag

class Family(models.Model):
    user    = models.ForeignKey(User , on_delete=models.CASCADE)
    hashtag = models.ForeignKey(Hashtags , on_delete=models.CASCADE)
    # title   = models.CharField(blank=True, max_length=100)
    slug    = models.SlugField(null=True,blank=True)
    content = models.TextField(blank=True)
    date    = models.DateTimeField(blank=True, default=datetime.datetime.now)
    img     = models.ImageField(upload_to="img-tags")
    tags    = models.CharField(blank=True, max_length=100)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.hashtag)
        super(Family,self).save(*args,**kwargs)

    def __str__(self):
        return self.hashtag

class Art_Photography(models.Model):
    user    = models.ForeignKey(User , on_delete=models.CASCADE)
    hashtag = models.ForeignKey(Hashtags , on_delete=models.CASCADE)
    # title   = models.CharField(blank=True, max_length=100)
    slug    = models.SlugField(null=True,blank=True)
    content = models.TextField(blank=True)
    date    = models.DateTimeField(blank=True, default=datetime.datetime.now)
    img     = models.ImageField(upload_to="img-tags")
    tags    = models.CharField(blank=True, max_length=100)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.hashtag)
        super(Art_Photography,self).save(*args,**kwargs)

    def __str__(self):
        return self.hashtag

class Urban(models.Model):
    user    = models.ForeignKey(User , on_delete=models.CASCADE)
    hashtag = models.ForeignKey(Hashtags , on_delete=models.CASCADE)
    # title   = models.CharField(blank=True, max_length=100)
    slug    = models.SlugField(null=True,blank=True)
    content = models.TextField(blank=True)
    date    = models.DateTimeField(blank=True, default=datetime.datetime.now)
    img     = models.ImageField(upload_to="img-tags")
    tags    = models.CharField(blank=True, max_length=100)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.hashtag)
        super(Urban,self).save(*args,**kwargs)

    def __str__(self):
        return self.hashtag

class Food(models.Model):
    user    = models.ForeignKey(User , on_delete=models.CASCADE)
    hashtag = models.ForeignKey(Hashtags , on_delete=models.CASCADE)
    # title   = models.CharField(blank=True, max_length=100)
    slug    = models.SlugField(null=True,blank=True)
    content = models.TextField(blank=True)
    date    = models.DateTimeField(blank=True, default=datetime.datetime.now)
    img     = models.ImageField(upload_to="img-tags")
    tags    = models.CharField(blank=True, max_length=100)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.hashtag)
        super(Food,self).save(*args,**kwargs)

    def __str__(self):
        return self.hashtag

class Fashion(models.Model):
    user    = models.ForeignKey(User , on_delete=models.CASCADE)
    hashtag = models.ForeignKey(Hashtags , on_delete=models.CASCADE)
    # title   = models.CharField(blank=True, max_length=100)
    slug    = models.SlugField(null=True,blank=True)
    content = models.TextField(blank=True)
    date    = models.DateTimeField(blank=True, default=datetime.datetime.now)
    img     = models.ImageField(upload_to="img-tags")
    tags    = models.CharField(blank=True, max_length=100)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.hashtag)
        super(Fashion,self).save(*args,**kwargs)

    def __str__(self):
        return self.hashtag

class Celebrities(models.Model):
    user    = models.ForeignKey(User , on_delete=models.CASCADE)
    hashtag = models.ForeignKey(Hashtags , on_delete=models.CASCADE)
    # title   = models.CharField(blank=True, max_length=100)
    slug    = models.SlugField(null=True,blank=True)
    content = models.TextField(blank=True)
    date    = models.DateTimeField(blank=True, default=datetime.datetime.now)
    img     = models.ImageField(upload_to="img-tags")
    tags    = models.CharField(blank=True, max_length=100)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.hashtag)
        super(Celebrities,self).save(*args,**kwargs)

    def __str__(self):
        return self.hashtag

class Entertainment(models.Model):
    user    = models.ForeignKey(User , on_delete=models.CASCADE)
    hashtag = models.ForeignKey(Hashtags , on_delete=models.CASCADE)
    # title   = models.CharField(blank=True, max_length=100)
    slug    = models.SlugField(null=True,blank=True)
    content = models.TextField(blank=True)
    date    = models.DateTimeField(blank=True, default=datetime.datetime.now)
    img     = models.ImageField(upload_to="img-tags")
    tags    = models.CharField(blank=True, max_length=100)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.hashtag)
        super(Entertainment,self).save(*args,**kwargs)

    def __str__(self):
        return self.hashtag

class Follow_Shoutout_Like_Comment(models.Model):
    user    = models.ForeignKey(User , on_delete=models.CASCADE)
    hashtag = models.ForeignKey(Hashtags , on_delete=models.CASCADE)
    # title   = models.CharField(blank=True, max_length=100)
    slug    = models.SlugField(null=True,blank=True)
    content = models.TextField(blank=True)
    date    = models.DateTimeField(blank=True, default=datetime.datetime.now)
    img     = models.ImageField(upload_to="img-tags")
    tags    = models.CharField(blank=True, max_length=100)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.hashtag)
        super(Follow_Shoutout_Like_Comment,self).save(*args,**kwargs)

    def __str__(self):
        return self.hashtag

class Travel_Active_Sports(models.Model):
    user    = models.ForeignKey(User , on_delete=models.CASCADE)
    hashtag = models.ForeignKey(Hashtags , on_delete=models.CASCADE)
    # title   = models.CharField(blank=True, max_length=100)
    slug    = models.SlugField(null=True,blank=True)
    content = models.TextField(blank=True)
    date    = models.DateTimeField(blank=True, default=datetime.datetime.now)
    img     = models.ImageField(upload_to="img-tags")
    tags    = models.CharField(blank=True, max_length=100)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.hashtag)
        super(Travel_Active_Sports,self).save(*args,**kwargs)

    def __str__(self):
        return self.hashtag

class Electronics(models.Model):
    user    = models.ForeignKey(User , on_delete=models.CASCADE)
    hashtag = models.ForeignKey(Hashtags , on_delete=models.CASCADE)
    # title   = models.CharField(blank=True, max_length=100)
    slug    = models.SlugField(null=True,blank=True)
    content = models.TextField(blank=True)
    date    = models.DateTimeField(blank=True, default=datetime.datetime.now)
    img     = models.ImageField(upload_to="img-tags")
    tags    = models.CharField(blank=True, max_length=100)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.hashtag)
        super(Electronics,self).save(*args,**kwargs)

    def __str__(self):
        return self.hashtag

class Textart(models.Model):
    user    = models.ForeignKey(User , on_delete=models.CASCADE)
    hashtag = models.ForeignKey(Hashtags , on_delete=models.CASCADE)
    # title   = models.CharField(blank=True, max_length=100)
    slug    = models.SlugField(null=True,blank=True)
    content = models.TextField(blank=True)
    date    = models.DateTimeField(blank=True, default=datetime.datetime.now)
    img     = models.ImageField(upload_to="img-tags")
    tags    = models.CharField(blank=True, max_length=100)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.hashtag)
        super(Textart,self).save(*args,**kwargs)

    def __str__(self):
        return self.hashtag

class Other(models.Model):
    user    = models.ForeignKey(User , on_delete=models.CASCADE)
    hashtag = models.ForeignKey(Hashtags , on_delete=models.CASCADE)
    # title   = models.CharField(blank=True, max_length=100)
    slug    = models.SlugField(null=True,blank=True)
    content = models.TextField(blank=True)
    date    = models.DateTimeField(blank=True, default=datetime.datetime.now)
    img     = models.ImageField(upload_to="img-tags")
    tags    = models.CharField(blank=True, max_length=100)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.hashtag)
        super(Other,self).save(*args,**kwargs)

    def __str__(self):
        return self.hashtag