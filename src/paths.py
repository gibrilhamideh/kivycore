


import os
import sys

def resource_path(relative_path):

    base_path = os.path.dirname(__file__)
    return os.path.join(getattr(sys, '_MEIPASS', base_path), relative_path) 


path = os.path.dirname(__file__)
"""Path to main directory."""

screens_path = resource_path("screens")
"""Path to screens directory."""

components_path = resource_path("theme/components")
"""Path to components directory."""

resources_path = resource_path("resources")
"""Path to resources directory."""

core_path = resource_path("core")
"""Path to core directory."""

