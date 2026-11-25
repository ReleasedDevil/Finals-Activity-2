# Generated for the Student model.
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("student_id", models.CharField(max_length=30, unique=True)),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("phone", models.CharField(blank=True, max_length=30)),
                ("birth_date", models.DateField(blank=True, null=True)),
                ("gender", models.CharField(blank=True, choices=[("Male", "Male"), ("Female", "Female"), ("Prefer not to say", "Prefer not to say")], max_length=30)),
                ("address", models.TextField(blank=True)),
                ("guardian_name", models.CharField(blank=True, max_length=200)),
                ("guardian_contact", models.CharField(blank=True, max_length=30)),
                ("course", models.CharField(blank=True, max_length=150)),
                ("year_level", models.CharField(blank=True, max_length=50)),
                ("section", models.CharField(blank=True, max_length=50)),
                ("previous_school", models.CharField(blank=True, max_length=200)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["last_name", "first_name"]},
        ),
    ]
