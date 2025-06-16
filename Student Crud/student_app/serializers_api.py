from rest_framework import serializers
from .models import User, Student, Faculty, Mark, Subject
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    student_class = serializers.CharField(required=False)
    subjects = serializers.CharField(required=False)
    marks = serializers.ListField(child=serializers.DictField(), required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role', 'mobile_number', 'address', 'student_class', 'subjects', 'marks']

    def create(self, validated_data):
        student_class = validated_data.pop('student_class', '')
        subjects = validated_data.pop('subjects', '')
        marks_data = validated_data.pop('marks', [])

        user = User.objects.create_user(**validated_data)

        if user.role == 'student':
            student = Student.objects.create(user=user, student_class=student_class, subjects=subjects)

            for mark in marks_data:
                subject_id = mark.get('subject_id')
                obtained = mark.get('marks_obtained')

                try:
                    subject = Subject.objects.get(id=subject_id)
                    Mark.objects.create(student=student, subject=subject, marks_obtained=obtained)
                except Subject.DoesNotExist:
                    raise serializers.ValidationError(f"Subject with ID {subject_id} does not exist.")

        elif user.role == 'faculty':
            Faculty.objects.create(user=user, subjects=subjects)

        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class MarksSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.name', read_only=True)
    subject_name = serializers.CharField(source='subject.name', read_only=True)

    class Meta:
        model = Mark
        fields = ['id', 'student', 'subject', 'marks_obtained', 'student_name', 'subject_name']