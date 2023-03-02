from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import Language


User = get_user_model() # table of user

class Audio(models.Model):
    """
            class des videos et sons
    """
    number=models.CharField(max_length=250)
    language=models.ForeignKey(Language, related_name="music", on_delete=models.DO_NOTHING)
    creation_date = models.DateTimeField(auto_now_add=True)
    annotation = models.ManyToManyField(User, through="Annotation")

    class Meta:
        ordering = ['-creation_date', 'number', 'language']
    
    def __str__(self) -> str:
        return  self.number


class Emotion(models.Model):
    """
        emotions list
    """
    name = models.CharField(max_length=250)
    emoji=models.CharField(max_length=250)
    creation_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-creation_date", "name"]
        
    def __str__(self) -> str:
        return self.name


class Annotation(models.Model):
    """
            user annotation
    """
    emotion=models.ForeignKey(Emotion,on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="annotations", on_delete=models.DO_NOTHING)
    audio = models.ForeignKey(Audio, related_name="annotations", on_delete=models.CASCADE)

    class Meta:
        ordering = ['-creation_date']
    
    def __str__(self) -> str:
        return f'{self.emotion.name}'