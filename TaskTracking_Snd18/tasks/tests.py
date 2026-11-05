from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from .models import Anime


class AnimeApiTests(TestCase):
    def test_create_anime_with_100_point_rating(self):
        url = reverse('tasks:anime-create')
        response = self.client.post(url, {
            'title': 'Dungeon Master Guide',
            'author': 'Wizards of the Coast',
            'year': 2024,
            'status': 'character',
            'rating_scale': 100,
            'rating': 95,
            'tags': 'fantasy, guide',
        })

        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertEqual(data['rating'], 95)
        self.assertEqual(data['rating_scale'], 100)
        self.assertEqual(data['tags'], 'fantasy, guide')

    def test_create_anime_with_uploaded_image(self):
        url = reverse('tasks:anime-create')
        image = SimpleUploadedFile('card.png', b'fake-image', content_type='image/png')
        response = self.client.post(url, {
            'title': 'Arcane Spell',
            'author': 'Mage',
            'year': 2025,
            'status': 'magic',
            'rating_scale': 10,
            'rating': 8,
            'tags': 'arcane, spell',
            'cover_image': image,
        })

        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertIn('cover_image', data)

    def test_create_anime(self):
        url = reverse('tasks:anime-create')
        response = self.client.post(url, {
            'title': 'Attack on Titan',
            'author': 'Hajime Isayama',
            'year': 2013,
            'status': 'card',
            'rating': 9,
        })

        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertEqual(data['title'], 'Attack on Titan')
        self.assertEqual(data['author'], 'Hajime Isayama')

    def test_anime_list_returns_anime(self):
        Anime.objects.create(
            title='Naruto',
            author='Masashi Kishimoto',
            year=2002,
            status='item',
            rating=10,
        )
        url = reverse('tasks:anime-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn('anime', response.json())
        self.assertEqual(len(response.json()['anime']), 1)

    def test_create_anime_with_invalid_data(self):
        url = reverse('tasks:anime-create')
        response = self.client.post(url, {
            'title': 'Example',
            'author': 'Author',
            'year': 2026,
        })

        self.assertEqual(response.status_code, 400)
