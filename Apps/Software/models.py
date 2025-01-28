from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.urls import reverse

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
class SoftCategory(BaseModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class SoftVersion(BaseModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class SoftFee(BaseModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class SoftProject(BaseModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=False, null=True, blank=True)
    content = RichTextField()
    illustration = models.TextField(null=True, blank=True)
    characteristic = models.TextField(null=True, blank=True)
    employer_opinion = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='image/project')
    category = models.ForeignKey(SoftCategory, on_delete=models.SET_NULL, null=True, blank=True)
    total_Area = models.FloatField(null=True, blank=True)
    gravity_loading_sys = models.ForeignKey(SoftVersion, on_delete=models.SET_NULL, null=True, blank=True)
    lateral_loading_sys = models.ForeignKey(SoftFee, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("Software:detail", kwargs={"id": self.id, "title": self.slug})

    def get_absolute_url(self):
        return reverse('Software:project_detail', args=[self.id])

class SoftProjectImage(models.Model):
    project = models.ForeignKey(SoftProject, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')
    caption = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.project.title}"

class SoftCoworking(BaseModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=False, null=True, blank=True)
    content = RichTextField()
    illustration = models.TextField(null=True, blank=True)
    characteristic = models.TextField(null=True, blank=True)
    coworker_opinion = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='image/coworking')
    category = models.ForeignKey(SoftCategory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("Structure_Design:coworking_detail", kwargs={"id": self.id, "title": self.slug})

class SoftCoworkingImage(models.Model):
    coworking = models.ForeignKey(SoftCoworking, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='coworking_images/')
    caption = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.coworking.title}"