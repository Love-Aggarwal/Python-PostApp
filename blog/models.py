from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Author(models.Model):
    # name = models.CharField(max_length=50)
    # email = models.EmailField(unique=True,verbose_name="Author Email")
    # active = models.BooleanField(default=False)
    # created_on = models.DateTimeField(auto_now_add=True)
    # last_logged_in = models.DateTimeField(auto_now=True)
    #required to associate Author model with User model (Important)
    user = models.OneToOneField(User, null=True, blank=True,on_delete=models.CASCADE)

    # additional fields
    activation_key = models.CharField(max_length=255, default=1)
    email_validated = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    # def __str__(self):
    #     return self.name + " : " +self.email


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)  #this is one to many rel as one author has many Category

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('post_by_category', args=[self.slug])


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)  #this is one to many rel as one author has many Tags
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('post_by_tag', args=[self.slug])

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, 
                   help_text="Slug will be generated automatically from the title of the post")
    content = RichTextUploadingField()
    #content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE) #this is one to many rel as one author has many Popst
    category = models.ForeignKey(Category,on_delete=models.CASCADE)   # this is one to one rel as one cat has may Post
    tags = models.ManyToManyField(Tag) # this is many to many  rel as one post has many tags and one tags has many post
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
      return reverse('post_detail', args=[self.id, self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)



class Feedback(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the sender")
    email = models.EmailField(max_length=200, help_text="Email of the sender")
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Feedback"

    def __str__(self):
        return self.name + "-" +  self.email