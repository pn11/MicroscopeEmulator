"""Primary application entrypoint.
"""
import argparse
import json
import os
import pathlib
import sys


def _load_todos():
    fname = str(pathlib.Path.home())+'/.todo.json'
    if not os.path.exists(fname):
        return {}
    else:
        with open(fname) as f:
            return json.load(f) 

def _write_todos(todo_dict):
    fname = str(pathlib.Path.home())+'/.todo.json'
    with open(fname, "w") as f:
        f.write(json.dumps(todo_dict, ensure_ascii=False, indent=4))

def _add_todo(todo_name):
    todo_dict = _load_todos()
    todo_dict[todo_name] = 'Not Yet'
    _write_todos(todo_dict)
    
def _remove_todo(todo_name, all_flag=False):
    todo_dict = _load_todos()
    if all_flag:
        todo_dict.clear()
    else:
        try:
            todo_dict.pop(todo_name)
        except KeyError:
            print("Error: No such To-Do!", file=sys.stderr)
    _write_todos(todo_dict)


def _complete_todo(todo_name, all_flag=False):
    todo_dict = _load_todos()
    if all_flag:
        for k in todo_dict.keys():
            todo_dict[k] = 'Done'
    else:
        try:
            todo_dict[todo_name] = 'Done'
        except KeyError:
            print("Error: No such To-Do!", file=sys.stderr)
    _write_todos(todo_dict)

def _show_todos():
    todo_dict = _load_todos()
    for k, v in todo_dict.items():
        if v == 'Not Yet':
            print('□ ' + k)
        else:
            print('☑ ' + k)

def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('subcommand', help='add, complete, or remove')
    parser.add_argument('content', help='Content of To-Do', nargs='?')
    parser.add_argument('-a', '--all', action='store_true', help='remove or complete all To-Dos')
    args = parser.parse_args()

    todo_dict = _load_todos()

    if args.subcommand == 'add':
        if args.content is not None:
            _add_todo(args.content)
    elif args.subcommand == 'complete':
        if args.content is not None or args.all:
            _complete_todo(args.content, args.all)
    elif args.subcommand == 'remove':
        if args.content is not None or args.all:
            _remove_todo(args.content, args.all)
    elif args.subcommand == 'show':
        _show_todos()
    else:
        print('Error: No such command!', file=sys.stderr)

    
    
    return None
