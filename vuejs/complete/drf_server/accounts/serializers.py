from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
# models.py 말고는 User 모델 쓸 떄 get_user_model()
# DB -> JSON 
class UserSerializer(serializers.ModelSerializer): # ModelSerializer
    # JSON으로 비밀번호가 안나가도록 설정해주기
    password = serializers.CharField(write_only=True) # 입력은 받는데 보여주진 않는것 -> write_only
    # 오버 라이딩 -> 13번째줄 password가 필드가 만들어짐 바꿔치기 하는것
    class Meta:
        model = User # 어떤 DB랑 Serializer랑 연결할지 설정
        fields = ('username', 'password') 