pipeline{
    agent any
    stages{
        stage("Create Virtual Environment"){
            steps{
                sh "python3.7 -m venv venv"
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
        stage("Activate Virtual Envrionment"){
            steps{
                sh "source /venv/bin/activate"
            }
            post{
                always{
                    echo "Activation of virtual envrionment completed"
                }
                success{
                    echo "Activated virtual envrionment"
                }
                failure{
                    echo "Fialed to activate virtual envrionment"
                }
            }
        }
        stage("Activate Virtual Envrionment"){
            steps{
                sh "pip3.7 install -r requirements.txt"
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