import pygame

# Initialize the mixer
pygame.mixer.init()

# Load the .wav file
sound = pygame.mixer.Sound("339129__indigoray__beep-select.wav")

# Play the sound
sound.play()

# Wait to allow the sound to finish (optional)
pygame.time.wait(1000)  # Adjust based on sound duration
