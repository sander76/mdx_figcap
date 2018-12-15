'''
Figure Caption Extension for Python-Markdown
==================================

Converts \![alttext](http://example.com/image.png "caption")
to the image with a caption.
Its syntax is same as embedding images.

License: [BSD](http://www.opensource.org/licenses/bsd-license.php)

'''

from __future__ import unicode_literals
from markdown.extensions import Extension
from markdown.inlinepatterns import ImagePattern, IMAGE_LINK_RE
from markdown.util import etree
import re


class FigureCaptionExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        # append to inline patterns
        md.inlinePatterns['image_link'] = FigureCaptionPattern(IMAGE_LINK_RE, md)


class FigureCaptionPattern(ImagePattern):
    def handleMatch(self, m):
        image = ImagePattern.handleMatch(self, m)
        title = image.get('title')
        if title:
            span = etree.Element('span')
            figure = etree.SubElement(span, 'figure')
            figure.append(image)
            caption = etree.SubElement(figure, 'figcaption')
            caption.text = title
            return span
        else:
            return image


def makeExtension(*args, **kwargs):
    return FigureCaptionExtension(*args, **kwargs)
