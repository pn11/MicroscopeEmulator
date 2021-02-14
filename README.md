# CUI Command Sample in Python

This is a sample project for a CUI command written in Python. To write a command, all we need to know is how to use `argparse` and how to write `setup.py`.
In this example, I will make a command called `todo` which has commands like below.

- `todo add "buy a milk"`
- `todo complete "buy a milk"`
- `todo remove "buy a milk"`
- `todo complete -a`
- `todo remove -a`

## The source code

By using `argparse`, we can add subcommands and options. By "subcommand", I mean "commit" in a commandline `git commit -m "add my cool feature"`, which is acturally the first argument.   
For other chunks, I call them:

- command: git
- subcommand: commit
- option: -m
- argument for option -m: "add my cool feature"

## `setup.py`

Need `console_scripts` to install as a CUI command.
