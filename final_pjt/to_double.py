# 텍스트 파일 경로
text_file_path = 'movie_list.txt'

# 수정된 텍스트를 저장할 파일 경로
output_file_path = 'movie_list.txt'

# 텍스트 파일 열기 (cp949 인코딩으로)
with open(text_file_path, 'r', encoding='utf-8', errors='replace') as file:
    text_data = file.read()

# 작은따옴표를 큰따옴표로 바꾸기
modified_text = text_data.replace("{", "")

# 수정된 텍스트 파일 저장
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(modified_text)

print("작은따옴표를 큰따옴표로 바꾼 텍스트 파일이 성공적으로 저장되었습니다.")