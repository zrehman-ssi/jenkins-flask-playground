pipeline{
    agent { 
		docker { 
			image 'python:3.7.4' 
		} 
	}
    stages{
        stage("Create Virtual Environment"){
            steps{
                sh "python3.7 -m venv venv"
				sh "python3.7 --version"
				sh "venv/bin/activate/pip3.7 install -r requirements.txt"
				
            }
            post{
                always{
                    echo "Virtual environment step competed"
                }
                success{
                    echo "Virtual environment created"
                }
                failure{
                    echo "Virtual environment failed"
                }
            }
        }
        stage("Install Dependencies Envrionment"){
            steps{
                sh "venv/bin/activate/pip3.7 install -r requirements.txt"
                sh "venv/bin/activate/python3.7 -m compileall -f ."
            }
            post{
                always{
                    echo "Requirements installation completed"
                }
                success{
                    echo "Requirements installed successfully."
                }
                failure{
                    echo "Fialed to install requirements from requirements.txt"
                }
            }
        }
    }
    post{
        always{
            echo "========always========"
        }
        success{
            echo "========pipeline executed successfully ========"
        }
        failure{
            echo "========pipeline execution failed========"
        }
    }
}