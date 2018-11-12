import os
import jinja2
import pyecoregen

from pyecoregen import ecore


class FileLoader(jinja2.FileSystemLoader):
    ORIGINAL_TEMPLATE_PREFIX = '{pyecoregen}'

    def get_source(self, environment, template):
        if  template.startswith(self.ORIGINAL_TEMPLATE_PREFIX):
            template = template.replace(self.ORIGINAL_TEMPLATE_PREFIX, '', 1)
            pyecoregenDir = os.path.dirname(pyecoregen.__file__)
            filename = os.path.abspath(os.path.join(pyecoregenDir, template))
            f = open(filename, 'rb')
            try:
                contents = f.read().decode(self.encoding)
            finally:
                f.close()
            return contents, filename, None
        return super().get_source(environment, template)


class EcoreGenerator(ecore.EcoreGenerator):

    def create_environment(self, **kwargs):
        env = super().create_environment()
        textxTemplates = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'templates')
        env.loader = FileLoader([textxTemplates, self.templates_path])
        return env
