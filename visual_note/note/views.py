from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from visual_note.authentication import IsAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from note.serializers import NoteSerializer
from note.models import Note
from visual_note.pagination import LargePagination


class CreateView(APIView):
    authentication_classes = [IsAuthentication]

    def post(self, request):
        user = IsAuthentication.authenticate(self, request)
        request.data['user'] = user[0].pk

        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListView(generics.ListAPIView):
    authentication_classes = [IsAuthentication]
    serializer_class = NoteSerializer
    model = Note
    pagination_class = LargePagination

    def get_queryset(self):
        folder = self.request.data.get("folder")
        user_notes = Note.objects.filter(user=self.request.user)

        if folder:
            return user_notes.filter(folder=folder).order_by('-id')
        else:
            return user_notes.filter(folder__isnull=True).order_by('-id')


class UpdateView(APIView):
    authentication_classes = [IsAuthentication]

    def get_object(self, pk):
        note_instance = get_object_or_404(Note, pk=pk)
        return note_instance

    def put(self, request, pk):
        print("Gelen Data : ", request.data)
        user = IsAuthentication.authenticate(self, request)
        user = user[0].pk
        request.data['user_id'] = user
        note = self.get_object(pk=pk)
        note_user = note.user.id
        if str(note_user) == str(user):
            request.data['user'] = user
            serializer = NoteSerializer(note, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            error_message = _(
                'Bu Dosya Size Ait Değil.')
            return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)


class DeleteView(generics.DestroyAPIView):
    authentication_classes = [IsAuthentication]
    serializer_class = NoteSerializer
    model = Note
    queryset = model.objects.all()
    lookup_field = 'pk'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)
