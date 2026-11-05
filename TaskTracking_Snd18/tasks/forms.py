from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Anime


class AnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = [
            "title",
            "author",
            "year",
            "status",
            "rating_scale",
            "rating",
            "description",
            "tags",
            "cover_image",
        ]
        exclude = ["user"]
        labels = {
            "title": _("Название"),
            "author": _("Автор / создатель"),
            "year": _("Год выхода"),
            "status": _("Тип"),
            "rating_scale": _("Шкала оценки"),
            "rating": _("Оценка"),
            "description": _("Описание"),
            "tags": _("Теги (через запятую)"),
            "cover_image": _("Изображение"),
        }
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
            "tags": forms.TextInput(attrs={"placeholder": "fantasy, magic, rare"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        rating = cleaned_data.get("rating")
        rating_scale = cleaned_data.get("rating_scale")
        if rating is not None and rating_scale is not None and rating > rating_scale:
            raise forms.ValidationError(_("Рейтинг не может быть больше выбранной шкалы."))
        return cleaned_data

    def clean_rating(self):
        rating = self.cleaned_data.get("rating")
        if rating is None:
            return rating
        rating_scale = self.cleaned_data.get("rating_scale")
        if rating_scale and rating > rating_scale:
            raise forms.ValidationError(_("Рейтинг не может быть больше выбранной шкалы."))
        return rating
