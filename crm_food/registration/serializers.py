from rest_framework import serializers
from rest.models import Users, Roles


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ['name']


class UsersRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    role = RolesSerializer(many=True)

    class Meta:
        model = Users
        fields = ['name', 'surname', 'email', 'phone', 'password', 'password2', 'role', 'date']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        new_roles = validated_data.pop('role')
        password2 = validated_data('password2')
        password = validated_data('password')

        users = Users.objects.create(**validated_data)
        if password != password2:
            raise serializers.ValidationError('Passwords do not match')
        users.set_password(password)

        for new_role in new_roles:
            Roles.objects.create(users=users, **new_role)

            return users



