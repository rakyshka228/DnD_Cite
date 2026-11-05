import json
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from .forms import AnimeForm
from .models import Anime


def serialize_anime(anime):
    return {
        "id": anime.id,
        "title": anime.title,
        "author": anime.author,
        "year": anime.year,
        "status": anime.status,
        "rating": anime.rating,
        "rating_scale": anime.rating_scale,
        "description": anime.description,
        "tags": anime.tags,
        "cover_image": anime.cover_image.url if anime.cover_image else None,
        "cover_url": anime.cover_url,
    }


def parse_request_data(request):
    if request.content_type == "application/json":
        try:
            return json.loads(request.body.decode("utf-8") or "{}")
        except json.JSONDecodeError:
            return None
    return request.POST.dict()


def build_anime_form(request, instance=None):
    if request.content_type and "multipart/form-data" in request.content_type:
        return AnimeForm(request.POST, request.FILES, instance=instance)
    if request.content_type == "application/json":
        return AnimeForm(parse_request_data(request), instance=instance)
    return AnimeForm(request.POST, instance=instance)


def _user_anime_queryset(request):
    if request.user.is_authenticated:
        return Anime.objects.filter(user=request.user)
    return Anime.objects.all()


def anime_list(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])

    anime = _user_anime_queryset(request).order_by("id")
    data = [serialize_anime(item) for item in anime]
    return JsonResponse({"anime": data})


def anime_detail(request, pk):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])

    anime = get_object_or_404(_user_anime_queryset(request), pk=pk)
    return JsonResponse(serialize_anime(anime))


@login_required
def anime_page_list(request):
    anime = Anime.objects.filter(user=request.user)

    status = request.GET.get("status", "")
    rating_min = request.GET.get("rating_min", "")
    sort_by = request.GET.get("sort_by", "title")
    sort_dir = request.GET.get("sort_dir", "asc")

    if status:
        anime = anime.filter(status=status)
    if rating_min:
        anime = anime.filter(rating__gte=int(rating_min))

    if sort_by == "year":
        ordering = "year" if sort_dir == "asc" else "-year"
    else:
        ordering = "title" if sort_dir == "asc" else "-title"

    anime = anime.order_by(ordering)
    return render(
        request,
        "tasks/book_list.html",
        {
            "anime": anime,
            "status": status,
            "rating_min": rating_min,
            "sort_by": sort_by,
            "sort_dir": sort_dir,
        },
    )


@login_required
def anime_page_detail(request, pk):
    anime = get_object_or_404(Anime, pk=pk, user=request.user)
    return render(request, "tasks/book_detail.html", {"anime": anime})


@csrf_exempt
def anime_create(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    if request.content_type == "application/json":
        data = parse_request_data(request)
        if data is None:
            return HttpResponseBadRequest("Invalid JSON payload")
        form = AnimeForm(data)
    else:
        form = build_anime_form(request)

    if form.is_valid():
        anime = form.save(commit=False)
        if request.user.is_authenticated:
            anime.user = request.user
        anime.save()
        return JsonResponse(serialize_anime(anime), status=201)

    return JsonResponse({"errors": form.errors}, status=400)


@login_required
def anime_page_create(request):
    if request.method == "POST":
        form = build_anime_form(request)
        if form.is_valid():
            anime = form.save(commit=False)
            anime.user = request.user
            anime.save()
            return redirect("tasks:anime-page-list")
    else:
        form = AnimeForm()

    return render(request, "tasks/book_form.html", {"form": form, "title": "Добавить аниме"})


@login_required
def anime_page_update(request, pk):
    anime = get_object_or_404(Anime, pk=pk, user=request.user)
    if request.method == "POST":
        form = build_anime_form(request, instance=anime)
        if form.is_valid():
            form.save()
            return redirect("tasks:anime-page-detail", pk=anime.pk)
    else:
        form = AnimeForm(instance=anime)

    return render(request, "tasks/book_form.html", {"form": form, "title": "Редактировать аниме"})


@login_required
def anime_page_delete(request, pk):
    anime = get_object_or_404(Anime, pk=pk, user=request.user)
    if request.method == "POST":
        anime.delete()
        return redirect("tasks:anime-page-list")

    return render(request, "tasks/book_confirm_delete.html", {"anime": anime})


@csrf_exempt
def anime_update(request, pk):
    if request.method not in ("POST", "PUT", "PATCH"):
        return HttpResponseNotAllowed(["POST", "PUT", "PATCH"])

    if not request.user.is_authenticated:
        return JsonResponse({"detail": "Authentication required"}, status=401)

    anime = get_object_or_404(_user_anime_queryset(request), pk=pk)
    if request.content_type == "application/json":
        data = parse_request_data(request)
        if data is None:
            return HttpResponseBadRequest("Invalid JSON payload")
        form = AnimeForm(data, instance=anime)
    else:
        form = build_anime_form(request, instance=anime)
    if form.is_valid():
        anime = form.save()
        return JsonResponse(serialize_anime(anime))

    return JsonResponse({"errors": form.errors}, status=400)


@csrf_exempt
def anime_delete(request, pk):
    if request.method not in ("POST", "DELETE"):
        return HttpResponseNotAllowed(["POST", "DELETE"])

    if not request.user.is_authenticated:
        return JsonResponse({"detail": "Authentication required"}, status=401)

    anime = get_object_or_404(_user_anime_queryset(request), pk=pk)
    anime.delete()
    return JsonResponse({"deleted": pk})


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("tasks:anime-page-list")
    else:
        form = UserCreationForm()
    return render(request, "auth/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("tasks:anime-page-list")
    else:
        form = AuthenticationForm(request)
    return render(request, "auth/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("tasks:login")
