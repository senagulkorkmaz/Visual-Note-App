from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from visual_note.authentication import IsAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from visual_note.pagination import LargePagination
from diary.serializers import DiarySerializer
from diary.models import Diary


class CreateView(APIView):
    authentication_classes = [IsAuthentication]

    def post(self, request):
        user = IsAuthentication.authenticate(self, request)
        request.data['user'] = user[0].pk

        serializer = DiarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListView(generics.ListAPIView):
    authentication_classes = [IsAuthentication]
    serializer_class = DiarySerializer
    model = Diary
    queryset = model.objects.all()
    pagination_class = LargePagination

    def get_queryset(self):
        return Diary.objects.filter(user=self.request.user).order_by('-id')


class UpdateView(APIView):
    authentication_classes = [IsAuthentication]

    def get_object(self, pk):
        diary_instance = get_object_or_404(Diary, pk=pk)
        return diary_instance

    def put(self, request, pk):
        user = IsAuthentication.authenticate(self, request)
        user = user[0].pk
        request.data['user_id'] = user
        diary = self.get_object(pk=pk)
        diary_user = diary.user.id
        if str(diary_user) == str(user):
            request.data['user'] = user
            serializer = DiarySerializer(diary, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            error_message = _(
                'Bu Günlük Size Ait Değil.')
            return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)


class DeleteView(generics.DestroyAPIView):
    authentication_classes = [IsAuthentication]
    serializer_class = DiarySerializer
    model = Diary
    queryset = model.objects.all()
    lookup_field = 'pk'

    def get_queryset(self):
        return Diary.objects.filter(user=self.request.user)
