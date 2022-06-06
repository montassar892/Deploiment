from rest_framework import serializers
from .models import Candidat


class CandidatSerilaizer(serializers.ModelSerializer):
    class Meta():
        model = Candidat
        fields = ['name','lastname','email','phonenum','dateofbirth','cv']

