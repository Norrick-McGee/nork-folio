from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def portfolio():
    projects = [
        {
            'name': 'Project 1',
            'description': 'Description for project 1',
            'url': 'https://github.com/norrick-mcgee/project1'
        },
        {
            'name': 'Project 2',
            'description': 'Description for project 2',
            'url': 'https://github.com/norrick-mcgee/project2'
        },
        {
            'name': 'Project 3',
            'description': 'Description for project 3',
            'url': 'https://github.com/norrick-mcgee/project3'
        }
    ]
    return render_template('portfolio.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)

