from .models import CustomUser
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']

class RegistrationSerializer(serializers.ModelSerializer):
    # bio = serializers.CharField()
    # profile_picture = serializers.ImageField()
    # followers = serializers.ManyRelatedField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password',]
        extra_kwargs = {
            'password' : {'write_only': True}
        }
    
    def save(self):

        password = self.validated_data['password']
     
        if CustomUser.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'Email already exists!'})

        account = CustomUser(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()

        return account