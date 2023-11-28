import re

from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor

class MyExtension(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(MyPreprocessor(md), 'func_args', 175)

class MyPreprocessor(Preprocessor):
    def run(self, lines):
        new_lines = []
        for line in lines:
            # Replace custom tag with a styled <div>
            line = line.replace('<args>', '<div style="color: blue;">')
            line = line.replace('</args>', '</div>')
            new_lines.append(line)
        return new_lines


def makeExtension(*args, **kwargs):
    # Return extension
    return MarkExtension(*args, **kwargs)