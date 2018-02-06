"""
Directions on how to setup is in the wiki itself.
"""
import os
import re
import sys
import pydoc
from argparse import ArgumentParser
from subprocess import Popen, PIPE

black_list = ['<p hidden>', '<!--', '<img src']
src_dir = os.path.dirname(os.path.realpath(__file__))


def check_if_up_to_date():
    status = Popen('git -C %s remote show origin' % src_dir,
                   stdout=PIPE, shell=True).stdout.readlines()[-1]
    if 'out of date' in status:
        print '[-] r2wiki out of date.\n ' \
              '\tRun $wiki -u \'\' or \n' \
              '\tUpdate with git -C %s pull origin master' % src_dir
    elif 'fatal: unable to access' in status:
        print '[-] Could not check for r2wiki update'


def arg_parse():
    parse = ArgumentParser()
    parse.add_argument('what_to_search_for', metavar='what_to_search_for',
                       help='What to search for. Supports regex . Triple escape escapes. \\\ ')
    parse.add_argument('-a', action='store_true', dest='match_any',
                       help='Will match any of the words.')

    parse.add_argument('-l', action='store_true', dest='show_link',
                       help='Show the corresponding r2wiki link')
    parse.add_argument('-u', action='store_true', dest='update',
                       help='Update r2wiki with latest content')
    a = parse.parse_args()
    return a


args = arg_parse()
check_if_up_to_date()

if args.update:
    Popen('git -C %s pull origin master' % src_dir, shell=True, stdout=PIPE).wait()
    print '\n[+] r2wiki updated'
    exit(0)

if args.match_any:
    pattern = re.compile('|'.join(args.what_to_search_for.split()), flags=re.IGNORECASE)
else:
    pattern = re.compile(''.join('(?=.*{})'.format(arg) for arg in args.what_to_search_for.split()),
                         flags=re.IGNORECASE)

try:
    from pygments import highlight
    from pygments.lexers import MarkdownLexer
    from pygments.formatters import TerminalFormatter
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

                                    match = re.sub('{\.is-warning}|'
                                                   '{\.is-info}', '', match)

                                    link = '[.](https://radare2.securisec.com/%s)' % md_path.strip(src_dir).strip('.md')
                                    if args.show_link:
                                        found += '%s\n%s' % (link, match)
                                    else:
                                        found += match

    pydoc.pipepager(highlight(found, MarkdownLexer(), TerminalFormatter()), cmd='less -r')

except IndexError:
    print 'Usage: %s search_param' % sys.argv[0]
except NameError:
    print 'pip install -U Pygments'
except ImportError:
    print 'Pygments dependency not met. pip install -U Pygments'
