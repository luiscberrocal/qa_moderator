from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient


class JWTTestMixin(object):

    def __init__(self, *args, **kwargs):
        super(JWTTestMixin, self).__init__(*args, **kwargs)
        self.jwt_api_client = APIClient()
        self.activated = False

    def get_access_token(self, user, **kwargs):

        obtain_token_url_name = kwargs.get('obtain_token_url_name', 'token_obtain_pair')
        token_url = reverse(obtain_token_url_name)
        password = kwargs.get('password', 'password')

        pay_load = {'username': user.username, 'password': password}
        token_response = self.jwt_api_client.post(token_url, data=pay_load)
        access_token = token_response.data.get('access')
        return access_token

    def set_credentials(self, token_or_user, **kwargs):
        if self.activated:
            if isinstance(token_or_user, str):
                access_token = token_or_user
            elif isinstance(token_or_user, get_user_model()):
                access_token = self.get_access_token(token_or_user, **kwargs)

            self.jwt_api_client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(access_token))

    def get_with_token(self, url, token_or_user, **kwargs):
        self.set_credentials(token_or_user)
        if kwargs.get('data'):
            response = self.jwt_api_client.get(url, data=kwargs.get('data'))
        else:
            response = self.jwt_api_client.get(url)
        return response

    def delete_with_token(self, url, token_or_user):
        self.set_credentials(token_or_user)
        response = self.jwt_api_client.delete(url, data={'format': 'json'})
        return response

    def put_with_token(self, url, token_or_user, data):
        self.set_credentials(token_or_user)
        response = self.jwt_api_client.put(url, data=data)
        return response

    def post_with_token(self, url, token_or_user, data):
        self.set_credentials(token_or_user)
        response = self.jwt_api_client.post(url, data=data)
        return response
