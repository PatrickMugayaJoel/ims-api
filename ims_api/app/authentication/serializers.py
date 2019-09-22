from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User, Company
from .validators import validate_company_name, validate_email,\
    validate_password


class BaseSignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[validate_email],
        max_length=255,
        required=True,
        error_messages={
            "required": "email is required",
            "blank": "email field can not be blank"
        })
    password = serializers.CharField(
        validators=[validate_password],
        write_only=True,
        required=True,
        error_messages={
            "required": "password field is required",
            "blank": "password field can not be blank",
        })   
    profile_pic = serializers.CharField(
        required=True
    )


class SignUpCompanySerializer(BaseSignUpSerializer):
    company_name = serializers.CharField(
        validators=[validate_company_name],
        max_length=255,
        min_length=3,
        required=True,
        error_messages={
            "required": "company name is required",
            "blank": "company name can not be blank",
            "min_length": "company name must be atleast 3 characters",
            "max_length": "company name cannot exceed 255 characters"
        })

    class Meta:
        model = Company
        fields = '__all__'


class CreateUserSerializer(BaseSignUpSerializer):
    first_name = serializers.CharField(
        required=True,
        error_messages={
            "required": "firstname is required",
            "blank": "firstname can not be blank"
        })
    last_name = serializers.CharField(
        required=True,
        error_messages={
            "required": "lastname is required",
            "blank": "lastname can not be blank"
        })
    
    class Meta:
        model = User
        fields = '__all__'


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
