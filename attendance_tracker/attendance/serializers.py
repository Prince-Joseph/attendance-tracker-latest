from rest_framework import serializers
from .models import Student


class ClasswiseStudentSerializer(serializers.ModelSerializer):
    # new_field_name_for_JSON = --------(source='orginal_field_name_in_model')
    rollNumber = serializers.CharField(source='roll_number')
    
    class Meta:
        model= Student
        fields = ('rollNumber',)