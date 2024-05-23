from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  button_labels = ["Button 1", "Button 2", "Button 3", "Button 4"]

  image_path = "map.png"
  return render_template("index.html", buttons=button_labels, image_path=image_path)

if __name__ == "__main__":
  app.run(debug=True)