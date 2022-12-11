from rest_framework import serializers
from .models import Contact,Positions

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model=Contact
        fields = ('id','first_name','last_name','company','email','phone','interested_in','estimated_budget','project_timeline','about_us','description')


class PositionsSerializer(serializers.ModelSerializer):

    class Meta:
        model=Positions
        fields =('id','name','email','phone','portfolio_url')

