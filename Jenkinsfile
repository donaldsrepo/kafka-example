CODE_CHANGES = true
pipeline {
  agent any
  parameters {
    choice(name: 'VERSION', choices: ['1.1','1.2'], description: 'pick a version')
    booleanParam(name: 'executeTests', defaultValue: true, description: 'choose to execute the tests stage')
  }
  environment {
    NEW_VERSION = '1.3'
    TEST_PIPELINE = credentials('donaldsrepo')
  }
  stages {
    stage("init") { 
      steps {
	      script {
		      gv = load "script.groovy"
		    }
      }
    }
    stage("build") { 
      when {
        expression {
          BRANCH_NAME == 'dev' && CODE_CHANGES == true
        }
      }
      steps {
	      script {
		      gv.buildApp()
		    }
        echo "building version ${NEW_VERSION}"
      }
    }
    stage("test") {
      when {
        expression {
          params.executeTests == true
        }
      }
      steps {
        echo "testing"
      }
    }
    stage("deploy") {
      steps {
        //echo "deploying"
        echo "deploying version ${params.VERSION} using credentials ${TEST_PIPELINE}"
      }
    }
  }
}
