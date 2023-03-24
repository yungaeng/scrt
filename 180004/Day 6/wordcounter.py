import keyboard
import pyperclip


def world_count(words):
    word_list = words.split()
    word_dict = {}
    for n in len(word_list):
        if word_list[n] in word_dict.kets():
            word_dict[len[n]] += 1
        else:
            word_dict.setdefault(word_list[n], 1)
    print(word_dict)


keyboard.add_hotkey('shift+windows+w', lambda: world_count(pyperclip.paste))
keyboard.wait('esc')
keyboard.remove_all_hotkeys()
