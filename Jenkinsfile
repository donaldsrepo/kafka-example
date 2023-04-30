CODE_CHANGES = true
pipeline {
  agent any
  parameters {
    choice(name: 'VERSION', choices: ['1.1','1.2'], description: 'pick a version')
  }
  environment {
    NEW_VERSION = '1.3'
    //TEST_PIPELINE = credentials('test-pipeline')
  }
  stages {
    stage("build") { 
      when {
        expression {
          BRANCH_NAME == 'dev' && CODE_CHANGES == true
        }
      }
      steps {
        echo "building"
        echo "building version ${NEW_VERSION}"
      }
    }
    stage("test") {
      steps {
        echo "testing"
      }
    }
    stage("deploy") {
      steps {
        echo "deploying"
      }
    }
  }
}
