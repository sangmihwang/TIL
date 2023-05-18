import json

# 텍스트 파일 경로
text_file_path = 'movie_list.txt'

# JSON 파일 경로
json_file_path = 'movie_list.json'

# 텍스트 파일 열기
with open(text_file_path, 'r', encoding='utf-8', errors='replace') as file:
    text_data = file.read()

# 텍스트 데이터를 JSON으로 변환
json_data = json.loads(text_data)

# JSON 파일로 저장
with open(json_file_path, 'w') as file:
    json.dump(json_data, file, indent=4)

print("텍스트 파일이 성공적으로 JSON 파일로 변환되었습니다.")
