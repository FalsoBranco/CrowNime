from django.db import models

# Create your models here.


class MediaTitle(models.Model):
    romanji = models.CharField(max_length=155)
    english = models.CharField(max_length=155, blank=True, null=True)
    native = models.CharField(max_length=155, blank=True, null=True)

    def __str__(self) -> str:
        return self.romanji


class SerieBase(models.Model):
    title = models.OneToOneField(
        MediaTitle, related_name="title", on_delete=models.CASCADE
    )

    class Meta:
        abstract = True


class Anime(SerieBase):
    pass
