from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _  # noqa


class DayOfWeek(TextChoices):
    MONDAY = 'MONDAY', _("ПОНЕДЕЛЬНИК")
    TUESDAY = 'TUESDAY', _("ВТОРНИК")
    WEDNESDAY = 'WEDNESDAY', _("СРЕДА")
    THURSDAY = 'THURSDAY', _("ЧЕТВЕРГ")
    FRIDAY = 'FRIDAY', _("ПЯТНИЦА")
    SATURDAY = 'SATURDAY', _("СУББОТА")
    SUNDAY = 'SUNDAY', _("ВОСКРЕСЕНЬЕ")
