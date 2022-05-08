import justpy as jp
import pandas as pd

data = pd.read_csv('./data/reviews.csv', parse_dates=["Timestamp"])
data['Month'] = data['Timestamp'].dt.strftime("%Y-%m")
month_average_crs = data.groupby(["Month", 'Course Name'])[
    'Rating'].mean().unstack()

# temp = list(month_average_crs.columns)[0]
# print("month_average_crs", month_average_crs[temp])


chart_def = """
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average Rating for course by month'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: false,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Fruit units'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ''
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}
"""


def app():
    wp = jp.QuasarPage()
    jp.QDiv(a=wp, text="Analysis of course Reviews",
            classes="text-h3 text-center q-pa-lg")
    jp.QDiv(
        a=wp, text="These graphs represent course review analysis", classes="text-body1")

    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.xAxis.categories = list(month_average_crs.index)

    # hc_data = list()
    # for column in list(month_average_crs.columns):
    #     cur_data = list(month_average_crs[column])
    #     hc_data.append({"name": column, "data": cur_data})

    # hc_data = [{"name": v1, "data": list(month_average_crs[v1])}
    #            for v1 in list(month_average_crs.columns)]

    hc_data = [{"name": v1, "data": [v2 for v2 in month_average_crs[v1]]}
               for v1 in month_average_crs.columns]

    hc.options.series = hc_data

    return wp


jp.justpy(app)
