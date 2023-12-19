from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from user.serializers import UserSerializer
from user.models import User
from visual_note.authentication import create_access_token, create_refresh_token
from django.contrib.auth.hashers import make_password


class RegisterAPIView(APIView):
    def post(self, request):
        print("Gelen Data : ", request.data)
        request.data['username'] = "kullanici"

        user = User.objects.filter(email=request.data.get("email")).first()
        if not user == None:
            error_message = ('Bu Mail Adresine Ait Kullanıcı Bulunmaktadır.')
            return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user = User.objects.filter(id=serializer.data.get("id")).first()
        user.username = f'kullanici_{user.pk}'
        user.password = make_password(request.data['password'])
        user.save()

        return Response("OK")


class LoginAPIView(APIView):
    tokens = serializers.SerializerMethodField()

    def post(self, request):
        print("Gelen Dataya Bakk ---->>>> ", request.data)
        liste = User.objects.all()
        user = liste.filter(email=request.data['email']).first()
        if not user:
            error_message = (
                'Geçersiz Kimlik Bilgileri! (Bu Mail Adresi ile Hesabınız Bulunmamaktadır.)')
            return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)

        if not user.check_password(request.data['password']):
            error_message = (
                'Geçersiz Kimlik Bilgileri! (Şifre Bilginiz Yanlış.)')
            return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)

        access_token = create_access_token(user.id)
        refresh_secret = create_refresh_token(user.id)

        user.refresh_token = refresh_secret
        user.access_token = access_token
        user.save(update_fields=["refresh_token", "access_token"])

        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutAPIView(APIView):
    def post(self, request):
        print("Gelen Data : ", request.data)
        user = User.objects.filter(
            refresh_token=request.data['refresh_token']).first()
        if not user:
            error_message = (
                'Refresf Token Yanlış ya da Yok! (Daha önce çıkış yapılmış olabilir.)')
            return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)
        else:
            response = Response()
            response.data = {
                'message': ('Çıkış İşlemi Başarılı')
            }
            return response
