from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

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
class Category(BaseModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class GravitySys(BaseModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class LateralSys(BaseModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Project(BaseModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='image/project')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    total_Area = models.FloatField(null=True, blank=True)
    gravity_loading_sys = models.ForeignKey(GravitySys, on_delete=models.SET_NULL, null=True, blank=True)
    lateral_loading_sys = models.ForeignKey(LateralSys, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("homePage:detail", kwargs={"id":self.id, "title": self.title})

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/project/')
    caption = models.CharField(max_length=200, blank=True, null=True)  # Optional

    def __str__(self):
        return f"Image for {self.project.title}"

class Coworking(BaseModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='image/coworking')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("homePage:detail", kwargs={"id":self.id, "title": self.title})
