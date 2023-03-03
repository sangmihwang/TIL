
## 13458_ 시험 감독

N = int(input())
stu = list(map(int, input().split()))   # 시험장 별 응시자 수
B, C = map(int, input().split())        # B 총감독관 감시 가능 /C 부감독관 감시 가능
cnt = 0                                       # 총감독관 1명/ 부감독관 여러명

# 총감독관 먼저 배치
for s in stu:
    cnt += 1
    if s > B:
        if (s - B) % C:
            cnt += ((s - B) // C + 1)       # 총감독관 감시 학생 제외하고 부감독관 감시
        else:
            cnt += (s - B) // C

print(cnt)
