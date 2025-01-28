from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class BaseModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)

class BaseModel(models.Model):
    deleted = models.BooleanField(default=False, editable=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    objects = BaseModelManager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.deleted = True
        self.save()

# Create your models here.
class HomeCategory(BaseModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class HomeProject(BaseModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=False, null=True, blank=True)
    content = RichTextField()
    illustration = models.TextField(null=True, blank=True)
    characteristic = models.TextField(null=True, blank=True)
    employer_opinion = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='image/project')
    category = models.ForeignKey(HomeCategory, on_delete=models.SET_NULL, null=True, blank=True)
    total_Area = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("Structure_Design:detail", kwargs={"id": self.id, "title": self.slug})

class HomeProjectImage(models.Model):
    project = models.ForeignKey(HomeProject, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')
    caption = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.project.title}"

class HomeCoworking(BaseModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=False, null=True, blank=True)
    content = RichTextField()
    illustration = models.TextField(null=True, blank=True)
    characteristic = models.TextField(null=True, blank=True)
    coworker_opinion = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='image/coworking')
    category = models.ForeignKey(HomeCategory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("Structure_Design:coworking_detail", kwargs={"id": self.id, "title": self.slug})

class HomeCoworkingImage(models.Model):
    coworking = models.ForeignKey(HomeCoworking, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='coworking_images/')
    caption = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.coworking.title}"

class SiteDetailModel(models.Model):
    title = models.CharField(max_length=10000)
    logo = models.ImageField(upload_to='site_detail/image')
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    address = models.TextField()
    work_time = models.TextField()
    empty_cart_image = models.ImageField(upload_to='site_detail/image')
    footer_title = models.CharField(max_length=1000)
    footer_text = models.TextField()
    about_us_text = models.TextField()
    copy_right = models.TextField()
    enamad_image = models.ImageField(upload_to='site_detail/image', null=True, blank=True)
    enamad_url = models.URLField(null=True, blank=True)
    kasbokar_image = models.ImageField(upload_to='site_detail/image', null=True, blank=True)
    kasbokar_url = models.URLField(null=True, blank=True)
    samandehi_image = models.ImageField(upload_to='site_detail/image', null=True, blank=True)
    samandehi_url = models.URLField(null=True, blank=True)
    limit_of_address_can_add = models.IntegerField()
    suggested_products_image = models.ImageField(upload_to='site_detail/image', null=True, blank=True)
    amazing_products_image = models.ImageField(upload_to='site_detail/image', null=True, blank=True)
    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    whatsapp = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    telegram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)