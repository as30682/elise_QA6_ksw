# 100에서 1까지 숫자를 출력. 단, 369 게임처럼 3, 6, 9 을 포함하고 있는 경우, 갯수만큼 “짝” 을 출력. (33일경우 “짝짝”)


for n in range(100, 0, -1):
    count = 0
    for c in str(n):
        if c in "369":
            count += 1
    if count > 0:
        print("짝" * count)
    else:
        print(n)
