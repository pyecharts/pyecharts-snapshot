# coding=utf-8
from __future__ import unicode_literals
from pyecharts import Bar, Line, Scatter, EffectScatter, Grid

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图示例", height=720, width=1200, title_pos="65%")
bar.add("商家A", attr, v1, is_stack=True)
bar.add("商家B", attr, v2, is_stack=True, legend_pos="80%")
line = Line("折线图示例")
attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line.add("最高气温", attr, [11, 11, 15, 13, 12, 13, 10],
         mark_point=["max", "min"], mark_line=["average"])
line.add("最低气温", attr, [1, -2, 2, 5, 3, 2, 0], mark_point=["max", "min"],
         mark_line=["average"], legend_pos="20%")
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
scatter = Scatter("散点图示例", title_top="50%", title_pos="65%")
scatter.add("scatter", v1, v2, legend_top="50%", legend_pos="80%")
es = EffectScatter("动态散点图示例", title_top="50%")
es.add("es", [11, 11, 15, 13, 12, 13, 10],
       [1, -2, 2, 5, 3, 2, 0], effect_scale=6,
       legend_top="50%", legend_pos="20%")

grid = Grid()
grid.add(bar, grid_bottom="60%", grid_left="60%")
grid.add(line, grid_bottom="60%", grid_right="60%")
grid.add(scatter, grid_top="60%", grid_left="60%")
grid.add(es, grid_top="60%", grid_right="60%")
grid.render(path='grid.pdf', delay=3)
