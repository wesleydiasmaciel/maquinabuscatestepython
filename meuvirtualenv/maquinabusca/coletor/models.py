from django.db import models
from django.utils import timezone

# Create your models here.

class Pagina(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    url = models.CharField(max_length=1024)
    texto = models.TextField()
    data_coleta = models.DateTimeField(default=timezone.now)
    data_armazenamento = models.DateTimeField(blank=True, null=True)

    def armazenar(self):
        self.data_armazenamento = timezone.now()
        self.save()

    def __str__(self):
        return self.url
