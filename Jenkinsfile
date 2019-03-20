#!groovy

pipeline {

  agent {
    label 'node'
  }

  options {

    // General Jenkins job properties
    buildDiscarder(logRotator(numToKeepStr:'20'))

    // Declarative-specific options
    skipDefaultCheckout()

    // "wrapper" steps that should wrap the entire build execution
    timeout(time: 240, unit: 'MINUTES')
  }

  stages {

    // --- BUILD ---
    stage('Build') {
      agent {
        label 'node'
      }
      steps {
        deleteDir()
        checkout scm
        sh 'make build'
      }
    }

    // -- UNIT TESTS ---
    stage('Unit Tests') {
      agent {
        label 'node'
      }
      steps {
        deleteDir()
        sh 'make build'
        sh 'make test'
      }
    }

  }

  post {
    success {
      slackSend (
        color: 'good',
        message: "SUCCESS: #${env.BUILD_NUMBER} ${env.JOB_NAME} (${env.BUILD_URL})"
      )
    }
    failure {
      slackSend (
        color: 'danger',
        message: "FAILURE: #${env.BUILD_NUMBER} ${env.JOB_NAME} (${env.BUILD_URL})"
      )
    }
    unstable {
      slackSend (
        color: 'warning',
        message: "UNSTABLE: #${env.BUILD_NUMBER} ${env.JOB_NAME} (${env.BUILD_URL})"
      )
    }
    aborted {
      slackSend (
        color: 'danger',
        message: "ABORTED: #${env.BUILD_NUMBER} ${env.JOB_NAME} (${env.BUILD_URL})"
      )
    }
  }
}
