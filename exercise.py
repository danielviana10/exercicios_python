def corresponding_parenthesis(text: str):
    left_count = text.count("(")
    right_count = text.count(")")

    if left_count > right_count:
        return ")" * (left_count - right_count)
    elif right_count > left_count:
        return "(" * (right_count - left_count)
    else:
        return ""


result = corresponding_parenthesis(")))(((((")
print(result)


def remove_more_than_two_repetitions(text):
    if len(text) < 3:
        return text

    result = [text[0]]
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
            if count <= 2:
                result.append(text[i])
        else:
            count = 1
            result.append(text[i])

    return "".join(result)


text = "Ollloco meuuuu, taaa peegaando fogoo biiiiichooo"
result1 = remove_more_than_two_repetitions(text)
print(result1)
