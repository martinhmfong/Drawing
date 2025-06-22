# Drawing Program

A terminal-based drawing program that supports creating canvases and drawing shapes with various characters.

## Requirements

- Python 3.10 or higher

## Installation

```bash
git clone git@github.com:martinhmfong/Drawing.git
cd DrawProgram
```

## Running the Program

Run the program using:
```bash
python runner.py
```

## Coordinate System

The program uses a 1-based indexing system where:
- The top-left corner of the canvas is at position (1,1)
- X coordinates increase from left to right (1 to width)
- Y coordinates increase from top to bottom (1 to height)
- All coordinates in commands should be provided using this 1-based system

## Limitations

- Line drawing (L command) only supports vertical and horizontal lines
- Diagonal lines are not supported

## Available Commands

The program supports the following commands:

- `C x y` - Create a new canvas of width x and height y
- `L x1 y1 x2 y2 c` - Draw a line from (x1,y1) to (x2,y2) using character c
- `R x1 y1 x2 y2 c` - Draw a rectangle with corners at (x1,y1) and (x2,y2) using character c
- `B x y c` - Fill the area connected to (x,y) with character c
- `Q` - Quit the program

### Example Usage

```
enter command: C 5 5
-------
|     |
|     |
|     |
|     |
|     |
-------

enter command: L 2 2 4 2 .
-------
|     |
| ... |
|     |
|     |
|     |
-------

enter command: R 1 1 3 3 #
-------
|###  |
|#.#. |
|###  |
|     |
|     |
-------

enter command: B 4 3 *
-------
|###**|
|#.#.*|
|###**|
|*****|
|*****|
-------
```

## Running Tests

To run the test suite:
```bash
python -m unittest discover tests/ -v
```

## Project Structure

```
DrawProgram/
├── runner.py                # Command-line interface
├── src/
│   ├── canvas.py            # Canvas implementation (basic canvas operations)
│   ├── drawing_board.py     # Drawing operations (line, rectangle, bucket fill)
│   ├── validators.py        # Input validation (dimensions, line orientation)
│   └── exceptions.py        # Custom exceptions for error handling
├── tests/
│   ├── test_canvas.py       # Tests for canvas operations
│   ├── test_drawing_board.py# Tests for drawing operations
│   ├── test_runner.py       # Tests for command-line operations
│   └── test_validators.py   # Tests for validation functions
└── README.md
```

## Error Handling

The program handles various error cases:
- Invalid command format
- Invalid number of parameters
- Canvas not initialized
- Out of canvas boundaries
- Invalid line orientation (non-horizontal/vertical)
- Invalid canvas dimensions
