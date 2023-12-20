from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from visual_note.authentication import IsAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from folder.serializers import FolderSerializer
from folder.models import Folder
from visual_note.pagination import LargePagination
from note.models import Note
from note.serializers import NoteSerializer


class CreateView(APIView):
    authentication_classes = [IsAuthentication]

    def post(self, request):
        user = IsAuthentication.authenticate(self, request)
        request.data['user'] = user[0].pk

        serializer = FolderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListView(generics.ListAPIView):
    authentication_classes = [IsAuthentication]
    serializer_class = FolderSerializer
    model = Folder
    pagination_class = LargePagination

    def get_queryset(self):
        return Folder.objects.filter(user=self.request.user).order_by('-id')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        data = serializer.data
        for folder_data in data:
            folder_id = folder_data['id']
            notes = Note.objects.filter(folder__id=folder_id)
            note_serializer = NoteSerializer(notes, many=True)
            folder_data['notlar'] = note_serializer.data

        return Response(data, status=status.HTTP_200_OK)


class UpdateView(APIView):
    authentication_classes = [IsAuthentication]

    def get_object(self, pk):
        folder_instance = get_object_or_404(Folder, pk=pk)
        return folder_instance

    def put(self, request, pk):
        print("Gelen Data : ", request.data)
        user = IsAuthentication.authenticate(self, request)
        user = user[0].pk
        request.data['user_id'] = user
        folder = self.get_object(pk=pk)
        folder_user = folder.user.id
        if str(folder_user) == str(user):
            request.data['user'] = user
            serializer = FolderSerializer(folder, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            error_message = _(
                'Bu Dosya Size Ait Değil.')
            return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)


class DeleteView(generics.DestroyAPIView):
    authentication_classes = [IsAuthentication]
    serializer_class = FolderSerializer
    model = Folder
    queryset = model.objects.all()
    lookup_field = 'pk'

    def get_queryset(self):
        return Folder.objects.filter(user=self.request.user)
