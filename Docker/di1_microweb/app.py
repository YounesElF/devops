from flask import Flask, render_template, request

microweb_app = Flask(__name__)

@microweb_app.route("/")
def main():
    # Render de HTML template
    return render_template("index.html")

if __name__ == "__main__":
    # host="0.0.0.0" maakt het bereikbaar vanaf andere machines (bv. host -> VM)
    # port=5050 zoals vaak in DevNet labs
    microweb_app.run(host="0.0.0.0", port=5050, debug=True)

