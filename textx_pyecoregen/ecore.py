import os
import jinja2

from pyecoregen import ecore
import pyecore.type


class FileSystemLoader(jinja2.FileSystemLoader):
    ORIGINAL_TEMPLATE_PREFIX = '{pyecoregen}'

    def get_source(self, environment, template):
        '''
        pyecoregen and textx-pyecoregen use the same template names, to distinguish
        them, a a prefix is used which cannot be resolved by a FilesystemLoader

        TODO a PrefixLoader might do the job
        '''
        if template.startswith(self.ORIGINAL_TEMPLATE_PREFIX):
            template = template.replace(self.ORIGINAL_TEMPLATE_PREFIX, '', 1)
            filename = os.path.abspath(os.path.join(
                self.ecoregentemplates, template))
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
        textxTemplates = os.path.join(os.path.abspath(
            os.path.dirname(__file__)), 'templates')
        env.loader = FileSystemLoader([textxTemplates, self.templates_path])
        env.loader.ecoregentemplates = self.templates_path
        return env
