pipeline{
    agent any
    stages{
        stage("Create Virtual Environment"){
            steps{
                bat 'echo %PATH%'
                cmd python -m venv venv
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
                cmd /venv/Scripts/activate
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
                cmd pip install -r requirements.txt
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