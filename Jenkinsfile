pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                // Activate virtual environment and install dependencies
                bat 'envi\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Start Django Development Server') {
            steps {
                // Activate virtual environment and start Django server
                bat 'envi\\Scripts\\activate && cd master_project && python manage.py runserver 0.0.0.0:8000'
            }
        }
    }
}
