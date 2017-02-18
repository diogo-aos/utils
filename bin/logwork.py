import sys
from subprocess import Popen, PIPE
import pickle
from curses import wrapper
from datetime import datetime
import sqlite3
import threading
import curses
import time
from os.path import expanduser, join

class Task:
    def __init__(self, name, db_path):
        self.name = name
        self.db_con = sqlite3.connect(db_path)
        self.windows = {}

        self._last_windowname = ''

    def start(self):
        self.ts_start = datetime.now()
        cur = self.db_con.execute('''INSERT INTO task(start, end, name, comments)
                                     VALUES (?,?,?,?)''',
                                  (self.ts_start, None, self.name, None))
        self.tid = cur.lastrowid
        self.db_con.commit()

        # def store_window(e, tid, db_con):
        #     while not e.isSet():
        #         print('hello')
        #         time.sleep(0.5)
        #         name = get_active_window_name()
        #         db_con.execute('''INSERT INTO monitor_window(ts, windowname, taskid)
        #                           VALUES (?,?,?)''', (datetime.now(), name, tid))
        #         db_con.commit()
        #
        # self.event = threading.Event()
        # self.thread = threading.Thread(target=store_window, args=(self.event, self.tid, self.db_con))
        # self.thread.start()

    def store_window(self):
        name = get_active_window_name()
        if name != self._last_windowname:
            self.db_con.execute('''INSERT INTO monitor_window(ts, windowname, taskid)
                              VALUES (?,?,?)''', (datetime.now(), name, self.tid))
            self.db_con.commit()
            self._last_windowname = name

    def end(self):
        self.ts_end = datetime.now()
        # self.event.set()
        # self.thread.wait()

    def commit(self, comment):
        self.comment = comment
        self.db_con.execute('''UPDATE task SET end=?, comments=? WHERE id=?''',
                    (self.ts_end, comment, self.tid))
        self.db_con.commit()
        self.db_con.close()

def exists_table(con, name):
    cur = con.execute('''SELECT name FROM sqlite_master
                         WHERE type='table' AND name='{}';'''.format(name))
    return len(cur.fetchall()) > 0

def create_tables(con):
    if not exists_table(con, 'task'):
        con.execute('''CREATE TABLE task
                     (id INTEGER PRIMARY KEY, start TIMESTAMP, end TIMESTAMP, name TEXT, comments TEXT)''')
    if not exists_table(con, 'monitor_window'):
        con.execute('''CREATE TABLE monitor_window
                     (id INTEGER PRIMARY KEY, ts TIMESTAMP, windowname TEXT, taskid INTEGER,
                      FOREIGN KEY(taskid) REFERENCES task(id))''')
    con.commit()


def get_active_window_name():
    windowname = Popen(['xdotool', 'getactivewindow'],  stdout=PIPE)
    windowname.wait()
    try:
        window_num = int(windowname.stdout.read())
    except:
        return None
    name = Popen(['xdotool', 'getwindowname', str(window_num)],  stdout=PIPE)
    name.wait()
    return name.stdout.read().decode('utf-8')


def main():
    PERIOD = 0.25
    task_name = input('task name:')
    print('task started at {}'.format(datetime.now()))
    db_path = join(expanduser('~'),'.task_db.sqlite3')

    con = sqlite3.connect(db_path)
    create_tables(con)
    con.close()

    task = Task(task_name, db_path)
    task.start()

    stdscr = curses.initscr()
    curses.noecho()
    stdscr.nodelay(True)
    curses.cbreak()
    stdscr.keypad(True)

    stdscr.clear()  # clear screen
    stdscr.addstr('press f to finish task\n')
    while True:
        time.sleep(PERIOD)
        task.store_window()
        # stdscr.refresh()
        c = stdscr.getch()
        #stdscr.addstr('you pressed {}\n'.format(c))
        if c == 102:
            task.end()
            break

    curses.nocbreak()
    stdscr.keypad(False)
    stdscr.nodelay(False)
    curses.echo()
    curses.endwin()

    comment = input('comment:')
    task.commit(comment)

main()
