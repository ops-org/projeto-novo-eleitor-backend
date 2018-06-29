node {

    agent {
        docker {
            image 'python:3.6'
        }
    }

    stages
    
    try {
        stage ('Clone') {
        	deleteDir()
            checkout scm
        }

        stage ('Build') {
        	sh "echo 'shell scripts to build project...'"
            sh 'docker images;'
            sh 'docker run --rm fedora echo "Hello World!"'
        }

        stage ('Tests') {
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

      	stage ('Deploy') {
            sh "echo 'shell scripts to deploy to server...'"
      	}

    } catch (err) {
        currentBuild.result = 'FAILED'
        throw err
    }
}
