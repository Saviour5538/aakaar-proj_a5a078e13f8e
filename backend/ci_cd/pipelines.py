import os
import sys
from jenkins import Jenkins

# Jenkins server connection details
JENKINS_URL = 'http://localhost:8080'
JENKINS_USERNAME = 'your_username'
JENKINS_PASSWORD = 'your_password'

# Connect to Jenkins server
jenkins = Jenkins(JENKINS_URL, username=JENKINS_USERNAME, password=JENKINS_PASSWORD)

# Define pipeline
def create_pipeline(pipeline_name, pipeline_config):
    try:
        # Create pipeline
        jenkins.create_job(pipeline_name, pipeline_config)
        print(f'Pipeline {pipeline_name} created successfully')
    except Exception as e:
        print(f'Error creating pipeline {pipeline_name}: {str(e)}')

# Define pipeline configuration
pipeline_config = '''
<project>
    <actions/>
    <description/>
    <keepDependencies>false</keepDependencies>
    <properties>
        <hudson.model.ParametersDefinitionProperty>
            <parameterDefinitions>
                <hudson.model.StringParameterDefinition>
                    <name>BRANCH</name>
                    <description/>
                    <defaultValue>main</defaultValue>
                </hudson.model.StringParameterDefinition>
            </parameterDefinitions>
        </hudson.model.ParametersDefinitionProperty>
    </properties>
    <scm class="hudson.scm.NullSCM"/>
    <canRoam>true</canRoam>
    <disabled>false</disabled>
    <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
    <triggers/>
    <concurrentBuild>false</concurrentBuild>
    <builders>
        <hudson.tasks.Shell>
            <command>python backend/app.py</command>
        </hudson.tasks.Shell>
    </builders>
    <publishers/>
    <buildWrappers/>
</project>
'''

# Create pipeline
create_pipeline('my_pipeline', pipeline_config)