# import sys
# import os
#
# current_dir = os.path.dirname(os.path.abspath(__file__))
# project_root = os.path.dirname(os.path.dirname(current_dir))
# sys.path.insert(0, project_root)

from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    """Lead to gold function"""
    return f"Lead transmuted to gold using {create_fire()}"


def stone_to_gem() -> str:
    """Stone to gem function"""
    return f"Stone transmuted to gem using {create_earth()}"
