import re
import xml.etree.ElementTree as etree

from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor

class MyExtension(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(MyPreprocessor(md), 'func_returns', 175)

class MyPreprocessor(Preprocessor):
    def run(self, lines):
        # Join lines into a single string
        source_text = "\n".join(lines)
        
        # Get relevant elements
        rets_elements = re.findall(r'<rets>[\s\S]*?</rets>', source_text)

        # Process elements
        for rets_element in rets_elements:
            
            parsed_RetsElement = etree.fromstring(rets_element)
            retsResult = processRetsElement(parsed_RetsElement)

            source_text = source_text.replace(rets_element, retsResult)

        # Split the modified text back into lines
        modified_lines = source_text.splitlines()

        return modified_lines


import textwrap

def processRetsElement(retsElement):    
    html_entries = ""

    count = 1

    for ret_element in retsElement.findall(".//ret"):

        ret = {
            "name": ret_element.attrib.get("name"),
            "type": ret_element.attrib.get("type"),
        }
        
        html_entries += f'''
        <tr>
            <td>{count}: <b>{ret["name"]}</b></td>
            <td>{ret["type"]}</td>
            <td>{ret_element.text}</td>
        </tr>
        '''

        count += 1 # increment
    
    result = textwrap.dedent(f'''
    <div>
        <p>Returns</p>
        <table>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
        {html_entries}
        </table>
    </div>
    ''')

    return result



def makeExtension(*args, **kwargs):
    # Return extension
    return MyExtension(*args, **kwargs)