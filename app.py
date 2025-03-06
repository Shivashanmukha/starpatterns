# app.py
from flask import Flask, request, render_template

app = Flask(__name__)

# Define star patterns for letters
letter_patterns = {
    'A': ["  *  ", " * * ", "*****", "*   *", "*   *"],
    'B': ["**** ", "*   *", "**** ", "*   *", "**** "],
    'C': [" ****", "*    ", "*    ", "*    ", " ****"],
    'D': ["**** ", "*   *", "*   *", "*   *", "**** "],
    'E': ["*****", "*    ", "**** ", "*    ", "*****"],
    'F': ["*****", "*    ", "**** ", "*    ", "*    "],
    'G': [" ****", "*    ", "* ***", "*   *", " ****"],
    'H': ["*   *", "*   *", "*****", "*   *", "*   *"],
    'I': [" *** ", "  *  ", "  *  ", "  *  ", " *** "],
    'J': ["   **", "    *", "    *", "*   *", " *** "],
    'K': ["*   *", "*  * ", "***  ", "*  * ", "*   *"],
    'L': ["*    ", "*    ", "*    ", "*    ", "*****"],
    'M': ["*   *", "** **", "* * *", "*   *", "*   *"],
    'N': ["*   *", "**  *", "* * *", "*  **", "*   *"],
    'O': [" ****", "*    *", "*    *", "*    *", " ****"],
    'P': ["**** ", "*   *", "**** ", "*    ", "*    "],
    'Q': [" ****", "*    *", "*    *", "*  * *", " **** *"],
    'R': ["**** ", "*   *", "**** ", "* *  ", "*  * "],
    'S': [" ****", "*    ", " ****", "    *", " ****"],
    'T': ["*****", "  *  ", "  *  ", "  *  ", "  *  "],
    'U': ["*   *", "*   *", "*   *", "*   *", " ****"],
    'V': ["*   *", "*   *", "*   *", " * * ", "  *  "],
    'W': ["*   *", "*   *", "* * *", "* * *", " * * "],
    'X': ["*   *", " * * ", "  *  ", " * * ", "*   *"],
    'Y': ["*   *", " * * ", "  *  ", "  *  ", "  *  "],
    'Z': ["*****", "   * ", "  *  ", " *   ", "*****"],
    # Add patterns for other letters as needed
}

@app.route('/', methods=['GET', 'POST'])
def index():
    patterns = {}
    word = ""
    if request.method == 'POST':
        word = request.form['word'].upper()  # Convert to uppercase for consistency
        for letter in word:
            if letter in letter_patterns:
                patterns[letter] = letter_patterns[letter]
    
    return render_template('app.html', patterns=patterns, word=word)

if __name__ == '__main__':
    app.run(debug=True)