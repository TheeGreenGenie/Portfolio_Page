from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/projects')
def projects():
    projects_list = [
        {
            'title': 'Project 1',
            'description': 'A first project description (To be filled)',
            'link': '#'
        },
        {
            'title': 'Project etc.',
            'description': 'Other Projects (To be filled)',
            'link': '#'
        }
    ]
    return render_template('projects.html', title='Projects', projects=projects_list)

@app.route('/contact')
def contact():
    contact_info = {
        'personal email': 'solomonshasanmi@gmail.com',
        'work email': 'Solomon.Shasanmi@Pennmedicine.upenn.edu',
        'Work Website': 'https://www.med.upenn.edu/afcri/afcri-cbio-high-school-summer-internship.html',
        'linkedin': 'https://www.linkedin.com/in/solomon-shasanmi-a38b32245',
        'github': 'https://github.com/TheeGreenGenie'
    }
    return render_template('contact.html', title='Contact', contact_info=contact_info)

if __name__ == '__main__':
    app.run(debug=True)