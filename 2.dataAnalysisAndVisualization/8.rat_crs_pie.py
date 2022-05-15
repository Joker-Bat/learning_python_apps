import justpy as jp
import pandas as pd

data = pd.read_csv('./data/reviews.csv', parse_dates=['Timestamp'])
share = data.groupby(['Course Name'])['Rating'].count()

# print(list(share))

chart_def = """
{
    chart: {
        type: 'pie'
    },
    title: {
        text: 'Count of ratings by course'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Brands',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 61.41,
            sliced: true,
            selected: true
        }, {
            name: 'Internet Explorer',
            y: 11.84
        }, {
            name: 'Firefox',
            y: 10.85
        }, {
            name: 'Edge',
            y: 4.67
        }, {
            name: 'Safari',
            y: 4.18
        }, {
            name: 'Sogou Explorer',
            y: 1.64
        }, {
            name: 'Opera',
            y: 1.6
        }, {
            name: 'QQ',
            y: 1.2
        }, {
            name: 'Other',
            y: 2.61
        }]
    }]
}
"""


def app():
    wp = jp.QuasarPage()

    hc = jp.HighCharts(a=wp, options=chart_def)

    hc.options.xAxis.categories = list(share.index)

    hc_data = [{"name": v1, "y": v2}
               for v1, v2 in zip(list(share.index), list(share))]

    # hc.options.series = [{"name": "Ratings", "data": hc_data}]
    hc.options.series[0].data = hc_data

    return wp


jp.justpy(app)
