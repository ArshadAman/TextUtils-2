from flask import Flask, render_template, request


# Initalising the app
app = Flask(__name__)


# Making Routes
@app.route('/', methods=['GET', 'POST'])
def home__page():
    formatted_string = ''
    input_str = ''
    if request.method == 'POST':
        input_str = request.form['input']
        options = request.form.get('options')
        if options == 'upper':
            formatted_string+=input_str.upper()
        elif options == 'lower':
            formatted_string+=input_str.lower()
        elif options == 'capitalise':
            formatted_string+=input_str.capitalize()
        elif options == 'rem-punc':
            punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            new_str = ''
            for i in input_str:
                if i not in punctuation:
                    new_str+=i
            formatted_string+=new_str
        elif options == 'rem-ex-space':
            splittedWords = input_str.split()
            new_str = " ".join(splittedWords)
            formatted_string+=new_str
        elif options == 'wcount':
            splittedWords = input_str.split()
            no_words = len(splittedWords)
            formatted_string += str(no_words)
        elif options == 'lcount':
            no_letters = len(input_str)
            formatted_string += str(no_letters)
    return render_template('index.html', output = formatted_string, input = input_str)


if __name__ == '__main__':
    app.run(debug=True)