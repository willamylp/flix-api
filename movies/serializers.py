from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie


class MovieModelSerializer(serializers.ModelSerializer):

    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)

        return None

    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError("A Data de Lançamento deve ser maior que 1990")
        return value
    
    def vlidade_resumo(self, value):
        if len(value) < 200:
            raise serializers.ValidationError("O Resumo não pode ser maior que 200 caracteres.")
        return value
    
