<template>
  <div class="container">
    <!-- 顶部栏 -->
    <div class="Header">
        <div class="title">
          <el-image :src="icon_mark" style="width: 3vw;height: 3vh;" fit="fill"/>
          <span style="font-size: 3vh;">SYSTEMNAME</span>
        </div>
        <div class="search-box">
          <el-input class="no-border-input" v-model="input_value" style="width: 35vw" placeholder="Please input" />
          <el-image :src="icon_search" style="width: 1.8vw;height: 1.8vh;cursor: pointer;" fit="fill" v-on:click="search()"/>
        </div>
        <div class="Personalization">
          <el-image :src="icon_like" style="width: 2.5vw;height: 2.5vh;" fit="fill"/>
          <el-image :src="icon_trans" style="width: 2.5vw;height: 2.5vh;" fit="fill"/>
        </div>
    </div>

    <!-- 主体栏 -->
    <div class="Main">
      <div class="controller"> <!-- 左侧控制栏 -->
        
        <div class="Medium_block"> <!-- Medium模块 -->
          <MutipleSelector :size="selectorSize" title="Medium" :item_list="medium_list"/>
          <div class="graph">
            <PieChart :size="piechartSize" />

            <div class="clouds">
              <div class="title">
                <span>Medium</span>
              </div>
              <WordCloud :size="wordcloudSize" />
            </div>

          </div>
          <div class="legend">
            <Legend v-for="item in legend_list" :text="item['text']" :color="item['color']" />
          </div>
        </div>

        <div class="Subject_block">   <!-- Subject模块 -->
          <MutipleSelector :size="selectorSize" title="Subject" :item_list="subject_list"/>
          <div style="margin-top: 1vh;">
            <RadialBarChart :size="radialbarchartSize" />
          </div>
          <div class="clouds">
            <div class="title">
              <span>Subject</span>
            </div>
            <WordCloud :size="subject_wordcloudSize" />
          </div>
        </div>

        <div class="Subject_block">   <!-- Symbols模块 -->
          <MutipleSelector :size="selectorSize" title="Symbols" :item_list="symbol_list"/>
          <div style="margin-top: 1vh;">
            <RadialBarChart :size="radialbarchartSize" />
          </div>
          <div class="clouds">
            <div class="title">
              <span>Symbols</span>
            </div>
            <WordCloud :size="subject_wordcloudSize" />
          </div>
        </div>

        <div class="VisualFormat_block">   <!-- Visual_Format模块 -->
          <div class="Title"><span>VisualFormat</span></div>
          <div class="Structure">
            <div><span>Structure</span></div>
            <div class="checkgroup">
              <el-checkbox v-for="item in Structure_list" :label="item" />
            </div>
          </div>
          <div class="Style">
            <div><span>Style</span></div>
            <div class="checkgroup">
              <el-checkbox v-for="item in Style_list" :label="item" />
            </div>
          </div>
          <div class="Morphology">
            <div><span>Morphology</span></div>
            <WordCloud :size="subject_wordcloudSize" style="border: 1px solid #000; box-sizing: border-box;"/>
          </div>
        </div>

      </div>

      <div class="viewer">
        <Card :size="cardSize" v-for="value in filtered_data" :dataset="value" style="margin: 0.5vw 0.5vw;"/>
      </div>
    </div>

    <!-- 底部栏 -->
    <div class="Footer">
      <div class="History_period">
        <div class="selector">
          <span>History Period</span>
          <img :src="icon_arrow_up" style="object-fit: contain;"  v-on:click="showHistorySelector"/>
        </div>
        <div class="labels">
          <el-checkbox v-for="item in history_period" v-show="item['status']"
            v-model="item['status']" :label="item['period']"  />
        </div>
      </div>
      <div></div>
    </div>

    <!-- History Period 展开栏 -->
    <div class="history_selector" v-show="history_selector_show">
      <el-checkbox v-for="item in history_period" 
          v-model="item['status']" :label="item['period']" font-size="smaller" />
    </div>
  </div>
  <div class="mask"></div>
  <Details class="details"/>
