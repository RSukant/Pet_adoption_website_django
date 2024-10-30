pipeline {
    agent any

    stages {
        stage('Setup Virtual Environment') {
            steps {
                // Activate virtual environment and install dependencies
                sh 'envi/Scripts/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Django Tests') {
            steps {
                // Activate virtual environment and run tests
                sh 'envi/Scripts/activate && python manage.py test'
            }
        }

        stage('Start Django Development Server') {
            steps {
                // Activate virtual environment and start Django server
                sh 'envi/Scripts/activate && python manage.py runserver 0.0.0.0:8000'
            }
        }
    }
}
