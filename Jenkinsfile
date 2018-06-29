pipeline {
    agent {
        docker {
            image 'python:3.6'
        }
    }

    stages {

        stage ('Prepare Environment') {
            steps {
                sh 'pip3 install pipenv --user';
            }
        }
  
        stage ('Clone') {
            steps {
        	    deleteDir()
                checkout scm
            }
        }

        stage ('Build') {
            steps {
        	    sh "echo 'shell scripts to build project...'"
                sh 'docker images;'
                sh 'docker run --rm fedora echo "Hello World!"'
            }
        }

        stage ('Tests') {
	        steps {
                parallel 'static': {
                    sh "echo 'shell scripts to run static tests...'"
                },
                'unit': {
                    sh "echo 'shell scripts to run unit tests...'"
                },
                'integration': {
                    sh "echo 'shell scripts to run integration tests...'"
                }
            }
        }

      	stage ('Deploy') {
            steps {
                sh "echo 'shell scripts to deploy to server...'"
            }
      	}
    }
}
