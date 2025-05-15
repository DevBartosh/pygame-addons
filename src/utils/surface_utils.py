from hashlib import sha256

import numpy
import pygame

class SurfaceUtils:
    """
    Class containing additional methods for surfaces.
    """
    @staticmethod
    def surfaces_equal(
        surface_1: pygame.Surface,
        surface_2: pygame.Surface
    ) -> bool:
        surf_1_array = pygame.surfarray.array2d(surface_1)
        surf_2_array = pygame.surfarray.array2d(surface_2)

        return numpy.array_equal(surf_1_array, surf_2_array)

    @staticmethod
    def str_surface(surface: pygame.Surface) -> str:
        surface_array = pygame.surfarray.array2d(surface)
        string = f"<Surface(sha256={sha256(str(surface_array).encode()).hexdigest()}>"

        return string