def do_search_list(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    found = []
    for letter in word:
        if letter in vowels:
            if letter not in found:
                found.append(letter)
    return found


def do_search_set(word):
    vowels = set('aieeouu')
    print(vowels)
    found = vowels.intersection(set(word))
    return found


def do_search_dict(word):
    found = {}
    vowels = set('aieoouu') #Создали множество
    print(vowels)
    found['a'] = 0
    found['i'] = 0
    found['e'] = 0
    found['o'] = 0
    found['u'] = 0
    for letter in word:
        if letter in vowels:
            found[letter] += 1
    return found


if __name__ == '__main__':
    word = input('Введите слово для поиска гласных \n')
    #word = word.strip()

    found = do_search_dict(word)
    print('found=', found)
    print('found_items=', found.items())
    print('Количество найденных гласных')
    for k, v in (found.items()):
        if v > 0:
            print(k, 'найдено', v, 'раз')

    print('The end')

