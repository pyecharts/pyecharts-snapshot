import os
import codecs

from pyecharts import EchartsEnvironment

from pyecharts_snapshot.main import make_a_snapshot


class SnapshotEnvironment(EchartsEnvironment):
    def render_chart_to_notebook(self):
        """
        Disable html rendering (_repr_html_) in jupyter.
        """
        return None

    def render_chart_to_file(
            self,
            chart,
            object_name='chart',
            path='render.html',
            template_name='simple_chart.html',
            **kwargs):
        _, extension = os.path.splitext(path)
        if extension == '.html':
            super(EchartsEnvironment, self).render_chart_to_file(
                chart=chart,
                object_name=object_name,
                path=path,
                template_name=template_name,
                **kwargs
            )
        else:
            super(EchartsEnvironment, self).render_chart_to_file(
                chart=chart,
                object_name=object_name,
                path='tmp.html',
                template_name=template_name,
                **kwargs
            )
            make_a_snapshot('tmp.html', path)
            if extension == '.svg':
                with codecs.open(path, 'r', 'utf-8') as f:
                    return f.read()
            else:
                with open(path, 'rb') as f:
                    return f.read()