</template>

<script>
import PieChart from './PieChart.vue';
import WordCloud from './WordCloud.vue';
import Legend from './Legend.vue';
import MutipleSelector from './MutipleSelector.vue';
import RadialBarChart from './RadialBarChart.vue';
import Card from './Card.vue';
import Details from './Details.vue';

import {ref} from 'vue'
import icon_mark from '../assets/images/mark.png';
import icon_search from '../assets/images/search.png';
import icon_like from '../assets/images/icon_like.png';
import icon_trans from '../assets/images/icon_trans.png';
import icon_arrow_up from '../assets/images/arrow_up.png';

import axios from 'axios';

export default {
  name: 'Main',
  components:{
    PieChart,
    WordCloud,
    Legend,
    MutipleSelector,
    RadialBarChart,
    Card,
    Details
  },
  data() {
      return {
        icon_mark: icon_mark,
        icon_search: icon_search,
        icon_like: icon_like,
        icon_trans: icon_trans,
        icon_arrow_up: icon_arrow_up,
        input_value: '',

        piechartSize: 5.5 * window.innerWidth / 100,
        wordcloudSize: [9.5 * window.innerWidth / 100 ,9.5 * window.innerHeight / 100],
        subject_wordcloudSize: [14.8 * window.innerWidth / 100 ,11 * window.innerHeight / 100],
        legendSize: 0,
        selectorSize: 15 * window.innerWidth / 100,
        radialbarchartSize: [15 * window.innerWidth / 100, 5 * window.innerHeight / 100],
        cardSize:[
          (82 - 5) * window.innerWidth / 100 / 6 - 8, (82 - 5) * window.innerWidth / 100 / 6 * 1.5
        ],

        medium_list:[
          {"name":"器物", "status":false},
          {"name":"Sculpture", "status":false},
          {"name":"织绣", "status":false},
          {"name":"装饰", "status":false},
          {"name":"平面绘画", "status":false},
          {"name":"建筑 ", "status":false},
        ],
        medium_list_en:[
          {"name":"Utensil & Vessel", "status":false},
          {"name":"Sculpture", "status":false},
          {"name":"Textile", "status":false},
          {"name":"Adornment & Ornament", "status":false},
          {"name":"Pictorial work", "status":false},
          {"name":"Architecture", "status":false},
        ],
        subject_list:[
          {"name":"吉祥", "status":false},
          {"name":"叙事", "status":false},
          {"name":"身份", "status":false},
          {"name":"思想", "status":false},
        ],
        subject_list_en:[
          {"name":"Auspiciousness", "status":false},
          {"name":"Narrativity", "status":false},
          {"name":"Identity", "status":false},
          {"name":"Ideology", "status":false},
        ],
        symbol_list:[
          {"name":"生物", "status":false},
          {"name":"自然", "status":false},
          {"name":"人与人造物", "status":false},
          {"name":"其他", "status":false},
        ],    
        symbol_list_en:[
          {"name":"Creature", "status":false},
          {"name":"Nature", "status":false},
          {"name":"Human", "status":false},
          {"name":"Others", "status":false},
        ],
        Structure_list:[
          "Single (321)",
          "Repeat (2)",
          "Tile (3)",
          "Scene combination (51)",
          "Decorative combination (13)",
        ],
        Style_list:[
          "Realistic (321)",
          "Abstract (432)"
        ],

        legend_list: [
          { color: "#FAC632", text: "Utensil & Vessel (1234)"},
          { color: "#FE7960", text: "Textile (123)"},
          { color: "#18B8EB", text: "Sculpture (123)"},
          { color: "#F38BA6", text: "Adornment & Ornament (123)"},
          { color: "#C8DA55", text: "Pictorial works (123)"},
          { color: "#00B88E", text: "Architecture (123)"}
        ],

        Card_list:[
          1,2,3,4,5,6,7,8,9,10,11,12,13,14
        ],

        history_period:[
          {"period": "石器时代", "status":false},
          {"period": "商代", "status":false},
          {"period": "西周", "status":false},
          {"period": "春秋", "status":false},
          {"period": "秦代", "status":false},
          {"period": "汉", "status":false},
          {"period": "魏晋", "status":false},
          {"period": "南北朝", "status":false},
          {"period": "唐代", "status":false},
          {"period": "宋代", "status":false},
          {"period": "元代", "status":false},
          {"period": "明代", "status":false},
          {"period": "清代","status":false}
        ],

        history_selector_show: false,

        /**     filtered_data 示例
          {           
            "name": "long",
            "symbols": {
              "first_symbol": "",
              "other_symbol": []
            },
            "mediums": {
              "first_medium": "",
              "other_medium": []
            },
            "times": {
              "first_time": "",
              "other_time": []
            },
            "image": null
          }
        */
        filtered_data:[],
        results:[],
      };
    },
    created(){

      // console.log(window.innerWidth);
    },
    methods:{
      showHistorySelector(){
        this.history_selector_show = (this.history_selector_show)?false:true;
      },
      // async loadImage(){
      //   try {
      //     // 假设后端返回图片列表
      //     const response = await axios.get('http://localhost:5000/api/images');
      //     this.results = response.data;
      //   } catch (error) {
      //     console.error('加载图片列表失败:', error);
      //   }
      // },
      async search(){
        axios.post(this.$BackendUrl + '/search', {
          "key_word": this.input_value,
        }).then(response => {
          this.results = response.data;
          this.filter();
          // console.log(this.results[0]);
        });
      },
      filter(){
        // Medium 检查
        const mediums = [], subjects = [], symbols = [], times = [];
        
        for(const medium of this.medium_list) if(medium.status)mediums.push(medium.name);
        for(const subject of this.subject_list) if(subject.status)subjects.push(subject.name);
        for(const symbol of this.symbol_list) if(symbol.status)symbols.push(symbol.name);
        for(const time of this.history_period) if(time.status)times.push(time.name);
        console.log(mediums);
        var result = [];
        for(const feature of this.results){
          var flag = true;
          if(mediums.length != 0)flag = flag && mediums.includes(feature['medium_lv1_cn']);
          if(subjects.length != 0)flag = flag && subjects.includes(feature['subject_lv1_cn']);
          if(symbols.length != 0)flag = flag && symbols.includes(feature['symbol_lv1_cn']);
          if(times.length != 0)flag = flag && times.includes(feature['time_lv1_cn ']);
          if(flag){
            result.push({
              name: feature['name_cn'],
              time: {
                first_time: feature['time_lv1_cn'],
                other_time: [feature['time_lv2_cn']]
              },
              medium: {
                first_medium: feature['medium_lv1_cn'],
                other_medium: [feature['medium_lv2_cn'], feature['medium_lv3_cn']]
              },
              subject:{
                first_subject: feature['subject_lv1_cn'],
                other_subject: [feature['subject_lv2_cn']]
              },
              symbols: [feature['symbol_lv1_cn'],feature['symbol_lv2_cn']],
              image: feature['fileName_cn'],
            })
          }
        }
        this.filtered_data = result;
        console.log(result);
      },
    },
    watch:{
      medium_list:{
        handler(newVal, oldVal){
          this.filter();
        },
        deep: true,
      },
      subject_list:{
        handler(newVal, oldVal){
          this.filter();
        },
        deep: true,
      },
      symbol_list:{
        handler(newVal, oldVal){
          this.filter();
        },
        deep: true,
      },
      history_period:{
        handler(newVal, oldVal){
          this.filter();
        },
        deep: true,
      },
    }
}

</script>   


<style scoped>
  @import url('../style/main.css');
.details{
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 5;
  width: 50vw;
  height: 60vh;
}
.mask{
  position: absolute;
  width: 100vw;
  height: 100vh;
  top: 0%;
  left: 0%;
  background-color: #00000040;
  z-index: 3;
}
</style>


