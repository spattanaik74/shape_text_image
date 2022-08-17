class TemplateConfig:
    template_portrait_1 = {"header": [(5, 5), (694, 73)],
                  "image": [(5, 79), (322, 760)],
                  "description": [(327, 79), (694, 760)],
                  "footer": [(5, 766), (694, 894)]}

    template_landscape = {"image": [(5, 5), (990, 450)],
                  "header": [(5, 455), (900, 520)],
                  "description": [(5, 530), (900, 800)],
                  "footer": [(5, 800), (900, 895)]}

    template_portrait = {'image': [(5, 5), (460, 894)],
                  "header": [(465, 5), (990, 140)],
                  "description": [(465, 150), (990, 720)],
                  "footer": [(465, 730), (995, 890)]}

    template_portrait_2 = {'image': [(5, 100), (500, 894)],
                  "header": [(5, 5), (990, 95)],
                  "description": [(500, 100), (990, 720)],
                  "footer": [(500, 730), (995, 890)]}

    template_portrait_3 = {'image': [(470, 110), (650, 890)],
                           "header": [(5, 5), (905, 95)],
                           "description": [(5, 100), (460, 745)],
                           "footer": [(5, 750), (454, 890)]}

    def list_templates(self):
        pass

    def view_template(self, template_name):
        pass


