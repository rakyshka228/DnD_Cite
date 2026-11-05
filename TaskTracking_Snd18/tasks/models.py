from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _


class Anime(models.Model):
    STATUS_CHOICES = [
        ("card", _("Карта")),
        ("item", _("Предмет")),
        ("character", _("Персонаж")),
        ("magic", _("Магия")),
    ]

    title = models.CharField(max_length=256, verbose_name=_("Название"))
    author = models.CharField(max_length=256, verbose_name=_("Автор / создатель"))
    year = models.PositiveIntegerField(null=True, blank=True, verbose_name=_("Год выхода"))
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="card", verbose_name=_("Тип"))

    RATING_SCALE_CHOICES = [
        (5, "5"),
        (10, "10"),
        (100, "100"),
    ]
    rating_scale = models.PositiveSmallIntegerField(
        choices=RATING_SCALE_CHOICES,
        default=10,
        blank=True,
        null=True,
        verbose_name=_("Система рейтинга"),
    )
    rating = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        verbose_name=_("Рейтинг"),
    )
    description = models.TextField(blank=True, verbose_name=_("Описание"))
    tags = models.CharField(max_length=500, blank=True, verbose_name=_("Теги"))
    cover_image = models.FileField(upload_to="covers/", blank=True, null=True, verbose_name=_("Изображение"))
    cover_url = models.URLField(blank=True, verbose_name=_("Ссылка на изображение"))
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="animes",
        verbose_name=_("Владелец"),
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("Карта")
        verbose_name_plural = _("Карт")
        db_table = 'tasks_book'

    def __str__(self):
        return f"{self.title} by {self.author}"
