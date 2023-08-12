import uuid
from django.db import models

from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    file_name = f'{uuid.uuid4()}.{ext}'
    return file_name


class Base(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    modify = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Service(Base):
    ICON_CHOICES = (
        ('lni-cog', 'Gear'),
        ('lni-stats-up', 'Graphic'),
        ('lni-users', 'Users'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Rocket'),
    )
    icon = models.CharField(max_length=12, choices=ICON_CHOICES)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self) -> str:
        return self.name
    

class JobPosition(Base):
    position = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Job Position'
        verbose_name_plural = 'Job Positions'

    def __str__(self) -> str:
        return self.position
    

class Employee(Base):
    name = models.CharField(max_length=100)
    position = models.ForeignKey('core.JobPosition', verbose_name='Position', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    image = StdImageField(upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField(max_length=100, default='#')
    twiter = models.CharField(max_length=100, default='#')
    instagram = models.CharField(max_length=100, default='#')

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Team'

    def __str__(self) -> str:
        return self.name
    

class Feature(Base):
    ICON_CHOICE = (
        ('lni-rocket','Rocket'),
        ('lni-laptop-phone', 'Laptop-Phone'),
        ('lni-cog', 'gear'),
        ('lni-leaf', 'Leaf'),
        ('lni-layers', 'Layers'),
    )

    icon = models.CharField(max_length=18, choices=ICON_CHOICE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

    def __str__(self) -> str:
        return self.name