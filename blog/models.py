from django.conf import settings
from django.db import models
from django.utils import timezone

# IMPORTANTE colocar o models.Model para o Django entender que é um modelo e ,consequentemente, deve ser salvo no BD
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # é um link para outro modelo
    title = models.CharField(max_length=200)    # para definir um texto com uma limitaçao de caracteres
    text = models.TextField()   # para textos sem limite de caracteres
    creation_date = models.DateTimeField(default=timezone.now)  # data e hora
    publication_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publication_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
