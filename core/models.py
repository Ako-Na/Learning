from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Instructor(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    job = models.CharField(max_length=255, default=None, blank=True, null=True)
    description = models.CharField(max_length=1024, default=None, blank=True, null=True)
    photo = models.CharField(max_length=255, default=None, blank=True, null=True)
    rating = models.DecimalField(max_digits=32, decimal_places=2, default=0)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeFiled(auto_now=True)

class Student(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    photo = models.CharField(max_length=255, default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Category(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    photo = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Course(models.Model):
    class CourseStatus(models.TextChoices):
        DRAFT = 'DRAFT',
        PENDING = 'PENDING',
        PUBLISHED = 'PUBLISHED',
        BANNED = 'BANNED',
        DENIED = 'DENIED'

    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    instructor = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    category = models.OneToOneField(
        Category,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=1024)
    subtitle = models.TextField()
    description = models.TextField()
    thumbnail = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=CourseStatus.choices, default=CourseStatus.DRAFT)
    preview_url = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=32, decimal_places=2, default=0)
    created_at = models.DateTimeFiled(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)