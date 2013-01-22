# -*- encoding: utf-8 -*-

import bottle

app = bottle.default_app()

@app.route('/', method='GET')
@app.route('/greet/<name:re:[a-z]+>', method='GET')
def greet(name='world'):
    res = {}
    res['status'] = 'OK'
    res['result'] = 'Hello %s' % name

    return res


@app.route('/fibonacci', method='POST')
def fibonacci():
    res = {}
    steps = bottle.request.forms.steps

    try:
        steps = int(steps)
        fib = Fibonacci(steps)
        seq = fib.calculate()
        res['status'] = 'OK'
        res['result']={}
        res['result']['sequence'] = [n for n in seq]

    except Exception as e:
        res['status'] = 'Error'
        res['message'] = '%s' % e

    return res


class Fibonacci(object):
    def __init__(self, steps):
        self.a = 0
        self.b = 1
        self.index = 0
        self.steps = steps

    def calculate(self):
        if self.steps > 0:
            if self.steps == 1:
                yield self.a
            else:
                yield self.a
                yield self.b
                self.index = self.index + 2
                while self.index < self.steps:
                    self.a, self.b = self.b, self.a + self.b
                    self.index = self.index + 1
                    yield self.b
        else:
            raise Exception('\'steps\' must be an integer >= 0')


if __name__ == '__main__':
    bottle.run(app, host='localhost', port=5000, debug=True, reloader=True)
