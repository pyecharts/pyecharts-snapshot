import os
import codecs
from tempfile import mkstemp

from pyecharts.engine import EchartsEnvironment
from pyecharts_snapshot.main import (
    DEFAULT_DELAY,
    DEFAULT_PIXEL_RATIO,
    make_a_snapshot,
)


class SnapshotEnvironment(EchartsEnvironment):
    def render_chart_to_notebook(self, **_):
        """
        Disable html rendering (_repr_html_) in jupyter.
        """
        return None

    def render_chart_to_file(
        self,
        chart,
        object_name="chart",
        path="render.png",
        template_name="simple_chart.html",
        verbose=True,
        delay=DEFAULT_DELAY,
        pixel_ratio=DEFAULT_PIXEL_RATIO,
        **kwargs
    ):
        _, extension = os.path.splitext(path)
        tmp_file_handle, tmp_file_path = mkstemp(suffix=".html")
        super(SnapshotEnvironment, self).render_chart_to_file(
            chart=chart,
            object_name=object_name,
            path=tmp_file_path,
            template_name=template_name,
            **kwargs
        )
        make_a_snapshot(
            tmp_file_path,
            path,
            delay=delay,
            pixel_ratio=pixel_ratio,
            verbose=verbose,
        )
        os.close(tmp_file_handle)
        content = None
        if extension == ".svg":
            with codecs.open(path, "r", "utf-8") as f:
                content = f.read()
        else:
            with open(path, "rb") as f:
                content = f.read()
        return content
