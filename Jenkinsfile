
pipeline {

    agent {
        label 'linux-agent'
    }

    options {
        skipDefaultCheckout()
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code'
                checkout scm

                sh '''
                    echo "===== CHECKOUT DETAILS ====="
                    git log -1 --oneline
                    ls -la
                '''
            }
        }

        stage('Build') {
            steps {
                echo 'Building application'

                sh '''
                    mkdir -p build
                    cp app/index.html build/

                    echo "===== BUILD OUTPUT ====="
                    ls -l build/
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Testing application'

                sh '''
                    test -f build/index.html

                    grep -q "Hello from Jenkins Pipeline" build/index.html

                    echo "Application test successful"
                '''
            }
        }

        stage('Package') {
            steps {
                echo 'Packaging application'

                sh '''
                    tar -czf application.tar.gz build/

                    echo "===== PACKAGE DETAILS ====="
                    ls -lh application.tar.gz

                    tar -tzf application.tar.gz
                '''
            }
        }

        stage('Archive') {
            steps {
                archiveArtifacts(
                    artifacts: 'application.tar.gz',
                    fingerprint: true
                )
            }
        }
    }

    post {
        success {
            echo 'CI Pipeline completed successfully!'
        }

        failure {
            echo 'CI Pipeline failed!'
        }

        always {
            echo 'Pipeline execution finished.'
        }
    }
}
