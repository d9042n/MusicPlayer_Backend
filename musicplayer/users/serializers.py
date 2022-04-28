from rest_framework import serializers

from .models import Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username', 'email', 'password', 'fullname', 'birthdate', 'country', 'user_id', 'is_online',
                  'refresh_token']
        extra_kwargs = {
            'password': {
                'write_only': True
            },
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = Users.objects.create(**validated_data)
        instance.is_active = True

        if password is not None:
            instance.set_password(password)
            instance.save()

        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password is not None:
            instance.set_password(password)

        instance.is_online = validated_data.get("is_online", instance.is_online)
        instance.refresh_token = validated_data.get("refresh_token", instance.refresh_token)

        instance.save()

        return instance


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username', 'email', 'fullname', 'birthdate', 'country', 'user_id', ]
        extra_kwargs = {
            'password': {
                "required": False,
                "write_only": True
            },
            'username': {
                "required": False,
            },
            'email': {
                "required": False,
            }
        }

    def update(self, instance, validated_data):
        instance.fullname = validated_data.get('fullname', instance.fullname)
        instance.birthdate = validated_data.get('birthdate', instance.birthdate)
        instance.country = validated_data.get('country', instance.country)
        instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)

        instance.save()

        return instance
