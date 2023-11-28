import re
import xml.etree.ElementTree as etree

from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor

class MyExtension(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(MyPreprocessor(md), 'func_args', 175)

class MyPreprocessor(Preprocessor):
    def run(self, lines):
        # Join lines into a single string
        source_text = "\n".join(lines)
        
        # Find all <args> elements using regular expressions
        args_elements = re.findall(r'<args>[\s\S]*?</args>', source_text)

        # Process each <args> element
        for args_element in args_elements:
            
            parsed_ArgsElement = etree.fromstring(args_element)
            argsResult = processArgsElement(parsed_ArgsElement)

            source_text = source_text.replace(args_element, argsResult)

        # Split the modified text back into lines
        modified_lines = source_text.splitlines()

        return modified_lines


import textwrap

def processArgsElement(argsElement):    
    html_args = ""

    arg_count = 1

    for arg_element in argsElement.findall(".//arg"):

        argName = arg_element.attrib.get("name")
        argType = arg_element.attrib.get("type")
        argDefault = arg_element.attrib.get("default")

        
        html_args += f'''
        <tr>
            <td>{arg_count}: <b>{argName}</b></td>
            <td>{argType}</td>
            <td>{arg_element.text}</td>
        </tr>
        '''

        arg_count += 1 # increment
    
    result = textwrap.dedent(f'''
    <div>
        <p>Arguments</p>
        <table>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
        {html_args}
        </table>
    </div>
    ''')

    return result



def makeExtension(*args, **kwargs):
    # Return extension
    return MyExtension(*args, **kwargs)