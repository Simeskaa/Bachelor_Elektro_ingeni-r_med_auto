import numpy as np

class Triangulator:
    def __init__(self, mic_pos, speed_of_sound=343):
        self.mic_positions = mic_pos
        self.speed_of_sound = speed_of_sound

    def _get_direction(self, delays):
        # Compute distances and convert to meters
        distances = np.array(delays) * self.speed_of_sound

        # Compute direction vectors for each microphone pair
        a = self.mic_positions[1:] - self.mic_positions[0]
        b = np.square(distances[1:]) - np.square(distances[0]) + np.square(self.mic_positions[0]) - np.square(self.mic_positions[1:]).sum(axis=1, keepdims=True)
        direction_vectors = np.linalg.solve(2 * a, b).T

        # Normalize direction vectors
        norms = np.linalg.norm(direction_vectors, axis=1)
        normalized_directions = direction_vectors / norms[:, np.newaxis]

        # Compute angles between direction vectors and x-axis
        angles = np.arctan2(normalized_directions[:,1], normalized_directions[:,0]) * 180 / np.pi
        return angles
