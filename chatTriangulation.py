import numpy as np

class SoundTriangulation:
    def __init__(self, mic_positions, sound_speed=343):
        """
        Initializes a sound triangulation object.

        Parameters:
        mic_positions (numpy array): The positions of the microphones as an Nx3 array, where N is the number of microphones.
        sound_speed (float): The speed of sound in m/s.
        """
        self.mic_positions = mic_positions
        self.sound_speed = sound_speed

    def estimate_direction(self, tdoas):
        """
        Estimates the direction of an incoming signal based on the time differences of arrival (TDOAs) at the microphones.

        Parameters:
        tdoas (numpy array): An array of TDOAs in seconds, with the first microphone as the reference.

        Returns:
        direction (numpy array): A unit vector pointing in the direction of the incoming signal.
        """
        # Convert TDOAs to distances
        distances = tdoas * self.sound_speed

        # Construct the system of equations
        print(self.mic_positions[1:], self.mic_positions[0])
        A = 2 * (self.mic_positions[1:] - self.mic_positions[0])
        b = np.square(distances[1:]) - np.square(distances[0]) + np.square(self.mic_positions[0]) - np.square(self.mic_positions[1:]).sum(axis=1)

        # Solve for the direction vector
        direction, _, _, _ = np.linalg.lstsq(A, b, rcond=None)

        # Normalize the direction vector
        direction /= np.linalg.norm(direction)

        return direction

    def _get_direction(self, delays):
        c = self.sound_speed
        x = self.mic_positions
        d = delays * c
        distances = np.sqrt(np.sum((x[1:] - x[0])**2, axis=1))
        print(distances, d[1:], d[0])
        cos_alpha = (np.square(distances) - np.square(d[1:]) + np.square(d[0])) / (2 * distances * d[0])
        sin_alpha = np.sqrt(1 - np.square(cos_alpha))
        b = np.square(distances[1:]) - np.square(distances[0]) + np.square(x[0][0]) - np.square(x[1:, 0]) - np.square(x[1:, 1]) + 2 * x[1:, 0] * x[0][0] - 2 * x[1:, 1] * x[0][1]
        cos_theta = b / (2 * distances * np.sqrt(np.square(x[1:, 0] - x[0][0]) + np.square(x[1:, 1] - x[0][1])))
        sin_theta = np.sqrt(1 - np.square(cos_theta))
        direction = np.array([
            np.mean(sin_alpha * sin_theta),
            np.mean(sin_alpha * cos_theta),
            np.mean(cos_alpha)
        ])
        return direction / np.linalg.norm(direction)


