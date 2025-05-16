import pygame

def surfaces_equal(
    surface_1: pygame.Surface,
    surface_2: pygame.Surface
) -> bool:
    surf_1_bytes = pygame.image.tobytes(surface_1, "RGBA")
    surf_2_bytes = pygame.image.tobytes(surface_2, "RGBA")

    return surf_1_bytes == surf_2_bytes