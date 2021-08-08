from django.db import models
from django.utils.translation import gettext_lazy as _


class MediaFormat(models.IntegerChoices):
    TV = 1, _("Tv")
    MOVIE = 2, _("Movie")
    OVA = 3, _("Ova")
    # <!-- Opcionais -->
    # TV_SHORT
    # MANGA
    # NOVEL
    # ONE_SHOT


class MediaStatus(models.IntegerChoices):
    FINISHED = 1, _("Finished")
    RELEASING = 2, _("Releasing")


class MediaSeason(models.IntegerChoices):
    WINTER = 1, _("Winter")  # Months December to February
    SPRING = 2, _("Spring")  # Months March to May
    SUMMER = 3, _("Summer")  # Months June to August
    FALL = 4, _("Fall")  # Months September to November
