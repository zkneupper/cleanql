#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Python standard library
import io
import sys


class CaptureStderr(list):
    """A context manager for capturing stderr"""

    def __enter__(self):
        self._stderr = sys.stderr
        sys.stderr = self._stringio = io.StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stderr = self._stderr
