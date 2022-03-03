<!--
 * @Author: wanqqq29
 * @Date: 2022-02-28 11:15:41
 * @LastEditTime: 2022-03-01 15:39:44
 * @LastEditors: wanqqq29
 * @Description: blog.wanqqq29.cn
 * @FilePath: \web\src\layouts\MainLayout.vue
-->
<template>
  <q-layout view="hHh lpR fFf" style="background: linear-gradient(90deg, rgba(106, 17, 203, 1) 0%, rgba(37, 117, 252, 1) 100%);">

    <q-page-container>
      <router-view />
    </q-page-container>

  </q-layout>
</template>

<script>

import { defineComponent, ref } from 'vue'

export default defineComponent({
  name: 'MainLayout',

  components: {
  },

  setup () {

    return {
    }
  }
})
</script>
