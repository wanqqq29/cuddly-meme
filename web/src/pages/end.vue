<template>
  <q-dialog v-model="e_flag" position="top" rounded>
    <q-card
      class="flex flex-center text-center bg-secondary text-white text-weight-bold"
      style="width: 350px; height: 5rem; font-size: 1.5rem"
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
        <submit style="width: 100%" @e_flag="get_e_flag"/>
      </div>
    </div>
    <div id="content" class="flex row">
      <div class="left">
        <div class="pinfo">
          <div class="ptitle flex q-mb-md">
            <span>{{ pinfo.pname }}</span>
            <a :href="pinfo.plink" target="_blank">
              <q-icon color="info" name="open_in_new"
              />
            </a>
          </div>
          <div class="ptext flex wrap q-mb-md">
            <div class="poutpoeple bg-secondary q-mt-sm">产品特色：{{ pinfo.pfeatures }}</div>
            <div class="offer bg-secondary q-mt-sm">供应商：{{ pinfo.poffer }}</div>
            <div class="poutpoeple bg-secondary q-mt-sm">出游人数：{{ pinfo.ppeoplenum }}</div>
            <div class="ptotalnum bg-secondary q-mt-sm">评论总数：{{ pinfo.ptotalnum }}</div>
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
          <div class="barChart">
            <bar-chart :barData="charts_data.charts.bar"/>
          </div>
        </div>
      </div>
      <div class="right">

        <div class="main_content">
          <q-card>
            <q-tabs
              v-model="tab"
              align="justify"
              class="bg-secondary text-white"
              narrow-indicator
            >
              <q-tab label="评论" name="commen"/>
              <q-tab label="图片" name="pic"/>
            </q-tabs>

            <q-separator/>

            <q-tab-panels v-model="tab" animated class="bg-info text-left">
              <q-tab-panel name="commen">
                {{ review_list.load.length }}|{{ review_list.all.length }}
                <q-list class="text-white shadow-2 rounded-borders bg-secondary " style=" width: 100%;">
                  <q-scroll-area style="height: 400px; width: 100%;">
                    <q-infinite-scroll :offset="250" @load="onLoad_Commen">
                      <div v-for="(item,index) in review_list.load" :key="index">
                        <q-item>
                          <q-item-section avatar>
                            <q-avatar>
                              {{ item['score'] }}
                            </q-avatar>
                          </q-item-section>
                          <q-item-section>
                            {{ item['item'] }}
                          </q-item-section>
                        </q-item>
                        <q-separator color="orange" inset/>
                      </div>
                      <template v-slot:loading>
                        <div class="row justify-center q-my-md">
                          <q-spinner-dots color="primary" size="40px"/>
                        </div>
                      </template>
                    </q-infinite-scroll>
                  </q-scroll-area>
                </q-list>
              </q-tab-panel>
              <q-tab-panel name="pic">
                {{ pic_list.load.length }}|{{ pic_list.all.length }}
                <q-list class="text-white shadow-2 rounded-borders bg-purple-3" style=" width: 100%;">
                  <q-scroll-area style="height: 400px; width: 100%;">
                    <q-infinite-scroll :offset="250" @load="onLoad_Pic">
                      <div class="row">
                        <img v-for="(item,index) in pic_list.load" :key="index" :src="item" class="col-6 ">
                      </div>
                      <template v-slot:loading>
                        <div class="row justify-center q-my-md">
                          <q-spinner-dots color="primary" size="40px"/>
                        </div>
                      </template>
                    </q-infinite-scroll>
                  </q-scroll-area>
                </q-list>
              </q-tab-panel>
            </q-tab-panels>
          </q-card>
        </div>
        <div class="row">
          <div class="pieChart col">
            <pie-chart :pieData="charts_data.charts.pie"/>
          </div>
          <div class="wordChart col q-ml-sm">
            <word-chart :wordData="charts_data.charts.wordCloud"/>
          </div>
        </div>
        <!--        <q-btn label="getinfo" @click="getinfo"></q-btn>-->
        <!--        <q-btn label="getWordCloud" @click="getWordCloud"></q-btn>-->
        <!--        <q-btn label="getreview" @click="getreview"></q-btn>-->
      </div>
    </div>
  </div>
