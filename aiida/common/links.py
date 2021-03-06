# -*- coding: utf-8 -*-
from enum import Enum

__copyright__ = u"Copyright (c), This file is part of the AiiDA platform. For further information please visit http://www.aiida.net/. All rights reserved."
__license__ = "MIT license, see LICENSE.txt file."
__authors__ = "The AiiDA team."
__version__ = "0.7.1"


class LinkType(Enum):
    """
    A simple enum of allowed link types.
    """
    UNSPECIFIED = 'unspecified'
    CREATE = 'createlink'
    RETURN = 'returnlink'
    INPUT = 'inputlink'
    CALL = 'calllink'
