import justpy as jp


def app():
    wp = jp.QuasarPage()
    jp.QDiv(a=wp, text="Analysis of course Reviews",
            classes="text-h3 text-center q-pa-lg")
    jp.QDiv(
        a=wp, text="These graphs represent course review analysis", classes="text-body1")
    return wp


jp.justpy(app)
