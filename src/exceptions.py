"""Custom exceptions for the drawing program."""


class DrawingError(Exception):
    """Base class for all drawing related errors."""
    pass


class CanvasError(DrawingError):
    """Base class for canvas-related errors."""
    pass


class CanvasNotReadyError(CanvasError):
    """Raised when trying to draw on a non-existent canvas."""
    pass


class CanvasDimensionError(CanvasError):
    """Raised when invalid canvas dimensions are provided."""
    pass


class WrongOrientationError(DrawingError):
    """Raised when a line is neither horizontal nor vertical."""
    pass


class OutOfCanvasError(DrawingError):
    """Raised when trying to draw outside canvas bounds."""


class CommandError(DrawingError):
    """Raised when there is an error in command format or parameters."""
    pass
