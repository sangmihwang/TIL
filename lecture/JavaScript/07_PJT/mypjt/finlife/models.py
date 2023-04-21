from django.db import models
from django.conf import settings

# Create your models here.
class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique = True)   # 금융상품코드
    kor_co_nm = models.TextField()      # 금융회사명
    fin_prdt_nm = models.TextField()    # 금융상품명
    etc_note = models.TextField()       # 금융상품설명
    join_deny = models.IntegerField()   # 가입 제한
    join_member = models.TextField()    # 가입 대상
    join_way = models.TextField()       # 가입 방법
    spcl_cnd = models.TextField()       # 우대 조건 
    
     
class DepositOptions(models.Model):
    fin_prdt_cd = models.ForeignKey(DepositProducts, on_delete=models.CASCADE, related_name='options')
    intr_rate_type_nm = models.CharField(max_length=100)    # 저축금리 유형명
    intr_rate = models.FloatField()     # 저축금리
    intr_rate2 = models.FloatField()    # 최고우대금리    
    save_trm = models.IntegerField()    # 저축기간(개월)
    
    
