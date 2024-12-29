import pygame

# Initialize the pygame mixer
pygame.mixer.init()
sound = pygame.mixer.Sound("339129__indigoray__beep-select.wav")
sound.play()
pygame.time.wait(1000)  # Adjust based on sound duration
