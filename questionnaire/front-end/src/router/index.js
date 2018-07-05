import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Register from '@/components/Register'
import Login from '@/components/Login'
import CreQues from '@/components/CreateQUestionnaire'
import createTitle from '@/components/children/createTitle'
import completion from '@/components/children/completion'
import multipleChoice from '@/components/children/multipleChoice'
import multipleLineText from '@/components/children/multipleLineText'
import singleChoice from '@/components/children/singleChoice'
import singleLineText from '@/components/children/singleLineText'
import preview from '@/components/preview'
import myQuestionnaire from '@/components/MyQuestionnaire'
import Answer from '@/components/Answer'
import AnswerSuccess from '@/components/AnswerSuccess'
import Analysis from '@/components/Analysis'

Vue.use(Router)
export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/home',
      name: 'Home',
      component: Home
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/myQuestionnaire',
      name: 'myQuestionnaire',
      component: myQuestionnaire
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/answer/:id',
      name: 'Answer',
      component: Answer
    },
    {
      path: '/answerSuccess',
      name: 'Success',
      component: AnswerSuccess
    },
    {
      path: '/analysis/:id',
      name: 'Analysis',
      component: Analysis
    },
    {
      path: '/createQuestionnaire',
      name: 'CreQues',
      component: CreQues,
      children: [
        {
          path: '',
          name: 'createTitle',
          component: createTitle
        },
        {
          path: 'createTitle/:id',
          name: 'createTitle',
          component: createTitle
        },
        {
          path: 'completion/:id',
          name: 'completion',
          component: completion
        },
        {
          path: 'multipleChoice/:id',
          name: 'multipleChoice',
          component: multipleChoice
        },
        {
          path: 'multipleLineText/:id',
          name: 'multipleLineText',
          component: multipleLineText
        },
        {
          path: 'singleChoice/:id',
          name: 'singleChoice',
          component: singleChoice
        },
        {
          path: 'singleLineText/:id',
          name: 'singleLineText',
          component: singleLineText
        },
        {
          path: '/preview/:id',
          name: 'preview',
          component: preview
        },
      ]
    }
  ]
})
