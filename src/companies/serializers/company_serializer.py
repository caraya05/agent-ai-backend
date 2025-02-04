from loducode_utils.serializers import AuditSerializer, CitySerializer
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from easy_thumbnails.files import get_thumbnailer

from companies.models.company import Company



class CompanySerializer(AuditSerializer):


    class Meta:
        model = Company
        fields = (
            "id",
            "username",
            "name_company",
            "email",
            "person_in_charge",
            "phone",
            "address",
            "nit", "city",
            "company_type",
            "image",
            "sector",
            "activity_economic",
            "email",
            "is_staff",
            "permission",
            "access",
            "company_principal",
        )


class CompanyCreateSerializer(AuditSerializer):
    password = serializers.CharField(max_length=128, write_only=True,
                                     required=False)

    class Meta:
        model = Company
        fields = (
            "id", "username", "name_company", "email", "person_in_charge",
            "phone", "address",
            "nit", "city", "company_type", "image", "sector",
            "activity_economic", "password", "email",

        )

        extra_kwargs = {
            'password': {'write_only': True},
            # 'id': {'read_only': True}
        }

    def create(self, validated_data):
        user = Company.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        super().update(instance, validated_data)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
            instance.save()
        return instance


class CompanyListSerializer(AuditSerializer):
    image = SerializerMethodField(read_only=True)

    class Meta:
        model = Company
        fields = (
            "id", "username", "name_company", "person_in_charge", "image",
        )

    def get_image(self, instance):  # pylint: disable=R0201
        if instance.image:
            thumb_url = get_thumbnailer(instance.image)['avatar'].url
            return thumb_url
        return ''


class CompanyUserSerializer(AuditSerializer):
    class Meta:
        model = Company
        fields = (
            "id", "username", "name_company", "person_in_charge",
        )
