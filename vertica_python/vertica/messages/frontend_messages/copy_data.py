# Copyright (c) 2013-2017 Uber Technologies, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from __future__ import print_function, division, absolute_import

from six import text_type, binary_type

from ..message import BulkFrontendMessage

UTF_8 = 'utf-8'


class CopyData(BulkFrontendMessage):
    message_id = b'd'

    def __init__(self, data, unicode_error='strict'):
        BulkFrontendMessage.__init__(self)
        self._unicode_error = unicode_error
        if isinstance(data, text_type):
            self._data = self._data.encode(encoding=UTF_8, errors=self._unicode_error)
        elif isinstance(data, binary_type):
            self._data = data
        else:
            raise TypeError("should be string or bytes")

    def read_bytes(self):
        # to deal with unicode strings
        bytes_ = self._data
        return bytes_
