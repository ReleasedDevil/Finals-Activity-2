from django.db import models

class Student(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Prefer not to say", "Prefer not to say"),
    ]

    student_id = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES, blank=True)
    address = models.TextField(blank=True)
    guardian_name = models.CharField(max_length=200, blank=True)
    guardian_contact = models.CharField(max_length=30, blank=True)
    course = models.CharField(max_length=150, blank=True)
    year_level = models.CharField(max_length=50, blank=True)
    section = models.CharField(max_length=50, blank=True)
    previous_school = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.last_name}, {self.first_name} ({self.student_id})"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
