"""Single-file facade for the Pygments package layout shown in the project.

This file re-exports the public names from the standard Pygments modules so the
whole library can be imported from one module name instead of importing each file
separately.
"""

from pygments import *  # noqa: F401,F403
from pygments.__main__ import *  # noqa: F401,F403
from pygments.cmdline import *  # noqa: F401,F403
from pygments.console import *  # noqa: F401,F403
from pygments.filter import *  # noqa: F401,F403
from pygments.formatter import *  # noqa: F401,F403
from pygments.lexer import *  # noqa: F401,F403
from pygments.modeline import *  # noqa: F401,F403
from pygments.plugin import *  # noqa: F401,F403
from pygments.regexopt import *  # noqa: F401,F403
from pygments.scanner import *  # noqa: F401,F403
from pygments.sphinxext import *  # noqa: F401,F403
from pygments.style import *  # noqa: F401,F403
from pygments.token import *  # noqa: F401,F403
from pygments.unistring import *  # noqa: F401,F403
from pygments.util import *  # noqa: F401,F403

# Keep the module usable in the same way as the original package initializer.
try:
    from pygments import __version__ as __version__  # noqa: F401
except Exception:  # pragma: no cover
    pass

__all__ = [
    "__version__",
    "format", "highlight", "lex",
    "get_lexer_by_name", "get_lexer_for_filename", "get_lexer_for_mimetype",
    "guess_lexer", "guess_lexer_for_filename",
    "get_formatter_by_name", "get_formatter_for_filename",
    "class2html", "TerminalFormatter", "HtmlFormatter",
    "TextLexer", "RegexLexer", "Lexer",
    "Token", "TokenType",
]
