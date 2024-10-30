pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat '''
                    envi\\Scripts\\activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Django Tests') {
            steps {
                bat '''
                    envi\\Scripts\\activate
                    cd master_project
                    python manage.py test
                '''
            }
        }

        stage('Start Django Development Server') {
            steps {
                bat '''
                    envi\\Scripts\\activate
                    cd master_project
                    python manage.py runserver 0.0.0.0:8000
                '''
            }
        }
    }
}
