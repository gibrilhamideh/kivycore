


import os
import sys

def resource_path(relative_path):

    base_path = os.path.dirname(__file__)
    return os.path.join(getattr(sys, '_MEIPASS', base_path), relative_path) 


path = os.path.dirname(__file__)
"""Path to main directory."""

screens_path = resource_path("screens")
"""Path to screens directory."""

data_path = resource_path("data")
"""Path to data directory."""

widgets_path = resource_path("widgets")
"""Path to widgets directory."""

core_path = resource_path("core")


