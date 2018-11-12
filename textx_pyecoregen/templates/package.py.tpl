{% include "{pyecoregen}package.py.tpl" %}

classes = [{{ element.eClassifiers | map(attribute='name') | join(', ') }}]