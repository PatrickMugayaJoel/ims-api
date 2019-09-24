from django.contrib.auth import authenticate

from rest_framework import serializers

from .models import User
§
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)


    def validate(self, data):
        # The `validate` method makes sure current instance of `LoginSerializer` has "valid"
        # user in, this means validating that they've provided an email
        # and password and that this combination matches one of the users in our database.
        email = data.get('email', None)
        password = data.get('password', None)

        # Raise an exception if an email is not provided.
        if email is None:
            raise serializers.ValidationError(
                'An email address is required for sign up in.'
            )

        # Raise an exception if a password is not provided.
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        # The `authenticate` method is provided by Django and handles checking
        # for a user that matches this email/password combination. Notice how
        # we pass `email` as the `username` value. Remember that, in our User
        # model, we set `USERNAME_FIELD` as `email`.
        user = authenticate(username=email, password=password)

        # Raise an exception in case If no user was found matching this email/password combination then return None
        if user is None:
            raise serializers.ValidationError(
                'No user with this email and password.'
            )

        # Django provides a flag on our `User` model called `is_active`. The
        # purpose of this flag to tell us whether the user has been banned
        # or otherwise deactivated. This will almost never be the case, but
        # it is worth checking for. Raise an exception in this case.
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        # The `validate` method should return a dictionary of validated data.
        # This is the data that is passed to the `create` and `update` methods
        # that we will see later on.
        return {
            'email': user.email,
            'username': user.username,

        }
