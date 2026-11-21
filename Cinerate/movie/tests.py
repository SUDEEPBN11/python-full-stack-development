from unittest.mock import Mock, patch

from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory, SimpleTestCase

from .models import movie as Movie
from .views import movie_detail


class MovieDetailViewTests(SimpleTestCase):
    @patch('movie.views.render')
    @patch('movie.views.get_object_or_404')
    def test_movie_detail_looks_up_movie_model(self, get_object_or_404, render):
        movie_obj = Mock()
        movie_obj.id = 1
        movie_obj.rating.all.return_value = []
        get_object_or_404.return_value = movie_obj

        request = RequestFactory().get('/movie/1/')
        request.user = AnonymousUser()

        response = movie_detail(request, 1)

        get_object_or_404.assert_called_once_with(Movie, id=1)
        self.assertIs(response, render.return_value)
