from flask import Flask, Response,json
from flask import render_template
import subprocess,traceback,sys

app = Flask(__name__)

@app.route('/')
def say_hello():
	return render_template('index.html')

@app.route('/<string:switch_group_name>/<string:switch_name>/<string:stateCode>', methods=['GET', 'POST'])
def hello_world(switch_group_name=None,switch_name=None,stateCode=None):
    #switch_group_name, switch_name etc for future use

    l_status=200
    try:
        proc = subprocess.check_output(['/home/pi/projects/rfoutlet/codesend',stateCode], stderr=subprocess.STDOUT)
        l_status=200
    except subprocess.CalledProcessError:
        # There was an error - command exited with non-zero code
        print ("There was an issue which threw CalledProcessError")
        l_status=400
    except :
        print ("There was an issue -not totally sure of the flavor!")
        traceback.print_exc(file=sys.stdout)
        l_status=400
    #*


    resp = Response(status=l_status)

    return resp

