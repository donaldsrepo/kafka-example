pipeline {
  agent any
  environment {
    NEW_VERSION = '1.3'
    TEST_PIPELINE = credentials('test-pipeline')
  }
  stages {
    stage("build") {
      steps {
        echo "building"
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
