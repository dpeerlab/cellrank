# -*- coding: utf-8 -*-
from scanpy import settings

import cellrank.tools as tl
import cellrank.utils as ul
import cellrank.datasets
import cellrank.plotting as pl
from cellrank.tools._read import read
from cellrank.tools._constants import Lin

__author__ = ", ".join(["Marius Lange", "Michal Klein", "Juan Luis Restrepo Lopez"])
__email__ = ", ".join(["info@cellrank.org"])

try:
    from setuptools_scm import get_version

    __version__ = get_version(root="..", relative_to=__file__)
except (LookupError, ImportError):
    from packaging import version

    try:
        from importlib_metadata import version as get_version  # Python < 3.8
    except ImportError:
        from importlib.metadata import version as get_version  # Python = 3.8

    __version__ = version.parse(get_version(__name__))
    del version

del get_version
