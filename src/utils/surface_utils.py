import numpy
import pygame

class SurfaceUtils:
    @staticmethod
    def surfaces_equal(
        surface_1: pygame.Surface,
        surface_2: pygame.Surface
    ) -> bool:
        surf_1_array = pygame.surfarray.array2d(surface_1)
        surf_2_array = pygame.surfarray.array2d(surface_2)

        return numpy.array_equal(surf_1_array, surf_2_array)