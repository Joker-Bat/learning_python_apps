import justpy as jp
import pandas as pd

data = pd.read_csv('./data/reviews.csv', parse_dates=['Timestamp'])
data['Weekday'] = data['Timestamp'].dt.strftime("%A")
data['Daynumber'] = data['Timestamp'].dt.strftime("%w")

weekday_average = data.groupby(['Weekday', 'Daynumber']).mean()
weekday_average = weekday_average.sort_values('Daynumber')
# weekday_average.index.get_level_values(0)

print(list(weekday_average['Rating']))


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
            text: 'Average Ratings'
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
    hc = jp.HighCharts(a=wp, options=chart_def)

    hc.options.xAxis.categories = list(
        weekday_average.index.get_level_values(0))
    hc.options.series = [
        {"name": "Ratings", "data": list(weekday_average['Rating'])}]

    return wp


jp.justpy(app)
