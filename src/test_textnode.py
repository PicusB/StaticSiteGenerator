import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node = TextNode("This is a bold node", TextType.BOLD_TEXT)
        node2 = TextNode("This is an italic node", TextType.ITALIC_TEXT)
        self.assertNotEqual(node, node2)
    def test_eq_urls(self):
        node = TextNode("Easy URL", TextType.PLAIN_TEXT, "https://boot.dev")
        node2 = TextNode("Easy URL", TextType.PLAIN_TEXT, "https://boot.dev")
        self.assertEqual(node, node2)
    def test_noteq_URLNONE(self):
        node = TextNode("Easy URL", TextType.PLAIN_TEXT, "https://boot.dev")
        node2 = TextNode("Easy URL", TextType.PLAIN_TEXT)
        self.assertNotEqual(node, node2)

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a Test Paragraph", [], None)
        node2 = HTMLNode("p", "This is a Test Paragraph", [], None)
        self.assertEqual(node, node2)
    def test_eq(self):
        node = HTMLNode("a", "Linked Page", None, {"href" : "https://boot.dev"})
        node2 = HTMLNode("a", "Linked Page", None, {"href" : "https://boot.dev"})
        self.assertEqual(node, node2)
    def test_noteq(self):
        node = HTMLNode("p", "This is a Test Paragraph", [], None)
        node2 = HTMLNode("h1", "This is a Test Paragraphs", [], None)
        self.assertNotEqual(node, node2)

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click Here!", {"href":'"https://boot.dev"'})
        self.assertEqual(node.to_html(), '<a href="https://boot.dev">Click Here!</a>')
    def test_leaf_to_htm_noteq(self):
        node = LeafNode("a", "Click Here!", {"href":'"https://boot.dev"', "color": '"red"'})
        self.assertNotEqual(node.to_html(), '<a href="https://boot.dev">Click Here!</a>')

if __name__ == "__main__":
    unittest.main()