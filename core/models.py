from django.db import models

class Profile(models.Model):
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    
    tagline = models.CharField(max_length=250, blank=True, help_text="Short professional tagline")
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.full_name



class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    level = models.PositiveIntegerField(default=80, help_text="Skill proficiency percentage (0–100)")

    class Meta:
        ordering = ['-level']

    def __str__(self):
        return f"{self.name} ({self.level}%)"


class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='experiences')
    position = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    start_year = models.CharField(max_length=10)
    end_year = models.CharField(max_length=10, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-start_year']

    def __str__(self):
        return f"{self.position} at {self.company}"


class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='education')
    degree = models.CharField(max_length=150)
    institution = models.CharField(max_length=150)
    year = models.CharField(max_length=10)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-year']

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.client_name} - {self.role}"
    
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)  
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    cc_email = models.EmailField(blank=True, null=True, help_text="Optional CC email")  # optional CC

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"
