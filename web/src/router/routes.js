/*
 * @Author: wanqqq29
 * @Date: 2022-02-28 11:15:41
 * @LastEditTime: 2022-03-04 15:12:44
 * @LastEditors: wanqqq29
 * @Description: blog.wanqqq29.cn
 * @FilePath: \web\src\router\routes.js
 */

const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', name:'index',component: () => import('pages/Index.vue') },
      { path: '/result', name:'result',component: () => import('pages/Result.vue') },
      { path: '/end', name:'end',component: () => import('pages/end.vue') },

    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
