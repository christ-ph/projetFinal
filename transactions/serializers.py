from rest_framework import serializers
from .models import Vente,Commande


class VenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vente
        fields = "__all__"

class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = "__all__"
