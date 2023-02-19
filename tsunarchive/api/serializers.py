from rest_framework import serializers
from .models import Archive

class ArchiveSerializer(serializers.ModelSerializer):
    
    affiliation = serializers.CharField(required=False)
    image = serializers.ImageField(required=False)
    
    class Meta:
        model = Archive
        fields = ['id','name','gender', 'affiliation', 'hair_style', 'hair_color', 'Ttype', 'image']