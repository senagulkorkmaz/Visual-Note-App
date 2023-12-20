from rest_framework import serializers
from to_do_list.models import To_Do_List


class To_Do_ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = To_Do_List
        fields = '__all__'
