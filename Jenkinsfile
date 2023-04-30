CODE_CHANGES = true
pipeline {
  agent any
  tools {
    // add any tools to build your apps, such as maven, gradle and jdk
  }
  environment {
    NEW_VERSION = '1.3'
    TEST_PIPELINE = credentials('test-pipeline')
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
      when {
        expression {
          BRANCH_NAME == 'dev' || BRANCH_NAME = 'master'
        }
      }
      steps {
        echo "testing"
      }
    }
    stage("deploy") {
      steps {
        echo "deploying"
        echo "deploying with ${TEST_PIPELINE}"
        // sh "scriptname {TEST_PIPELINE}"
      }
    }
  }
  post {
    always {
      //
    }
    success {
      //
    }
    failure {
      //
    }
  }
}
