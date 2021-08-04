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

    description = models.TextField(
        blank=True, null=True, default="Sinopse indisponível no momento"
    )
    season_year = models.DateField(verbose_name="Ano do lançamento", null=True)

    class Meta:
        abstract = True


class Anime(SerieBase):
    pass

    def __str__(self) -> str:
        return self.title.romanji
