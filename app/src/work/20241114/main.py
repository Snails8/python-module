# 問題：数列の中から連続する部分列の最大和を求める
# 例：
# 入力: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# 出力: 6 （[4, -1, 2, 1]の合計）

def main(input: list[int]):
    """初回 O(n*2)
    memo:組み合わせ
    1. 開始位置から要素を足すだけ
    2. 開始位置はどこにでもなりうる
    3. 終了位置はどこでも良い
    """
    if input is None or len(input) == 0:
        ValueError("input is empty")
        return 0
    
    max_sum = float('-inf')
    for key, i in enumerate(input):
        row_total = i
        max_sum = max(max_sum, row_total)
        for l in range(key+1, len(input)):
            row_total += input[l]
            max_sum = max(max_sum, row_total)
    
    return max_sum

def kadane(input: list[int]):
    """2回目 kadane O(n)
    
    いわゆる損切り。
    1. 合計がマイナスの場合は、それまでの合計を捨てる
    2. プラスならそのまま続けてみる
    3. 最大値を記録しておく
    
    """
    if input is None or len(input) == 0:
        ValueError("input is empty")
        return 0
    
    current_sum = input[0]
    max_sum = input[0]
    
    for i in range(1, len(input)):
        current_sum = max(input[i], current_sum + input[i])
        max_sum = max(max_sum, current_sum)
    return max_sum


if __name__ == '__main__':
    input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    result = main(input)
    print("総当たり",result)
    
    result = kadane(input)
    print("kadane",result)