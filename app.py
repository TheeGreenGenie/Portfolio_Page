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
            'title': 'Vocalytics',
            'description': 'Application that takes in video input from user and gives tips on how to improve how they talk. Made for MorganHacks 2025 and won 2nd place overall. Shows proficiency in Opencv, Python, Video-analysis, & Live updating',
            'link': 'https://devpost.com/software/vocalytics-rqogdn'
        },
        {
            'title': 'CoviDash',
            'description': 'Covid Dashboard utilizing APIs to serve live data to a website. Project Demonstrates proficiency in Flask, Javascript, Python, & Live server deployment',
            'link': 'https://covidash.onrender.com'
        },
        {
            'title': 'Weather App',
            'description': 'Simple weather app. Displays the current weather of whatever city you enter. Project demonstrates proficiency in APIs, Flask, and Python, & Live server deployment',
            'link': 'https://my-weather-fxec.onrender.com/'
        },
        {
            'title': 'Blob-Bros',
            'description': 'Pygame platformer based on Mario-Bros. Project Demonstrates proficiency in OOP, Python, & 2d Physics',
            'link': 'https://github.com/TheeGreenGenie/Blob-Bros'
        },
        {
            'title': 'Expense Tracker',
            'description': 'Simple Expense Tracker which runs in the command line. This project shows proficiency in Python, CLI navigation, & Cross-platform integration',
            'link': 'https://github.com/TheeGreenGenie/ExpenseTracker'
        },
        {
            'title': 'Image Filter',
            'description': 'Image filtering application, make simple edits to a photo. This project shows proficiency in Python, especially using Numpy, Pillow, & GUIs (tkinter)',
            'link': 'https://github.com/TheeGreenGenie/Image_Filter'
        },
        {
            'title': 'To Do',
            'description': 'To do list function working in the command line. This project shows proficiency in CLI interaction, Python, & Json logging',
            'link': 'https://github.com/TheeGreenGenie/Image_Filter'
        },
        {
            'title': 'FinU',
            'description': 'Finance application made for HopHacks 2024. This project shows proficiency in Django, Python, and Finance APIs',
            'link': 'https://github.com/TheeGreenGenie/HopHacksProject'
        },
        {
            'title': 'Vireo',
            'description': 'Natural disaster web application made for MorganHacks 2024. This project shows proficiency in Teamwork, Streamlit, & User Interaction',
            'link': 'https://github.com/RobelK1738/Vireo'
        }
    ]
    return render_template('projects.html', title='Projects', projects=projects_list)

@app.route('/contact')
def contact():
    contact_info = {
        'pEmail': 'solomonshasanmi@gmail.com',
        'wEmail': 'Solomon.Shasanmi@Pennmedicine.upenn.edu',
        'wWebsite': 'https://www.med.upenn.edu/afcri/afcri-cbio-high-school-summer-internship.html',
        'linkedin': 'https://www.linkedin.com/in/solomon-shasanmi-a38b32245',
        'github': 'https://github.com/TheeGreenGenie'
    }
    return render_template('contact.html', title='Contact', contact_info=contact_info)

if __name__ == '__main__':
    app.run(debug=True)