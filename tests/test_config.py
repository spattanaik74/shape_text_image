from unittest import TestCase

from shape_text_image.config import TemplateConfig


class TestTemplateConfig(TestCase):
    def test_get_template_value_exists(self):
        val = TemplateConfig().get_template("TEMPLATE_LANDSCAPE")
        self.assertEqual([(5, 5), (990, 450)], val["image"])

    def test_get_template_value_not_exists(self):
        val = TemplateConfig().get_template("TEMPLATE_kncsfkgnslkang")
        self.assertIsNone(val)

    def test_view_template(self):
        self.fail()

    def test_list_templates(self):
        val = TemplateConfig().list_templates()
        self.assertTrue(len(val) > 0)
