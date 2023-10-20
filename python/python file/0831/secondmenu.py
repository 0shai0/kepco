menu = {
    "김밥": ["원조김밥", "소고기김밥", "돈까스김밥"],
    "분식": ["오뎅", "잔치국수", "라볶이"],
    "식사": ["제육덮밥", "오므라이스", "된장찌개"],
    "국밥": ["콩나물국밥", "갈비탕", "육개장"]
}

max_items = max(len(items) for items in menu.values())
separator = " ㅡ "  # 구분자 설정

# 표 헤더 출력
header = separator.join(["ㅡ" * (max_items + 2)] * (len(menu) * 2 - 1))
print(header)

# 카테고리 출력
category_row = []
for key in menu.keys():
    category_row.append("|{:^{width}}|".format(key, width=max_items))
print("".join(category_row))
print(header)

# 메뉴 출력
for i in range(max_items):
    row = []
    for items in menu.values():
        if i < len(items):
            row.append("|{:^{width}}|".format(items[i], width=max_items))            
        else:
            row.append("|{:^{width}}|".format("", width=max_items))
    print("".join(row))
    print(header)
