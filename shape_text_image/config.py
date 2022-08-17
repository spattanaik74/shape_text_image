from PIL import ImageFont


class TemplateConfig:
    def __init__(self):
        self.templates = {
            "TEMPLATE_LANDSCAPE": {
                "image": [(5, 5), (990, 450)],
                "header": [(5, 455), (900, 520)],
                "description": [(5, 530), (900, 800)],
                "footer": [(5, 800), (900, 895)]
            },

            "TEMPLATE_PORTRAIT_1": {
                'image': [(5, 5), (460, 894)],
                "header": [(465, 5), (990, 140)],
                "description": [(465, 150), (990, 720)],
                "footer": [(465, 730), (995, 890)]
            },

            "TEMPLATE_PORTRAIT_2": {
                "header": [(5, 5), (694, 73)],
                "image": [(5, 79), (322, 760)],
                "description": [(327, 79), (694, 760)],
                "footer": [(5, 766), (694, 894)]
            },

            "TEMPLATE_PORTRAIT_3": {
                'image': [(5, 100), (500, 894)],
                "header": [(5, 5), (990, 95)],
                "description": [(500, 100), (990, 720)],
                "footer": [(500, 730), (995, 890)]
            },

            "TEMPLATE_PORTRAIT_4": {
                "image": [(470, 110), (650, 890)],
                "header": [(5, 5), (905, 95)],
                "description": [(5, 100), (460, 745)],
                "footer": [(5, 750), (454, 890)]
            }
        }

    def list_templates(self):
        return [k for k, v in self.templates.items()]

    def view_template(self, template_name):
        pass

    def get_template(self, template_name):
        for k, v in self.templates.items():
            if k == template_name:
                return v
        return None


class FontConfig:
    def __init__(self):
        self.font_path = "../shape_text_image/fonts/"

    def get_font(self, font_name, font_size):
        return ImageFont.truetype(font=self.font_path + font_name + '.ttf', size=int(font_size))