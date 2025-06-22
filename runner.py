from src.drawing_board import DrawingBoard
from src.exceptions import CommandError, DrawingError


def validate_params(cmd: str, params: list) -> tuple:
    match [cmd, *params]:
        case ['Q']:
            return ()

        case ['C', width, height]:
            try:
                return int(width), int(height)
            except ValueError:
                raise CommandError("Canvas dimensions must be integers")

        case ['L' | 'R', x1, y1, x2, y2, c]:
            if len(c) != 1:
                raise CommandError("Parameter c must be a character (length 1)")
            try:
                return int(x1), int(y1), int(x2), int(y2), c
            except ValueError:
                raise CommandError("Coordinates must be integers")

        case ['B', x, y, c]:
            if len(c) != 1:
                raise CommandError("Parameter c must be a character (length 1)")
            try:
                return int(x), int(y), c
            except ValueError:
                raise CommandError("Coordinates must be integers")

        case [cmd, *_] if cmd in ('L', 'R'):
            raise CommandError(f"{cmd} requires 5 parameters: x1 y1 x2 y2 c")

        case [cmd, *_] if cmd == 'B':
            raise CommandError("B requires 3 parameters: x y c")

        case [cmd, *_] if cmd == 'C':
            raise CommandError("C requires 2 parameters: width height")

        case _:
            raise CommandError(f"Unknown command: {cmd}")


def main():
    board = DrawingBoard()
    print("\nDrawing Program")
    print("Commands:")
    print("  C x y             # Create canvas")
    print("  L x1 y1 x2 y2 c   # Draw line")
    print("  R x1 y1 x2 y2 c   # Draw rectangle")
    print("  B x y c           # Bucket fill")
    print("  Q                 # Quit\n")

    while True:
        try:
            command = input("enter command: ").strip()
            if not command:
                continue

            parts = command.split()
            cmd, params = parts[0].upper(), parts[1:]

            validated_params = validate_params(cmd, params)

            match cmd:
                case 'Q':
                    print("Quitting...")
                    break

                case 'C':
                    board.new_canvas(*validated_params)
                    print(board)

                case 'L':
                    board.draw_line(*validated_params)
                    print(board)

                case 'R':
                    board.draw_rectangle(*validated_params)
                    print(board)

                case 'B':
                    board.bucket_fill(*validated_params)
                    print(board)

        except CommandError as e:
            print(f"Command error: {str(e)}")
        except DrawingError as e:
            print(f"Drawing error: {str(e)}")
        except Exception as e:
            print(f"Unexpected error: {str(e)}")


if __name__ == "__main__":
    main()
