from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Platform, Genre, Game, DevelopingCompany
from decimal import Decimal
from .forms import GameForm

import random

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
             username='testuser', email='test@example.com', password='Testpassword00!')
        self.client.login(username='testuser', password='Testpassword00!')
        self.platform = Platform.objects.create(name='Platform 1')
        self.genre = Genre.objects.create(name='Genre 1')
        self.developingCompany = DevelopingCompany.objects.create(name='Company 1')


        # self.client.login(username='testuser', password='testpassword')



    def test_add_game_view_get(self):
        response = self.client.get(reverse('addgame'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h1>Agregar juego</h1>')
        self.assertContains(response, '<form method="POST"')
        self.assertContains(response, '<input type="submit"')

    def test_add_game(self):
        oldGameObjectCount = Game.objects.count()        

        Game.objects.create(
            title = 'Game 1',
            platform = self.platform,
            genre = self.genre,
            developingCompany = self.developingCompany,
            rating = '9.5',
            user= self.user
        )
        

        newGameObjectCount = Game.objects.count()
        response = self.client.post(reverse('addgame'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(oldGameObjectCount+1, newGameObjectCount)
        game = Game.objects.last()
        self.assertEqual(game.title, 'Game 1')
        self.assertEqual(game.platform.id, self.platform.id)
        self.assertEqual(game.genre.id, self.genre.id)



        self.assertEqual(game.developingCompany.id, self.developingCompany.id)
        self.assertEqual(game.rating, 9.5)
        self.assertEqual(game.user, self.user)

    def test_add_some_games(self):
        totalGamesToCreate = 20
        oldGameObjectCount = Game.objects.count()
        for _ in range(totalGamesToCreate):
            newRating = round(random.uniform(0.0, 5.0), 1)
            newTitle = 'Game '+str(round(random.randint(1, 30), 1))

            Game.objects.create(
                title = newTitle,
                platform = self.platform,
                genre = self.genre,
                developingCompany = self.developingCompany,
                rating = str(newRating),
                user= self.user
            )
            game = Game.objects.last()
            self.assertEqual(game.title, newTitle)
            self.assertEqual(game.platform.id, self.platform.id)
            self.assertEqual(game.genre.id, self.genre.id)
            self.assertEqual(game.developingCompany.id, self.developingCompany.id)
            self.assertEqual(game.rating, round(Decimal(newRating), 1))
            self.assertEqual(game.user, self.user)

        newGameObjectCount = Game.objects.count()
        # response = self.client.post(reverse('addgame'))
        # self.assertEqual(response.status_code, 200)
        self.assertEqual(oldGameObjectCount+totalGamesToCreate, newGameObjectCount)




    def test_delete_some_games(self):
        totalGamesToDelete = 20
        for _ in range(totalGamesToDelete):
            newRating = round(random.uniform(0.0, 5.0), 1)
            newTitle = 'Game '+str(round(random.randint(1, 30), 1))

            Game.objects.create(
                title = newTitle,
                platform = self.platform,
                genre = self.genre,
                developingCompany = self.developingCompany,
                rating = str(newRating),
                user= self.user
            )
        oldGameObjectCount = Game.objects.count()
        for _ in range(totalGamesToDelete):
            game = Game.objects.last()
            Game.objects.last().delete()

        newGameObjectCount = Game.objects.count()
        self.assertEqual(oldGameObjectCount-totalGamesToDelete, newGameObjectCount)

    def test_delete_game(self):
        Game.objects.create(
            title = 'Game 1',
            platform = self.platform,
            genre = self.genre,
            developingCompany = self.developingCompany,
            rating = '9.5',
            user = self.user
        )
        game = Game.objects.last()
        oldGameObjectCount = Game.objects.count()
        Game.objects.last().delete()
        newGameObjectCount = Game.objects.count()
        self.assertEqual(oldGameObjectCount-1, newGameObjectCount)

    def test_add_game_post(self):

        clientRequestForm = Client(enforce_csrf_checks=True)
        clientRequestForm.login(username='testuser', password='Testpassword00!')

        oldGameObjectCount = Game.objects.count()

        response =self.client.post(reverse('addgame'), data={
            'title': ['Game 200'],
            'platform': [self.platform.id],
            'genre': [self.genre.id],
            'developingCompany': [self.developingCompany.id],
            'rating': [round(Decimal(4.0), 1)]
        })
        


        newGameObjectCount = Game.objects.count()
        # self.assertEqual(response.status_code, 200)
        self.assertEqual(oldGameObjectCount+1, newGameObjectCount)

        self.assertEqual(game.title, 'Game 200')
        self.assertEqual(game.platform.id, self.platform.id)
        self.assertEqual(game.genre.id, self.genre.id)
        self.assertEqual(game.developingCompany.id, self.developingCompany.id)
        self.assertEqual(game.rating, 4.0)
        # self.assertEqual(game.user, self.user)