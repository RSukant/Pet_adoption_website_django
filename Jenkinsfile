pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                // Activate virtual environment and install dependencies
                sh '. envi/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Django Tests') {
            steps {
                // Activate virtual environment and run tests
                sh '. envi/bin/activate && python manage.py test'
            }
        }

        stage('Start Django Development Server') {
            steps {
                // Activate virtual environment and start Django server
                sh '. envi/bin/activate && python manage.py runserver 0.0.0.0:8000'
            }
        }
    }
}
