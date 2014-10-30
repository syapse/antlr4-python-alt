#[The "BSD license"]
# Copyright (c) 2012 Terence Parr
# Copyright (c) 2012 Sam Harwell
# Copyright (c) 2014 Eric Vergnaud
# Copyright (c) 2014 Brian Kearns
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. The name of the author may not be used to endorse or promote products
#    derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
# NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

from antlr4._compat import text_type
from antlr4._java import StringBuilder


def str_collection(val, begin, end):
    return begin + u', '.join([text_type(item) for item in val]) + end

def str_list(val):
    return str_collection(val, u'[', u']')

def str_set(val):
    return str_collection(val, u'{', u'}')

def escapeWhitespace(s, escapeSpaces):
    buf = StringBuilder()
    for c in s:
        if c==' ' and escapeSpaces:
            buf.append(u'\u00B7')
        elif c=='\t':
            buf.append(u"\\t")
        elif c=='\n':
            buf.append(u"\\n")
        elif c=='\r':
            buf.append(u"\\r")
        else:
            buf.append(c)
    return buf.toString()
