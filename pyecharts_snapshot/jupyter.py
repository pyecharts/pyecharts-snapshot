import os
import codecs

from pyecharts.engine import EchartsEnvironment

from pyecharts_snapshot.main import make_a_snapshot


class SnapshotEnvironment(EchartsEnvironment):
    def render_chart_to_notebook(self, **_):
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
            verbose=True,
            **kwargs):
        _, extension = os.path.splitext(path)
        if extension == '.html':
            super(SnapshotEnvironment, self).render_chart_to_file(
                chart=chart,
                object_name=object_name,
                path=path,
                template_name=template_name,
                **kwargs
            )
        else:
            super(SnapshotEnvironment, self).render_chart_to_file(
                chart=chart,
                object_name=object_name,
                path='tmp.html',
                template_name=template_name,
                **kwargs
            )
            make_a_snapshot('tmp.html', path, verbose=verbose)
            content = None
            if extension == '.svg':
                with codecs.open(path, 'r', 'utf-8') as f:
                    content = f.read()
            else:
                with open(path, 'rb') as f:
                    content = f.read()
            return content
