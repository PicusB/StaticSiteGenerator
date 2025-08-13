import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode


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

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
            )
    def test_no_children_error(self):
        with self.assertRaises(ValueError) as cm:
            ParentNode("b", None)
        self.assertEqual(str(cm.exception), "Parent Node must have children")
    def test_not_equal_nested(self):
        grandchild_node = LeafNode("i", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertNotEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
            )
    def test_multichild_equal(self):
        child1 = LeafNode("b", "FirstChild")
        child2 = LeafNode("i", "SecondChild")
        child3 = LeafNode("u", "ThirdChild")
        parent = ParentNode("b", [child1, child2, child3])
        self.assertEqual(parent.to_html(), "<b><b>FirstChild</b><i>SecondChild</i><u>ThirdChild</u></b>")


if __name__ == "__main__":
    unittest.main()