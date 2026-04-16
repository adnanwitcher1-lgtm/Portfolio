from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    tech_stack = models.CharField(max_length=500, help_text="Comma separated: Django, PostgreSQL, Stripe")
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    def get_tech_list(self):
        return [tech.strip() for tech in self.tech_stack.split(',')]
    
    class Meta:
        ordering = ['-created_at']