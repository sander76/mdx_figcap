import markdown


input1 = """
# PowerView® Venetian Blind programming with Remote control
The PowerView® M25S single shaft motor is suited to be used with Ultimate Venetian blind hardware from HunterDouglas.


![Venetian blind](/imgs/m25s/m25s_vb_detail.png "Venetian blind"){: .center-block}


asdfasdf
"""

md = markdown.Markdown(extensions=["markdown.extensions.attr_list", "mdx_figcap"])


def test1():
    txt = md.convert(input1)
    print(txt)
    assert True


test1()
