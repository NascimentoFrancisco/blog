from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Posts(models.Model):
    title = models.CharField(
        "Titulo", max_length=255, null=False, blank=False
    )
    image = models.ImageField(
        "Imagem", upload_to="images/blog/", null=True, blank=True
    )
    content = HTMLField("Conteúdo", null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title}"
    
    class Meta:
        ordering = ["created_at"]
        verbose_name = "post"
        verbose_name_plural = "posts"
