global a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
choice = int(input("What would you like to do \n1) from morse code to words \n2) from words do morse \n"))
word = str(input("What are the caracters/words that you want to translate? \n"))
final_word = ""
def translation(letter):
    if letter == "a" or letter == ".-":
        return ["a", ".-"]
    elif letter == "b" or letter == "-...":
        return ["b", "-..."]
    elif letter == "c" or letter == "-.-.":
        return ["c", "-.-."]
    elif letter == "d" or letter == "-..":
        return ["d", "-.."]
    elif letter == "e" or letter == ".":
        return ["e", "."]
    elif letter == "f" or letter == "..-.":
        return ["f", "..-."]
    elif letter == "g" or letter == "--.":
        return ["g", "--."]
    elif letter == "h" or letter == "....":
        return ["h", "...."]
    elif letter == "i" or letter == "..":
        return ["i", ".."]
    elif letter == "j" or letter == ".---":
        return ["j", ".---"]
    elif letter == "k" or letter == "-.-":
        return ["k", "-.-"]
    elif letter == "l" or letter == ".-..":
        return ["l", ".-.."]
    elif letter == "m" or letter == "--":
        return ["m", "--"]
    elif letter == "n" or letter == "-.":
        return ["n", "-."]
    elif letter == "o" or letter == "---":
        return ["o", "---"]
    elif letter == "p" or letter == ".--.":
        return ["p", ".--."]
    elif letter == "q" or letter == "--.-":
        return ["q", "--.-"]
    elif letter == "r" or letter == ".-.":
        return ["r", ".-."]
    elif letter == "s" or letter == "...":
        return ["s", "..."]
    elif letter == "t" or letter == "-":
        return ["t", "-"]
    elif letter == "u" or letter == "..-":
        return ["u", "..-"]
    elif letter == "v" or letter == "...-":
        return ["v", "...-"]
    elif letter == "w" or letter == ".--":
        return ["w", ".--"]
    elif letter == "x" or letter == "-..-":
        return ["x", "-..-"]
    elif letter == "y" or letter == "-.--":
        return ["y", "-.--"]
    elif letter == "z" or letter == "--..":
        return ["z", "--.."]
    else:
        return [" ", "..--"]
if choice == 1:
    word = word.replace("/", " ")
    new_word = word.split()
    for i in range(len(new_word)):
        letter = new_word[i]
        final_word += str(translation(letter)[0])
if choice == 2:
    for i in range(len(word)):
        letter = word[i]
        if i == len(word)-1:
            final_word += str(translation(letter)[1])
        else:
            final_word += str(translation(letter)[1]) + "/"
print(final_word)
