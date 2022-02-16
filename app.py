from flask import Flask, render_template, request, flash


### Conversion Function ###
def function(string):
  
  final_list = []
  
  initial_list = string.split(' ')
  
  cleaned_list = []
  
  for string in initial_list:
    if (string != ''):
      cleaned_list.append(string)

  for word in cleaned_list:
    for i in range(len(word)):
      if (i % 2 != 0):
        new_char = word[i].upper()
      else:
        new_char = word[i].lower()
      final_list.append(new_char)
    final_list.append(' ')

  return ''.join(final_list[:-1])



app = Flask(__name__)
app.secret_key = "attackoftheworms305"

@app.route("/")
def index():
	flash("")
	return render_template("index.html")


@app.route("/result", methods=["POST", "GET"])
def convert():
	flash(function(str(request.form['input_text'])))
	return render_template("index.html")
