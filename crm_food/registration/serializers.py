from rest_framework import serializers
from rest.models import Users, Roles
from django.contrib.auth import authenticate


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ['name']


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['name', 'surname', 'email', 'phone', 'password', 'role', 'date', 'username']
        extra_kwargs = {
            'password': {'write_only': True}
        }


# class UsersRegistrationSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
#     role = RolesSerializer(many=True)
#
#     class Meta:
#         model = Users
#         fields = ['name', 'surname', 'email', 'phone', 'password', 'password2', 'role', 'date']
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }
#
#     def create(self, validated_data):
#         new_roles = validated_data.pop('role')
#         password2 = validated_data('password2')
#         password = validated_data('password')
#
#         users = Users.objects.create(**validated_data)
#         if password != password2:
#             raise serializers.ValidationError('Passwords do not match')
#         users.set_password(password)
#
#         for new_role in new_roles:
#             Roles.objects.create(users=users, **new_role)
#
#             return users

    # def update(self, instance, validated_data):
    #
    #     # Passwords should not be handled with `setattr`, unlike other fields.
    #     # Django provides a function that handles hashing and
    #     # salting passwords. That means
    #     # we need to remove the password field from the
    #     # `validated_data` dictionary before iterating over it.
    #     password = validated_data.pop('password', None)
    #
    #     for (key, value) in validated_data.items():
    #         # For the keys remaining in `validated_data`, we will set them on
    #         # the current `User` instance one at a time.
    #         setattr(instance, key, value)
    #
    #     if password is not None:
    #         # `.set_password()`  handles all
    #         # of the security stuff that we shouldn't be concerned with.
    #         instance.set_password(password)
    #
    #     # After everything has been updated we must explicitly save
    #     # the model. It's worth pointing out that `.set_password()` does not
    #     # save the model.
    #     instance.save()
    #
    #     return instance
#
#
# class LoginSerializer(serializers.Serializer):
#     email = serializers.CharField(max_length=255)
#     username = serializers.CharField(max_length=255, read_only=True)
#     password = serializers.CharField(max_length=128, write_only=True)
#     token = serializers.CharField(max_length=255, read_only=True)
#
#     def validate(self, data):
#         # The `validate` method is where we make sure that the current
#         # instance of `LoginSerializer` has "valid". In the case of logging a
#         # user in, this means validating that they've provided an email
#         # and password and that this combination matches one of the users in
#         # our database.
#         username = data.get('username', None)
#         password = data.get('password', None)
#         email = data.get('email', None)
#         # Raise an exception if an
#         # email is not provided.
#         if email is None:
#             raise serializers.ValidationError(
#                 'An email address is required to log in.'
#             )
        #
        # if username is None:
        #     raise serializers.ValidationError(
        #         'A username is required to log in.'
        # #     )
        #
        # # Raise an exception if a
        # # password is not provided.
        # if password is None:
        #     raise serializers.ValidationError(
        #         'A password is required to log in.'
        #     )
        #
        # # The `authenticate` method is provided by Django and handles checking
        # # for a user that matches this email/password combination. Notice how
        # # we pass `email` as the `username` value since in our User
        # # model we set `USERNAME_FIELD` as `email`.
        # user = authenticate(username=username, password=password)
        #
        # # If no user was found matching this email/password combination then
        # # `authenticate` will return `None`. Raise an exception in this case.
        # if user is None:
        #     raise serializers.ValidationError(
        #         'A user with this email and password was not found.'
        #     )
        #
        # # Django provides a flag on our `User` model called `is_active`. The
        # # purpose of this flag is to tell us whether the user has been banned
        # # or deactivated. This will almost never be the case, but
        # # it is worth checking. Raise an exception in this case.
        # if not user.is_active:
        #     raise serializers.ValidationError(
        #         'This user has been deactivated.'
        #     )
        #
        # # The `validate` method should return a dictionary of validated data.
        # # This is the data that is passed to the `create` and `update` methods
        # # that we will see later on.
        # return {
        #     'email': user.email,
        #     'username': user.username,
        #     'token': user.token
        # }
