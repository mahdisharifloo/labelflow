from django.db import models


class BlogCard(models.Model):
    title = models.CharField(max_length=300)
    context = models.TextField(blank=True)
    business_section = models.CharField(max_length=300)
    image_path = models.TextField(blank=True)
    
    def __str__(self) -> str:
        return f"{self.title}"
    
    class Meta:
        db_table = "blog_cards"