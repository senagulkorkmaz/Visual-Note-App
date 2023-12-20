from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from visual_note.authentication import IsAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from to_do_list.serializers import To_Do_ListSerializer
from to_do_list.models import To_Do_List
from visual_note.pagination import LargePagination


class CreateView(APIView):
    authentication_classes = [IsAuthentication]

    def post(self, request):
        user = IsAuthentication.authenticate(self, request)
        request.data['user'] = user[0].pk

        serializer = To_Do_ListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListView(generics.ListAPIView):
    authentication_classes = [IsAuthentication]
    serializer_class = To_Do_ListSerializer
    model = To_Do_List
    queryset = model.objects.all()
    pagination_class = LargePagination

    def get_queryset(self):
        return To_Do_List.objects.filter(user=self.request.user).order_by('-id')


class UpdateView(APIView):
    authentication_classes = [IsAuthentication]

    def get_object(self, pk):
        to_do_instance = get_object_or_404(To_Do_List, pk=pk)
        return to_do_instance

    def put(self, request, pk):
        print("Gelen Data : ", request.data)
        user = IsAuthentication.authenticate(self, request)
        user = user[0].pk
        request.data['user_id'] = user
        note = self.get_object(pk=pk)
        note_user = note.user.id
        if str(note_user) == str(user):
            request.data['user'] = user
            serializer = To_Do_ListSerializer(note, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            error_message = _(
                'Bu Yapılacak Size Ait Değil.')
            return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)


class DeleteView(generics.DestroyAPIView):
    authentication_classes = [IsAuthentication]
    serializer_class = To_Do_ListSerializer
    model = To_Do_List
    queryset = model.objects.all()
    lookup_field = 'pk'

    def get_queryset(self):
        return To_Do_List.objects.filter(user=self.request.user)
