"""
The gpustat module.
"""

__version__ = '0.5.1'

from .__main__ import print_gpustat, main
from .core import GPUStat, GPUStatCollection
from .core import new_query

__all__ = (
    '__version__',
    'GPUStat', 'GPUStatCollection',
    'new_query',
    'print_gpustat', 'main',
)
