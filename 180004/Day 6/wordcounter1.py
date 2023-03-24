import keyboard
import pyperclip


def word_count(words):
    word_list = words.split()
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    print(word_dict)


keyboard.add_hotkey('shift+windows+w', lambda: word_count(pyperclip.paste()))
keyboard.wait('esc')
keyboard.remove_all_hotkeys()


"""
/r 엔터키


"""