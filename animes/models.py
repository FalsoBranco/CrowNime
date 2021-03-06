from django.db import models

from .choices import MediaFormat, MediaSeason, MediaStatus

# Create your models here.


class MediaTitle(models.Model):
    romanji = models.CharField(max_length=155)
    english = models.CharField(max_length=155, blank=True, null=True)
    native = models.CharField(max_length=155, blank=True, null=True)

    def __str__(self) -> str:
        return self.romanji


class Genre(models.Model):
    name = models.CharField(max_length=25, verbose_name="Nome do Gênero")

    def __str__(self) -> str:
        return self.name


class SerieBase(models.Model):
    title = models.OneToOneField(
        MediaTitle,
        related_name="serie",
        on_delete=models.CASCADE,
    )
    description = models.TextField(
        blank=True,
        null=True,
        default="Sinopse indisponível no momento",
    )
    season_year = models.DateField(
        verbose_name="Ano do lançamento",
        null=True,
    )
    genre = models.ManyToManyField(
        "animes.Genre",
        verbose_name="Generos",
        related_name="serie",
    )
    format = models.IntegerField(
        choices=MediaFormat.choices,
        null=True,
    )
    status = models.IntegerField(
        choices=MediaStatus.choices,
        null=True,
    )
    season = models.IntegerField(
        choices=MediaSeason.choices,
        null=True,
    )
    image = models.ImageField(
        upload_to="animes",
        null=True,
    )

    class Meta:
        abstract = True


class Anime(SerieBase):
    pass

    def __str__(self) -> str:
        return self.title.romanji
