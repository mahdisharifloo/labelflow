from rest_framework import serializers
from .models import Project
from django.contrib.auth import get_user_model
from utility.labelstudio import LabelStudioAPI

User = get_user_model()
ls = LabelStudioAPI()


class ProjectSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def validate_priority(self, priority):
        if priority > 10 or priority <0:
            raise serializers.ValidationError('priority is out of range')
        return priority

    def create(self,validated_data):
        if validated_data.get('project_type') == "image_classification":
            ls_creation_status = ls.create_image_classification_project(
                    title=validated_data.get('title'),
                    description=validated_data.get('context'),
                    choices=validated_data.get('choices').split('-'),
            )
        elif validated_data.get('project_type') == "text_classification":
            ls_creation_status = ls.create_image_classification_project(
                    title=validated_data.get('title'),
                    description=validated_data.get('context'),
                    choices=validated_data.get('choices').split('-')
            )
        else:
            raise Exception("Project Type Is Not Allowed")

        if ls_creation_status:
            new_project = Project.objects.create(**validated_data,ls_id=ls_creation_status['id'])
            return new_project
        else:
            raise Exception('Can Not Create This Project!')

    class Meta:
        model = Project
        exclude = ['ls_id']

class UserSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(read_only=True,many=True)
    class Meta:
        model = User
        fields = "__all__"

