# MIT License
#
# Copyright (c) 2024 Mr-Major-K
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
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
This module defines a custom exception class `ServerMethodCallError` for
handling errors related to the incorrect calling of server-specific methods on
the client side. This exception is part of the `loggingpython` package,
designed to ensure that server-side methods are not mistakenly invoked on the
client, which could lead to incorrect behavior or security vulnerabilities.

The `ServerMethodCallError` class inherits from the built-in `Exception`
class, allowing it to be raised and caught like any other exception. It takes
an optional message parameter that defaults to "This method can only be called
by the server." This message is passed to the base class constructor to
provide a descriptive error message when the exception is raised.

Example usage:

    try:
        # Attempt to call a server-specific method on the client
        some_client_method()
    except ServerMethodCallError as e:
        print(f"Error: {e}")

This module is part of the `loggingpython` package, which aims to provide a
comprehensive logging solution for Python applications, including error
handling and logging mechanisms for both client and server-side operations.
"""


class ServerMethodCallError(Exception):
    """
    `loggingpython`

    Raised when a method intended for the server is called on the client.
    This error indicates that a method that should only be executed by the
    server was mistakenly called by the client, which could lead to incorrect
    behavior.
    """
    def __init__(self,
                 message="This method can only be called by the server."):
        super().__init__(message)
