from flask import Flask, render_template, session, redirect,url_for
from form import Frank_hertzForm, set_Frank_hertzForm, Frank_hertzForm_1, set_Frank_hertzForm_1,Frank_hertzForm_2, set_Frank_hertzForm_2,Frank_hertzForm_3,set_Frank_hertzForm_3
from form import Frank_hertzForm_4, set_Frank_hertzForm_4
from bokeh.plotting import figure, output_file, show
from Latexlabel import LatexLabel

app = Flask(__name__)
app.config['SECRET_KEY'] = 'guess'


@app.route('/', methods=['GET', 'POST'])
def index():
    point_num = 161
    set_Frank_hertzForm_1(point_num)
    set_Frank_hertzForm_2(point_num)
    set_Frank_hertzForm_3(point_num)
    set_Frank_hertzForm_4(point_num)
    form1 = Frank_hertzForm_1()
    form2 = Frank_hertzForm_2()
    form3 = Frank_hertzForm_3()
    form4 = Frank_hertzForm_4()
    y_label = LatexLabel(text="V_{G2K}/V",x=390, y=17, x_units='screen', y_units='screen',
                       render_mode='css', text_font_size='10pt')
    x_label = LatexLabel(text="I_A/{\mu}A", x=20, y=480, x_units='screen', y_units='screen',
                         render_mode='css', text_font_size='10pt')

    if form1.submit1.data and form1.validate_on_submit():
        print('inside submit1')
        x = []
        y = []
        for i in range(point_num):
            point = getattr(form1,'form1_point_'+str(i),None)
            if point is not None:
                # session['point_'+str(i)] = point.data
                # print(session)
                y.append(point.data)
                x.append(i/2)
        print(x)
        print(y)
        session['form1'] = y
        session['legend1'] = form1.name1.data
        output_file("Frank_hertzForm_plot.html", title="弗兰克-赫兹实验曲线")
        p = figure(title="F-H实验曲线", plot_width = 600, plot_height = 600,min_border_left = 60, min_border_bottom = 60)
        p.title.align = 'center'
        p.title.text_font_size = "25px"
        p.line(x, y, legend = form1.name1.data, line_width = 2)
        p.add_layout(y_label, 'below')
        p.add_layout(x_label,'left')
        p.legend.location = "top_left"
        show(p)

    if form2.submit2.data and form2.validate_on_submit():
        print('inside submit2')
        x = []
        y2 = []
        legend1 = session['legend1']
        if 'form1' not in session:
            y1 = []
        else:
            y1 = session['form1']
            print(y1)

        for i in range(point_num):
            getattr(form1, 'form1_point_' + str(i), None).data = y1[i]
            point2 = getattr(form2, 'form2_point_' + str(i), None)
            print(getattr(form1, 'form1_point_' + str(i), None).data)
            if point2 is not None:
                y2.append(point2.data)
                x.append(i / 2)
        getattr(form1, 'name1', None).data = legend1
        session['form2'] = y2
        session['legend2'] = form2.name2.data
        output_file("Frank_hertzForm_plot.html", title="弗兰克-赫兹实验曲线")
        p = figure(title="F-H实验曲线")
        p.title.align = 'center'
        p.title.text_font_size = "25px"
        p.line(x, y1, legend = legend1, line_width=2)
        p.line(x, y2, legend= form2.name2.data, line_width=2, line_color="red")
        p.add_layout(y_label, 'below')
        p.add_layout(x_label, 'left')
        p.legend.location = "top_left"
        show(p)

    if form3.submit3.data and form3.validate_on_submit():
        print('inside submit3')
        x = []
        y1 = session['form1']
        y2 = session['form2']
        legend1 = session['legend1']
        legend2 = session['legend2']
        y3 = []

        for i in range(point_num):
            getattr(form1, 'form1_point_' + str(i), None).data = y1[i]
            getattr(form2, 'form2_point_' + str(i), None).data = y2[i]
            point3 = getattr(form3, 'form3_point_' + str(i), None)
            print(getattr(form3, 'form3_point_' + str(i), None).data)
            if point3 is not None:
                y3.append(point3.data)
                x.append(i / 2)
        getattr(form1, 'name1', None).data = legend1
        getattr(form2, 'name2', None).data = legend2
        session['form3'] = y3
        session['legend3'] = form3.name3.data
        output_file("Frank_hertzForm_plot.html", title="弗兰克-赫兹实验曲线")
        p = figure(title="F-H实验曲线")
        p.title.align = 'center'
        p.title.text_font_size = "25px"
        p.line(x, y1, legend= legend1, line_width=2)
        p.line(x, y2, legend= legend2, line_width=2, line_color="red")
        p.line(x, y3, legend= form3.name3.data, line_width=2, line_color="green")
        p.add_layout(y_label, 'below')
        p.add_layout(x_label, 'left')
        p.legend.location = "top_left"
        show(p)

    if form4.submit4.data and form4.validate_on_submit():
        print('inside submit4')
        x = []
        y1 = session['form1']
        y2 = session['form2']
        y3 = session['form3']
        legend1 = session['legend1']
        legend2 = session['legend2']
        legend3 = session['legend3']
        y4 = []

        for i in range(point_num):
            getattr(form1, 'form1_point_' + str(i), None).data = y1[i]
            getattr(form2, 'form2_point_' + str(i), None).data = y2[i]
            getattr(form3, 'form3_point_' + str(i), None).data = y3[i]
            point4 = getattr(form4, 'form4_point_' + str(i), None)
            print(getattr(form4, 'form4_point_' + str(i), None).data)
            if point4 is not None:
                y4.append(point4.data)
                x.append(i / 2)
        getattr(form1, 'name1', None).data = legend1
        getattr(form2, 'name2', None).data = legend2
        getattr(form3, 'name3', None).data = legend3
        output_file("Frank_hertzForm_plot.html", title="弗兰克-赫兹实验曲线")
        p = figure(title="F-H实验曲线")
        p.title.align = 'center'
        p.title.text_font_size = "25px"
        p.line(x, y1, legend= legend1, line_width=2)
        p.line(x, y2, legend= legend2, line_width=2, line_color="red")
        p.line(x, y3, legend= legend3, line_width=2, line_color="green")
        p.line(x, y4, legend= form4.name4.data, line_width=2, line_color="black")
        p.add_layout(y_label, 'below')
        p.add_layout(x_label, 'left')
        p.legend.location = "top_left"
        show(p)
        # return redirect(url_for('index'))
    return render_template('Frank_Hertz_experiment_plot.html', form1=form1, form2 = form2, form3 = form3, form4 = form4)
    # return render_template('temp.html', form1=form1, form2=form2, point_num=point_num)


if __name__ == '__main__':
    app.run()
    # class Test(object):
    #     a = 1
    #     b =2
    # t = Test()
    # a = getattr(t, 'a', 3)
    # c = getattr(t, 'c', 3)
    # print(a)
    # print(c)