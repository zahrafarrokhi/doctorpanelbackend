from rest_framework import serializers

from doctor.models import Doctor, Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    department_name = serializers.CharField(source="department.name")
    class Meta:
        model = Doctor
        fields = '__all__'


# class DepartmentFullSerialzer(serializers.ModelSerializer):
#     doctor_set = DoctorSerializer(many=True)
#     class Meta:
#         model = Department
#         fields = '__all__'