# Notebook
General Task Framework inspired by Jupyter Notebooks

# Design Idea

The goal of this project is to create a better and more dynamic script.
A `notebook` is a collection of `cell` methods that should be executed sequentially.
Each `cell` has access to the `notebook`'s variables and can modify them.
Any local variable created in a `cell` will only be available to that `cell`.

Each notebook should be instantiated from a configuration file, or set of configuration files, that define the initial state of the notebook.

## Development Notes


