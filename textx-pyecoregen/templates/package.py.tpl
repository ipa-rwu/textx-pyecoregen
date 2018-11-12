{% include "{pyecoregen}templates/package.py.tpl" %}

classes = [{{ element.eClassifiers | map(attribute='name') | join(', ') }}]