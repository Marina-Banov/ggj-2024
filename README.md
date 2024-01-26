# GGJ 2024

## Setup

**Requirements:**

- Python 3.9

**Note:** you might want to initialize a Python [virtual environment](https://docs.python.org/3/tutorial/venv.html).

**Install the required packages:**

```
pip install pygame
```

**Run the project:**

```
python main_desktop.py
```

## Deploy

To play the game in a modern browser, compile to WASM:

```
pip install pygbag
pygbag . --ume_block 0
```

Visit `localhost:8000`.
