from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from user.serializers import UserSerializer
from user.models import User
from visual_note.authentication import create_access_token, create_refresh_token
from django.contrib.auth.hashers import make_password
from visual_note.authentication import IsAuthentication
from rest_framework.generics import get_object_or_404


class RegisterAPIView(APIView):
    def post(self, request):
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


class UpdateAPIView(APIView):
    authentication_classes = [IsAuthentication]

    def get_object(self, pk):
        user_instance = get_object_or_404(User, pk=pk)
        return user_instance

    def put(self, request, *args, **kwargs):
        user = IsAuthentication.authenticate(self, request)
        print("User ---->>", user[0])
        pk = user[0].pk
        user_id = user[0].pk
        print("Gelen Data : ", request.data)

        if not request.data.get("password"):
            request.data['password'] = user[0].password
        else:
            request.data['password'] = make_password(request.data['password'])

        if not request.data.get("username"):
            request.data['username'] = user[0].username

        user = self.get_object(pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        error_dict = {}
        for field, errors in serializer.errors.items():
            error_dict[field] = str(errors[0])
        return Response({"message": error_dict}, status=status.HTTP_200_OK)
