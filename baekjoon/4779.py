def kanto(list_kanto):
    length = len(list_kanto)
    if length == 1:  # 길이가 1이면 끝
        return list_kanto
    start_kanto = kanto(list_kanto[0:int(1/3*length)])
    mid_kanto = [' ']*(int(1/3 * length))

    list_kanto = start_kanto + mid_kanto + start_kanto

    return list_kanto

while True:
    try:
        n = int(input())
        result_kanto = ['-'] * (3**n)
        answer = kanto(result_kanto)
        for i in answer:
            print(i, end='')
    except:
        break
