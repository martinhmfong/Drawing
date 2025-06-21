class DrawingBoardError(Exception):
    """Base exception for drawing board errors."""
    pass


class CanvasDimensionError(DrawingBoardError):
    """Raised when canvas dimensions are invalid."""
    pass


class OutOfCanvasError(DrawingBoardError):
    """Raised when drawing a point outside the canvas."""
    pass


class CanvasNotReady(DrawingBoardError):
    """Raised when operations are attempted without canvas."""
    pass
