import unittest

from textnode import TextNode, TextType


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
        node = TextNode("Easy URL", TextType.PLAIN_TEXT, "https://www.pornhub.com")
        node2 = TextNode("Easy URL", TextType.PLAIN_TEXT, "https://www.pornhub.com")
        self.assertEqual(node, node2)
    def test_noteq_URLNONE(self):
        node = TextNode("Easy URL", TextType.PLAIN_TEXT, "https://www.pornhub.com")
        node2 = TextNode("Easy URL", TextType.PLAIN_TEXT)
        self.assertNotEqual(node, node2)
if __name__ == "__main__":
    unittest.main()