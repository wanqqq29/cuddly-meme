<template>
  <q-dialog rounded v-model="e_flag" position="top">
    <q-card
      style="width: 350px; height: 5rem; font-size: 1.5rem"
      class="flex flex-center text-center bg-secondary text-white text-weight-bold"
    >
      请输入正确的网站与产品id
    </q-card>
  </q-dialog>
  <div id="mainbody" class="q-pt-lg">
    <div id="header" class="flex justify-between">
      <div class="left flex justify-between">
        <div class="logo">
          <router-link to="/">👋Hi~</router-link>
        </div>
        <div class="darkBtn">
          <q-icon name="dark_mode" size="30px" @click="darkApi"/>
        </div>
      </div>
      <div class="right">
        <submit @e_flag="get_e_flag" style="width: 100%"/>
      </div>
    </div>
    <div id="content" class="flex row">
      <div class="left">
        <div class="pinfo">
          <div class="ptitle flex q-mb-md">
            <span>{{ pinfo.pname }}</span>
            <a :href="pinfo.plink" target="_blank"
            >
              <q-icon name="open_in_new" color="info"
              />
            </a>
          </div>
          <div class="ptext flex wrap q-mb-md">
            <div class="poutpoeple bg-secondary q-mt-sm">产品特色：{{ pinfo.pfeatures }}</div>
            <div class="offer bg-secondary q-mt-sm">供应商：{{ pinfo.poffer }}</div>
            <div class="poutpoeple bg-secondary q-mt-sm">出游人数：{{ pinfo.ppeoplenum }}</div>
            <div class="ptotalnum bg-secondary q-mt-sm">pinfo.ptotalnum</div>
          </div>

          <div class="pdesc q-mb-md">
            <span class="bg-secondary q-mb-md">产品简介</span>
            <p>{{ pinfo.pdesc }}</p>
          </div>
          <div class="pfeatures q-mb-md">
            <span class="bg-secondary q-mb-md">产品卖点</span>
            <ul>
              <li v-for="(item) in pinfo.pmd">{{ item }}</li>
            </ul>
          </div>
        </div>
      </div>
      <div class="right">
        <div class="pieChart"></div>
        <div class="wordChart"></div>
        <div class="barChart">1111</div>
        <q-btn label="csrf" @click="getfoo"></q-btn>
      </div>
    </div>
  </div>
</template>
<style lang="scss" scoped>
#mainbody {
  width: 65%;
  margin: 0 auto;
  //大屏
  @media (max-width: 800px) {
    #header {
      justify-content: center;

      .left {
        text-align: center;

        .logo {
          margin: 0 auto;
        }
      }

      .right {
        width: 100%;
      }
    }
  }

  #header {
    line-height: 45px;
    color: white;

    .left {
      font-size: 30px;

      .logo {
        cursor: pointer;
        margin-right: 20px;
        height: 45px;

        a {
          color: white;
          text-decoration: none;
        }
      }

      .darkBtn {
        cursor: pointer;
        height: 45px;
      }
    }

    .right {
      width: 60%;
      font-size: 12px;

      .optionBar {
        width: 35%;
      }
    }
  }

  #content {
    color: white;

    .left {
      width: 40%;
      padding-right: 20px;

      .pinfo {
        .ptitle {
          display: flex;
          flex-direction: row;
          font-size: 20px;

          span {
            width: 88%;
            word-wrap: break-word;
          }

          a {
            text-decoration: none;
          }
        }

        .ptext {
          div {
            width: fit-content;
            padding: 5px;
            margin-right: 3px;
            margin-left: 3px;
            border-radius: 9px;
          }
        }

        .pfeatures, .pdesc {
          span {
            padding: 5px;
            margin-left: 3px;
            margin-right: 3px;
            border-radius: 9px;
          }
        }

        .pfeatures {
          li {
            list-style: none;
          }
        }
      }
    }

    .right {
      width: 60%;
      padding-left: 20px;
    }

    @media (max-width: 800px) {
      //大屏
      .left {
        width: 100%;
      }
      .right {
        width: 100%;
      }
    }
  }
}
</style>
<script>
import {reactive, ref} from "vue";
import {useQuasar} from "quasar";
import Submit from "src/components/submit.vue";
import {api} from "boot/axios";

export default {
  setup() {
    //Dark mode
    const $q = useQuasar();
    const darkApi = () => {
      $q.dark.toggle();
    };

    //dialog
    const e_flag = ref(false);
    const get_e_flag = (e) => {
      e_flag.value = e;
    };

    const post_data = reactive({type: 'ctrip', pid: '10798720'});

    //请求景点信息数据
    const pinfo = reactive({
      pname: "", //产品名
      pdesc: "", //产品介绍
      pfeatures: "", //产品特点
      poffer: "", //产品供应商
      ppeoplenum: "", //产品消费人数
      ptotalnum: "", //总评论数
      pmd: "",//产品卖点
    });


    const getfoo = () => {
      api.post('/getInfo/', post_data).then((res) => {
        console.log(res.data)
        pinfo.pname = res.data.pname[0];
        pinfo.pdesc = res.data.pdesc[0];
        pinfo.pfeatures = res.data.pfeatures[0];
        pinfo.poffer = res.data.poffer[0];
        pinfo.ppeoplenum = res.data.ppeoplenum;
        pinfo.pmd = res.data.pmd
      })
        .catch(error => {
          console.log(error)
        })
    }


    return {
      darkApi,
      e_flag,
      get_e_flag,
      getfoo,
      pinfo
    };
  },
  components: {Submit},
};
</script>
