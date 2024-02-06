music = list(map(int, input().split()))

as_music = sorted(music)
desc_music = sorted(music, reverse=True)

if music==as_music:
    print("ascending")
elif music==desc_music:
    print("descending")
else:
    print("mixed")
