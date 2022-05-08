import justpy as jp
import pandas as pd

data = pd.read_csv('./data/reviews.csv', parse_dates=["Timestamp"])
data['Month'] = data['Timestamp'].dt.strftime("%Y-%m")
month_average = data.groupby(["Month"]).mean()


chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Analysis of course Reviews'
    },
    subtitle: {
        text: 'These graphs represent course review analysis'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Month'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: ''
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        },
        labels: {
            format: '{value}°'
        },
        accessibility: {
            rangeDescription: ''
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x}: {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""


def app():
    wp = jp.QuasarPage()

    hc = jp.HighCharts(a=wp, options=chart_def)

    hc.options.xAxis.categories = list(month_average.index)
    cur_data = list(month_average['Rating'])
    cur_data.append(cur_data * 2)
    cur_data.append(cur_data * 3)
    hc.options.series[0].data = cur_data

    return wp


jp.justpy(app)
