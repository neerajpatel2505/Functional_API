from api.models import Movie 
from rest_framework import serializers

# class MovieSerializer(serializers.Serializer): 
#     id = serializers.IntegerField(read_only=True) 
#     name = serializers.CharField(max_length=200)
#     description = serializers.CharField(max_length=200) 
#     active = serializers.BooleanField(default=True)
    
#     def create(self,validated_data): 
#         return Movie.objects.create(**validated_data) 
    
#     def update(self, instence, validated_data): 
#         instence.name = validated_data.get('name',instence.name) 
#         instence.description = validated_data.get('description',instence.description) 
#         instence.active = validated_data.get('active',instence.active) 
#         instence.save() 
#         return instence
    
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'