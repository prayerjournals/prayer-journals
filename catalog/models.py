from django.db import models

# Create your models here.

from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


def get_image_filename(instance, filename):
    title = instance.title
    slug = slugify(title)
    return "note_images/%s-%s" % (slug, filename) 

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    title = models.CharField(max_length=128)
    body = models.TextField(max_length=4000)
    date = models.DateField(auto_now_add=True)
    image1 = models.ImageField(upload_to='note_images', verbose_name='Image 1')

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('view-note', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title

    class Meta:
        permissions = (("can_view_all_notes", "Can View All Notes"),)
    
    



    
    
    