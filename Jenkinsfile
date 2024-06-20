node {
    
    stage('Git Checkin') 
    {
        git 'https://github.com/rohioffl/cicd-pipeline.git'
    }
    
    stage('Sending Github files to docker-instance') 
    {
        sshagent(['docker-instance']) 
        {
            sh 'ssh -o StrictHostKeyChecking=no ubuntu@172.31.15.167'
            sh 'scp -r /var/lib/jenkins/workspace/flask-app/* ubuntu@172.31.15.167:/home/ubuntu/flask/'
        }
        
    }
    
    stage('Building docker image') 
    {
        sshagent(['docker-instance']) 
        {
            sh 'ssh -o StrictHostKeyChecking=no ubuntu@172.31.15.167 "cd /home/ubuntu/flask && docker build -t flask-app . "'
        }
    }
    stage('Tagging docker images') 
    {
        sshagent(['docker-instance']) 
        {
            sh 'ssh -o StrictHostKeyChecking=no ubuntu@172.31.15.167 "docker tag flask-app rohioffl/flask_app:latest && docker tag flask-app rohioffl/flask_app:v1.$BUILD_ID"'
        }
    }
    
    stage('Pusing docker image to docker-hub')
    {
        sshagent(['docker-instance']) 
        {
            withCredentials([string(credentialsId: 'dockhub', variable: 'pwd')]) 
            {
                sh "ssh -o StrictHostKeyChecking=no ubuntu@172.31.15.167 docker login -u rohioffl -p ${pwd}"
                sh 'ssh -o StrictHostKeyChecking=no ubuntu@172.31.15.167 "docker push rohioffl/flask_app:v1.${BUILD_ID} && docker push rohioffl/flask_app:latest"'
            }
        }    
            
    }
    stage('Apply k8s playbook') 
    {
        sshagent(['docker-instance']) 
        {
            sh 'ssh -o StrictHostKeyChecking=no ubuntu@172.31.15.167 ansible-playbook /home/ubuntu/flask/deploy.yaml'

        }    
            
    }
}