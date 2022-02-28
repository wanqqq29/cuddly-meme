<!--
 * @Author: wanqqq29
 * @Date: 2022-02-28 11:15:41
 * @LastEditTime: 2022-02-28 13:48:56
 * @LastEditors: wanqqq29
 * @Description: blog.wanqqq29.cn
 * @FilePath: \web\src\layouts\MainLayout.vue
-->
<template>
  <q-layout view="hHh lpR fFf">

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
