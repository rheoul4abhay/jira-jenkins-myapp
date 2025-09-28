properties([
    pipelineTriggers([
        githubPush()
    ])
]

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
		    sudo docker build -t my-flask-app .
		    sudo docker run -d -p 5000:5000 my-flask-app
		'''
            }
        }
    }
}
