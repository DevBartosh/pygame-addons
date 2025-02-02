import numpy
import pygame
from cryptography.hazmat.primitives.hashes import SHA256, Hash

class SurfaceUtils:
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
        surf_array = pygame.surfarray.array2d(surface)
        surface_hash = Hash(SHA256())
        surface_hash.update(str(surf_array).encode())
        string = f"<Surface(sha256={hex(int.from_bytes(surface_hash.finalize()))}>"
        
        return string