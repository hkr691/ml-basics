class Vector:
    def __init__(self, components):
        self.components = list(components)
        self.dim = len(self.components)
    
    def _is_valid_length(self, other):
        if self.dim != other.dim:
            raise ValueError("Vectors need to be of the same length.")
        return True 
    
    def __add__(self, other):
        self._is_valid_length(other)
        return Vector([a + b for a, b in zip(self.components, other.components)])
    
    def __sub__(self, other):
        self._is_valid_length(other)
        return Vector([a - b for a, b in zip(self.components, other.components)])
    
    def dot(self, other):
        self._is_valid_length(other)
        return sum(a * b for a, b in zip(self.components, other.components))
    
    def magnitude(self):
        return sum(a ** 2 for a in self.components) ** 0.5
    
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector([x / mag for x in self.components])
    
    def cosine_similarity(self, other):
        mag_self = self.magnitude()
        mag_other = other.magnitude()
        if mag_self == 0 or mag_other == 0:
            raise ValueError("Cannot compute cosine similarity with a zero vector.")
        return self.dot(other) / (mag_self * mag_other)
    
    def __repr__(self):
        return f"Vector({self.components})"