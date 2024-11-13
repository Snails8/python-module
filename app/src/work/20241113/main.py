##########################################
# ランレングス
##########################################

input = "aaabbbcc"
# output = "a3b3c2"


def encode(input):
    if not input:
        return ""

    result = ""  # result
    counter = 1  # 同一個数を記憶
    current = ""  # 文字を記憶
    for i, s in enumerate(input):
        # 初回
        if i == 0:
            current = s
            counter = 1
            continue
        # 最後(同じケースと、違うケース)
        if i == len(input) - 1:
            if current == s:
                result += current + str(counter + 1)
            else:
                result += current + str(counter) + s + "1"
            break

        # 途中
        if current == s:
            counter += 1
        else:
            result += current + str(counter)
            current = s
            counter = 1

    return result


def decode(input):
    if not input:
        return ""

    if len(input) % 2 != 0:
        return ""
    
    result = ""
    for i in  range(0, len(input), 2):
        current = input[i]
        num = int(input[i+1])
        result += current * num
    
    
    return result
    
    

if __name__ == "__main__":
    result_1 = encode(input)
    print(result_1)
    
    print(decode(result_1))
