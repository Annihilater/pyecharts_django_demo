from django.shortcuts import render

# Create your views here.
import json
from random import randrange

from django.http import HttpResponse
from rest_framework.views import APIView

from pyecharts.charts import Line
from pyecharts import options as opts


# Create your views here.
def response_as_json(data):
    json_str = json.dumps(data)
    response = HttpResponse(
        json_str,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response


def json_response(data, code=200):
    data = {
        "code": code,
        "msg": "success",
        "data": data,
    }
    return response_as_json(data)


def json_error(error_string="error", code=500, **kwargs):
    data = {
        "code": code,
        "msg": error_string,
        "data": {}
    }
    data.update(kwargs)
    return response_as_json(data)


JsonResponse = json_response
JsonError = json_error


def line_base() -> Line:
    line = (
        Line()
            .add_xaxis(list(range(10)))
            .add_yaxis(series_name="", y_axis=[randrange(0, 100) for _ in range(10)])
            .set_global_opts(
            title_opts=opts.TitleOpts(title="动态数据"),
            xaxis_opts=opts.AxisOpts(type_="value"),
            yaxis_opts=opts.AxisOpts(type_="value")
        )
            .dump_options_with_quotes()
    )
    return line


class ChartView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(line_base()))


cnt = 9


class ChartUpdateView(APIView):
    def get(self, request, *args, **kwargs):
        global cnt
        cnt = cnt + 1
        return JsonResponse({"name": cnt, "value": randrange(0, 100)})


class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(content=open("./templates/index.html").read())
