"""
Directions on how to setup is in the wiki itself.
"""
import os
import re
import sys
import pydoc
from argparse import ArgumentParser
from pygments import highlight
from pygments.lexers import MarkdownLexer
from pygments.formatters import TerminalFormatter

def arg_parse():
    parse = ArgumentParser()
    parse.add_argument('what_to_search_for', metavar='what_to_search_for',
                       help='What to search for. Supports regex . Triple escape escapes. \\\ ')
    parse.add_argument('-a', action='store_true', dest='match_any',
                       help='Will match any of the words.')
    a = parse.parse_args()
    return a

args = arg_parse()

if args.match_any:
    pattern = re.compile('|'.join(args.what_to_search_for.split()), flags=re.IGNORECASE)
else:
    pattern = re.compile(''.join('(?=.*{})'.format(arg) for arg in args.what_to_search_for.split()),
                         flags=re.IGNORECASE)

black_list = ['<p hidden>', '<!--', '<img src']
src_dir = os.path.dirname(os.path.realpath(__file__))

try:

    found = ''

    for path, subdirs, files in os.walk(src_dir):
        for name in files:
            md_path = os.path.join(path, name)
            if not '.git' in md_path and md_path.endswith('.md'):
                with open(md_path, 'r') as f:
                    for lines in f.readlines():
                        if re.search(pattern, lines):
                            if not any(filter in lines for filter in black_list):
                                match = ((re.sub('\*\*', '', lines)).lstrip() + '\n')  # .replace('`', "'")
                                if match.startswith('- ['):
                                    split = match.split(']')
                                    found += max(split, key=len).replace('[', '') + \
                                             ' [.](https://radare2.securisec.com%s' % split[-1].strip('(')
                                else:
                                    if match.startswith('>'):
                                        match = ''.join(list(match)[1:])
                                    if match.startswith('#'):
                                        match = ''.join(list(match)[1:])
                                    if match.startswith(' _'):
                                        match = re.sub('_', '', ''.join(list(match)[1:]))

                                    match = re.sub('<U\+1F680>', '', match)

                                    found += match.strip('<U+1F680>')

    pydoc.pipepager(highlight(found, MarkdownLexer(), TerminalFormatter()), cmd='less -R')

except IndexError:
    print 'Usage: %s search_param' % sys.argv[0]
except NameError:
    print 'pip install Pygments'
except ImportError:
    print 'Pygments dependency not met. pip install Pygments'
