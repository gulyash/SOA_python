from flask import Flask, render_template, request
import xmlrpc.client

app = Flask(__name__, template_folder='template')

ARR_LEN = 5


@app.route('/')
def homepage():
    form_data = {
        'answ': '',
        'answ2': ''
    }
    return render_template('home.html', title='Home', form_data=form_data)


@app.route('/', methods=['POST'])
def send_request():
    server = xmlrpc.client.ServerProxy('http://localhost:8000')

    form_data = {
        'answ': '',
        'answ2': ''
    }
    if request.form.get('my_first_service'):
        form_data['answ'] = server.my_first_service()
    if request.form.get('service_args'):
        num = int(request.form['tb_Num']) if request.form['tb_Num'] else ''
        str = request.form['tb_Str']
        field1 = request.form['tb_field1']
        field2 = request.form['tb_field2']
        arr = [request.form[f"tb_Arr{i}"] for i in range(ARR_LEN)]
        form_data['answ2'] = server.service_args(num, str, arr,
                                                  {
                                                      'field1': field1,
                                                      'field2': field2
                                                  }),
    return render_template('home.html', title='Home', form_data=form_data)


if __name__ == '__main__':
    app.run('localhost', 5000)
