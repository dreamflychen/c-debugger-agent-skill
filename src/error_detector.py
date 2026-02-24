# Error Detection Module

class ErrorDetector:
    def __init__(self, data):
        self.data = data

    def detect_errors(self):
        errors = []
        for index, value in enumerate(self.data):
            # Example error detection logic
            if value < 0:
                errors.append((index, 'Negative value detected'))
        return errors

# Example usage
if __name__ == '__main__':
    detector = ErrorDetector([10, -1, 23, -5, 0])
    detected_errors = detector.detect_errors()
    print(detected_errors)