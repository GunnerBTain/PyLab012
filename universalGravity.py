class UniversalGravity:
    """Represents universal gravitational constants."""
    G: float = 6.67430e-11  # Default; can be overridden

    def __init__(self, G: float = None):
        if G is not None:
            self.G = G