</template>
<style lang="scss" scoped>
#mainbody {
  width: 85%;
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

        .pdesc {
          p {
            margin-top: 14px;
          }
        }

        .pfeatures {
          ul {
            padding-left: 0;
            list-style: none;

            li {
            }
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
import {reactive, ref, onMounted} from "vue";
import {useQuasar} from "quasar";
import Submit from "src/components/submit.vue";
import WordChart from "../components/charts/WordChart.vue";
import PieChart from "../components/charts/PieChart.vue";
import BarChart from "../components/charts/BarChart.vue";
import {api} from "boot/axios";
import {useRoute, useRouter} from "vue-router";

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

    //router是全局路由对象，route= useRoute()是当前路由对
    let router = useRouter();
    let route = useRoute();
    const post_data = {type: route.params.type, pid: route.params.pid};
    // const post_data = reactive({type: 'ctrip', pid: '14262204'});

    const check_flag = route.params.check_flag;

    //请求评论数据
    const review_list = reactive({
      all: [],
      load: [],
    })
    const pic_list = reactive({
      all: [],
      load: [],
    })

    const getreview = () => {
      api.post("/getReview/", post_data).then((res) => {
        console.log(res.data['goodrate'])
        pinfo.ptotalnum = res.data['totalnum'];
        review_list.all = res.data['reviewlist'];
        pic_list.all = res.data['piclist'];
        charts_data.charts.pie = res.data['goodrate']
      }).catch((e) => {
        console.log(e)
      })

    };

    const onLoad_Commen = (index, done) => {
      review_list.all.splice(0, 20).forEach((item) => {
        review_list.load.push(item)
      })
      done()
    }

    const onLoad_Pic = (index, done) => {
      pic_list.all.splice(0, 20).forEach((item) => {
        pic_list.load.push(item)
      })
      done()
    }


    //请求景点信息数据
    const pinfo = reactive({
      pname: "", //产品名
      pdesc: "", //产品介绍
      pfeatures: "", //产品特点
      poffer: "", //产品供应商
      ppeoplenum: "", //产品消费人数
      ptotalnum: "", //总评论数
      pmd: "",//产品卖点
      plink: "",//产品链接
    });

    const getinfo = () => {
      api.post('/getInfo/', post_data).then((res) => {
        pinfo.pname = res.data.pname[0];
        pinfo.pdesc = res.data.pdesc[0];
        pinfo.pfeatures = res.data.pfeatures[0];
        pinfo.poffer = res.data.poffer[0];
        pinfo.ppeoplenum = res.data.ppeoplenum;
        pinfo.pmd = res.data.pmd
        pinfo.plink = res.data.plink
      })
        .catch(error => {
          console.log(error)
        })
    }

    //获取情感分析图表数据
    const charts_data = reactive({
      score: "", //
      charts: {
        pie: "", //好评率
        wordCloud: [], //词云
        bar: {
          y: {},
          x: [],
          type: [],
        }, //柱状图
      },
    });
    const getWordCloud = () => {
      api.post("/getWordCloud/", post_data).then((res) => {
        // charts_data.charts.pie = res.data.charts.pie;
        charts_data.charts.wordCloud = res.data.charts.wordCloud;
        charts_data.charts.bar = {
          y: {
            good: [32, 55, 11, 32, 51, 64, 763, 123, 523, 532, 645, 64],
            bad: [32, 55, 11, 32, 51, 64, 763, 123, 523, 532, 645, 64],
          },
          x: [
            "1月",
            "2月",
            "3月",
            "4月",
            "5月",
            "6月",
            "7月",
            "8月",
            "9月",
            "10月",
            "11月",
            "12月",
          ],
          type: ["好评", "差评", "总数"],
        };
        $q.loading.hide()
      });
    };


    const tab = ref('commen')
    onMounted(() => {

      if (
        check_flag |
        (post_data.type != undefined) |
        (post_data.pid != undefined)
      ) {
        $q.loading.show({
          message: '正在渲染数据，请稍后...'
        })
        getinfo();
        getWordCloud()
        getreview()
      } else {
        router.push("/");
      }
    });


    return {
      darkApi,
      e_flag,
      get_e_flag,
      getinfo,
      pinfo,
      charts_data,
      getWordCloud,
      tab,
      onLoad_Commen,
      onLoad_Pic,
      review_list,
      pic_list,
      getreview,

    };
  }
  ,
  components: {Submit, PieChart, WordChart, BarChart},
};
</script>
