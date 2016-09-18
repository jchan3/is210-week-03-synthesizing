#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

STRING1 = 'Spanish'
STRING2 = 'Flemish'
LENGTH = len(STRING1)
SPANISH_INDEX = (inquisition.SPANISH).index(STRING1)
STRING3 = (inquisition.SPANISH)[0:SPANISH_INDEX]
NEW_INDEX = SPANISH_INDEX + LENGTH
STRING4 = (inquisition.SPANISH)[NEW_INDEX:]

FLEMISH = STRING3 + STRING2 + STRING4
