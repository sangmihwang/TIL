from rest_framework import serializers
from .models import Article, Comment

# Form => forms.Form / forms.ModelForm
# serializers => Serializer / ModelSerializer
# Model 이 붙으면 => 정의한 필드에 대해서 입출력
# 안 붙으면 => 사용자가 원하는 필드를 추가로 입력받거나, 출력함

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        
# Serializer 사용
# 정의된 필드 외의 데이터를 사용자로부처 입력받고 싶을 때 사용
class ArticleListSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()
    # read_only: 사용자의 입력을 받지 않고, 출력만 하길 원할 때
    created_at = serializers.DateTimeField(read_only=True)
    # nothing = serializers.CharField()
    # write_only: 사용자의 입력만 받고, 출력을 하지 않길 원할 때
    # requires: 반드시 입력받아야하면 True
    # allow_blank: blank 허용
    # allow_null: null 허용
    myfield = serializers.CharField(write_only=True, required=False, allow_blank=True, allow_null=True)
    
    # BaseSerializer 의 create() 함수가 호출됨
    # serializers.Serializer 사용 시, create를 반드시 재정의해야 함
    def create(self, validated_data):
        print('validated_data =', validated_data)
        # myfield에 대한 계산
        validated_data['title'] += validated_data['myfield']
        return Article.objects.create(
            title=validated_data['title'],
            content=validated_data['content']
        )
        
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance