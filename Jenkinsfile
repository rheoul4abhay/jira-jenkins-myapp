properties([
    pipelineTriggers([
        githubPush()
    ])
])

pipeline {

    agent {
        label 'docker-node'
    }
    stages {
        stage('Build') {
	    when {
	        anyOf {
		    branch 'main'
		    branch pattern: "feature/JW-[0-9]+.*", comparator: "REGEXP"
		}
	    }
            steps {
                echo "Building application on branch ${env.BRANCH_NAME}"
		sh '''
		    sudo docker rm -f flask-app-container || true
		    sudo docker build -t my-flask-app .
		'''
            }
        }
	stage('Deploy') {
	    when {
		anyOf {
		    branch 'main'
		    branch pattern: "feature/JW-[0-9]+.*", comparator: "REGEXP"
		}
	    }
	    steps {
		echo "Deploying Flask app on branch ${env.BRANCH_NAME}"
		sh '''
		    sudo docker run -d --name flask-app-container -p 5000:5000 my-flask-app
		'''
	    }
	}
    }
}
