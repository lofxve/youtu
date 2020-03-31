from pyecharts.charts import Pie
from pyecharts import options as opts
from pyecharts.charts import Line
class Draw():
    def drawpie(attr,value,name):
        list1 = [list(z) for z in zip(attr,value)]
        # 图表初始化配置
        init_opts = opts.InitOpts(page_title=name)

        pie = Pie(init_opts=init_opts)
        # 标题配置
        title = opts.TitleOpts(title=name,
                               pos_left='center')
        # 图例配置
        legend_opts = opts.LegendOpts(orient="vertical",
                                      pos_top="20%",
                                      pos_left="15%")

        # 工具箱配置
        # feature = opts.ToolBoxFeatureOpts(save_as_image=True, restore=True, data_view=True, data_zoom=True)
        # 工具箱配置
        toolbox_opts = opts.ToolboxOpts(orient="vertical",
                                        pos_top="25%",
                                        pos_right="15%"
                                        )

        pie.set_global_opts(title_opts=title,
                            legend_opts=legend_opts,
                            toolbox_opts=toolbox_opts
                            )
        # 标签配置项
        pie.add("",
                list1,
                radius=[30, 75],
                center=['50%', '70%'],
                rosetype="area",
                label_opts=opts.LabelOpts(
                    position="outside",
                    formatter="{b|{b}: }{c}  {per|{d}%}  ",
                    background_color="#eee",
                    border_color="#aaa",
                    border_width=1,
                    border_radius=4,
                    rich={
                        "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                        "abg": {
                            "backgroundColor": "#e3e3e3",
                            "width": "100%",
                            "align": "right",
                            "height": 22,
                            "borderRadius": [4, 4, 0, 0],
                        },
                        "hr": {
                            "borderColor": "#aaa",
                            "width": "100%",
                            "borderWidth": 0.5,
                            "height": 0,
                        },
                        "b": {"fontSize": 16, "lineHeight": 33},
                        "per": {
                            "color": "#eee",
                            "backgroundColor": "#334455",
                            "padding": [2, 4],
                            "borderRadius": 2,
                        },
                    },
                ),

         )

        pie.render('{0}.html'.format(name))
    # 趋势图
    def drawline(list1,list4,name):

        # 图表初始化配置
        init_opts = opts.InitOpts(page_title=name)

        line = Line(init_opts=init_opts)
        # 标题配置
        title = opts.TitleOpts(title=name,
                               pos_left="10%")
        # 图例配置
        legend_opts = opts.LegendOpts(orient="horizontal",
                                      pos_top="5%",
                                      pos_right="15%")

        # 工具箱配置
        # feature = opts.ToolBoxFeatureOpts(save_as_image=True, restore=True, data_view=True, data_zoom=True)
        # 工具箱配置
        toolbox_opts = opts.ToolboxOpts(orient="vertical",
                                        pos_bottom="15%",
                                        pos_left="90%",
                                        )

        line.set_global_opts(title_opts=title,
                             legend_opts=legend_opts,
                             toolbox_opts=toolbox_opts,
                             yaxis_opts=opts.AxisOpts(name="单位：岁",
                                                      # axislabel_opts=opts.LabelOpts(formatter="{value}例",
                                                    ),
                             xaxis_opts=opts.AxisOpts(name="日期"),
                            datazoom_opts = opts.DataZoomOpts(orient="vertical"),
                             )
        line.add_xaxis(list4, )
        line.add_yaxis(name, list1, is_smooth=True, linestyle_opts=opts.LineStyleOpts(color="#E83132", width="4"))
        line.render('{0}.html'.format(name))