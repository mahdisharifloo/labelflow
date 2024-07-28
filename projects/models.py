from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

class Project(models.Model):
    title = models.CharField(max_length=300)
    ls_id = models.IntegerField(null=False)
    context = models.TextField(blank=True)
    project_type = models.TextField(blank=True)
    choices = models.TextField(blank=True)
    priority = models.IntegerField(default=1)
    is_done = models.BooleanField(default=False)
    image_logo_path = models.TextField(blank=True)
    image_banner_path = models.TextField(blank=True)
    created_by = models.ForeignKey(user,on_delete=models.CASCADE,related_name='projects')

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        db_table = "projects"