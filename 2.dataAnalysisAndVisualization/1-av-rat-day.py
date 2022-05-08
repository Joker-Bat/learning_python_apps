import justpy as jp
import pandas as pd

data = pd.read_csv("./data/reviews.csv", parse_dates=["Timestamp"])
data['Day'] = data['Timestamp'].dt.date
day_average = data.groupby(['Day']).mean()

chart_def = """
  {
    chart: {
        type: 'spline',
        inverted: true
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Altitude'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Temperature'
        },
        labels: {
            format: '{value}°'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
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
        name: 'Temperature',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""

# print(list(day_average['Rating']))


def app():
    wp = jp.QuasarPage()
    jp.QDiv(a=wp, text="Analysis of course Reviews",
            classes="text-h3 text-center q-pa-lg")
    jp.QDiv(
        a=wp, text="These graphs represent course review analysis", classes="text-body1")

    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.chart.inverted = False
    x = list(day_average.index)
    y = list(day_average['Rating'])
    hc.options.xAxis.categories = x
    hc.options.xAxis.title.text = "Date"
    hc.options.yAxis.title.text = "Average Rating"
    hc.options.series[0].data = y
    hc.options.series[0].name = "Average Rating"

    # print(hc.options)
    # print(type(hc.options))
    return wp


jp.justpy(app)
