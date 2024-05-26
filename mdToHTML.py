import sys
import markdown

inputPath = '/home/ubuntu/mydir/FrontEnd1/MarkdownToHTML/test.md'
outputPath = '/home/ubuntu/mydir/FrontEnd1/MarkdownToHTML/output.html'

input = ''

with open(inputPath) as f:
    input = f.read()

def mdToHTML():
    output = markdown.markdown(input)

    with open(outputPath, 'w') as f:
        f.write(output)

mdToHTML()