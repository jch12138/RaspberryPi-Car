from flask import render_template
from flask import redirect
from . import main
from .car import Car
from .steer import Steer

car = Car(11, 12, 13, 15)
steer = Steer(38,40)

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/control/<string:action_name>')
def action(action_name):
    if action_name == 'forward':
        print('forward')
        car.forward()
    elif action_name == 'backward':
        print('backward')
        car.backward()
    elif action_name == 'right':
        print('right')
        car.go_right()
    elif action_name == 'left':
        print('left')
        car.go_left()
    else:
        print('stop')
        car.stop()
    return action_name


@main.route('/action')
def action_stream():
    return redirect('http://192.168.0.102:8080/?action=stream')


@main.route('/camera/<string:action_name>')
def camera(action_name):
    if action_name == 'camera_up':
        print('camera_up')
        steer.increase_angle2()
    elif action_name == 'camera_down':
        print('camera_down')
        steer.reduce_angle2()
    elif action_name == 'camera_right':
        print('camera_right')
        steer.increase_angle1()
    elif action_name == 'camera_left':
        print('camera_left')
        steer.reduce_angle1()
    else:
        print('nothing to do')
    return action_name

