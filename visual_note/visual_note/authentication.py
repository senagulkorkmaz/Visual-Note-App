from rest_framework.exceptions import AuthenticationFailed
import jwt
import datetime
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework import exceptions
from django.utils.translation import gettext_lazy as _
from user.models import User


class IsAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # print(request.headers)
        auth = get_authorization_header(request).split()

        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token)

            user = User.objects.get(pk=id)

            return (user, None)
        raise exceptions.AuthenticationFailed(_('Kimliği Doğrulanmamış'))


# access_token
def create_access_token(id):
    return jwt.encode({
        'user_id': id,
        # 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=300),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(weeks=52),
        'iat': datetime.datetime.utcnow()
    }, 'access_secret', algorithm='HS256')


def decode_access_token(token):
    if User.objects.filter(access_token=token).exclude():
        pass
    else:
        raise exceptions.AuthenticationFailed(_('Kimliği Doğrulanmamış'))
    try:
        payload = jwt.decode(token, 'access_secret', algorithms='HS256')
        return payload['user_id']

    except:
        raise exceptions.AuthenticationFailed(_('Kimliği Doğrulanmamış'))


# refresh_token
def create_refresh_token(id):
    return jwt.encode({
        'user_id': id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'iat': datetime.datetime.utcnow()
    }, 'refresh_secret', algorithm='HS256')


def decode_refresh_token(token):
    if not token:
        raise AuthenticationFailed(_('Kimliği Doğrulanmamış'))

    try:
        # Burada tablodan tokenı alıp, geçerli tokenla karşılaştırabilirsiniz
        # Tablodan tokenı almak için bir işlev
        if User.objects.filter(refresh_token=token).exclude():
            pass
        else:
            raise AuthenticationFailed(_('Kimliği Doğrulanmamış'))

        # Token doğrulama işlemi
        payload = jwt.decode(token, 'refresh_secret', algorithms='HS256')
        return payload['user_id']

    except jwt.ExpiredSignatureError:
        # Token süresi dolmuşsa buraya düşer
        raise AuthenticationFailed(_('Kimliği Doğrulanmamış'))

    except jwt.InvalidTokenError:
        # Geçersiz bir token olduğunda buraya düşer
        raise AuthenticationFailed(_('Kimliği Doğrulanmamış'))
