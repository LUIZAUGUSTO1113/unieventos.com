from django.db import models
from django.contrib.auth import get_user_model

# model reponsável pela criação de eventos, bem como linkar este ao seu criador
class Event(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images', blank=True)
    description = models.TextField()
    event_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # relaciona com o usuário criador
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('-created',)


# model responsável pela inscrição dos usuário em um evento
# NÃO DESENVOLVIDO - VISUALIZAR O READ.ME