from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password',)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data.get('password'))
        user.is_active = True
        user.save()
        return user

    def update(self, user, validated_data):
        user = super().update(user, validated_data)
        password = validated_data.get('password')
        if password:
            user.set_password(password)
            user.save()
        return user
