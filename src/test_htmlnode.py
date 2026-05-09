import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

        def test_values(self):
            node = HTMLNode("div", "I wish I could read")
            self.assertEqual(node.tag, "div")
            self.assertEqual(node.children, None)
            self.assertEqual(node.props, None)

        def test_repr(self):
            node = HTMLNode("p", "What a strange world", None, {"class": "primary"})
            self.assertEqual(
                node.__repr__(),
                "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
            )


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_repr(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(
            node.__repr__(),
            "LeafNode(p, Hello, world!, None)",
        )
