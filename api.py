import flask
from flask import jsonify, request
from ck2l import get_recepy_dict

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET"])
def home():
    return """
<html>
   <body>
      <form action = "http://localhost:5000/recepy" method = "post">
         <p>Enter Chefkoch url:</p>
         <p><input type = "text" name = "url" /></p>
         <p><input type = "submit" value = "submit" /></p>
      </form>   
   </body>
</html>
    """

@app.route("/recepy", methods=["POST"])
def get_recepy():
    url = request.form["url"]

    recepy = get_recepy_dict(url)
    return jsonify(recepy)
    
app.run()
