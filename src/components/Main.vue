<template>
  <div class="container">
    <!-- 顶部栏 -->
    <div class="Header">
        <div class="title">
          <el-image :src="icon_mark" style="width: 3vw;height: 3vh;" fit="fill"/>
          <span style="font-size: 3vh;">{{ label_name.SystemName }}</span>
        </div>
        <div class="search-box">
          <el-input class="no-border-input" v-model="input_value" style="width: 35vw" :placeholder=label_name.InputHolder />
          <el-image :src="icon_search" style="width: 1.8vw;height: 1.8vh;cursor: pointer;" fit="fill" v-on:click="search()"/>
        </div>
        <div class="Personalization">
          <el-image :src="icon_like" style="width: 2.5vw;height: 2.5vh;" fit="fill"/>
          <el-image :src="icon_trans" style="width: 2.5vw;height: 2.5vh;" fit="fill" v-on:click="switch_language()"/>
        </div>
    </div>

    <!-- 主体栏 -->
    <div class="Main">
      <div class="controller"> <!-- 左侧控制栏 -->
        
        <div class="Medium_block"> <!-- Medium模块 -->
          <MutipleSelector :size="selectorSize" :title=label_name.MediumName 
              :item_labels=label_name.MediumItems :item_status="medium_items_status"/>
          <!-- <div class="graph">
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
          </div> -->
        </div>

        <div class="Subject_block">   <!-- Subject模块 -->
          <MutipleSelector :size="selectorSize" :title="label_name.SubjectName" 
              :item_labels=label_name.SubjectItems :item_status="subject_items_status"/>
          <!-- <div style="margin-top: 1vh;">
            <RadialBarChart :size="radialbarchartSize" />
          </div>
          <div class="clouds">
            <div class="title">
              <span>Subject</span>
            </div>
            <WordCloud :size="subject_wordcloudSize" />
          </div> -->
        </div>

        <div class="Subject_block">   <!-- Symbols模块 -->
          <MutipleSelector :size="selectorSize" :title="label_name.SymbolsName" 
              :item_labels=label_name.SymbolsItems :item_status="symbols_items_status"/>
          <!-- <div style="margin-top: 1vh;">
            <RadialBarChart :size="radialbarchartSize" />
          </div>
          <div class="clouds">
            <div class="title">
              <span>Symbols</span>
            </div>
            <WordCloud :size="subject_wordcloudSize" />
          </div> -->
        </div>

        <div class="VisualFormat_block">   <!-- Visual_Format模块 -->
          <div class="Title"><span>{{ label_name.VisualFormat }}</span></div>
          <div class="Structure">
            <div><span>{{label_name.StructureName}}</span></div>
            <div class="checkgroup">
              <el-checkbox v-for="(item,index) in label_name.StructureItems" :label="item"
                  v-model="struture_items_status[index]" />
            </div>
          </div>
          <div class="Style">
            <div><span>{{ label_name.StyleName }}</span></div>
            <div class="checkgroup">
              <el-checkbox v-for="(item,index) in label_name.StyleItems" :label="item"
                  v-model="style_items_status[index]" />
            </div>
          </div>
          <!-- <div class="Morphology">
            <div><span>Morphology</span></div>
            <WordCloud :size="subject_wordcloudSize" style="border: 1px solid #000; box-sizing: border-box;"/>
          </div> -->
        </div>

      </div>

      <div class="viewer">  <!-- 右侧主视图模块 -->
        <Card :size="cardSize" v-for="value in filtered_data" :dataset="value" :language=language
            style="margin: 0.5vw 0.5vw;"/>
      </div>
    </div>

    <!-- 底部栏 -->
    <div class="Footer">
      <div class="History_period">
        <div class="selector">
          <span>{{ label_name.HistoryName }}</span>
          <img :src="icon_arrow_up" style="object-fit: contain;"  v-on:click="showHistorySelector"/>
        </div>
        <div class="labels">
          <el-checkbox v-for="(item, index) in label_name.HistoryItems" v-show="history_items_status[index]"
            v-model="history_items_status[index]" :label="item"  />
        </div>
      </div>
      <div></div>
    </div>

    <!-- History Period 展开栏 -->
    <div class="history_selector" v-show="history_selector_show">
      <el-checkbox v-for="(item, index) in label_name.HistoryItems" 
          v-model="history_items_status[index]" :label="item" font-size="smaller" />
    </div>
  </div>
  <div class="mask"></div>
  <Details class="details" :language="language"/>
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
import { GetLabelName_CN, GetCSVTitleName_CN } from '../common/labels_cn';
import { GetLabelName_EN, GetCSVTitleName_EN } from '../common/labels_en';

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

        // legend_list: [
        //   { color: "#FAC632", text: "Utensil & Vessel (1234)"},
        //   { color: "#FE7960", text: "Textile (123)"},
        //   { color: "#18B8EB", text: "Sculpture (123)"},
        //   { color: "#F38BA6", text: "Adornment & Ornament (123)"},
        //   { color: "#C8DA55", text: "Pictorial works (123)"},
        //   { color: "#00B88E", text: "Architecture (123)"}
        // ],

        history_selector_show: false,

        language: "English",
        label_name: [],
        csv_title_names: [],

        medium_items_status: [false,false,false,false,false,false],
        subject_items_status: [false,false,false,false],
        symbols_items_status: [false,false,false,false],
        struture_items_status: [false,false,false,false,false],
        style_items_status: [false,false],
        history_items_status: [false,false,false,false,false,false,false,false,false,false,false,false],

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
      this.language_change();
      this.getAllCards();

      // console.log(window.innerWidth);
    },
    methods:{
      showHistorySelector(){
        this.history_selector_show = (this.history_selector_show)?false:true;
      },
      async getAllCards(){
        const response = await axios.get(this.$BackendUrl + '/all_cards');
        this.results = response.data;
        this.filter();
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
      filter(){           // 过滤器
        const mediums = [], subjects = [], symbols = [], times = [];
        
        for(let i=0;i<this.label_name.MediumItems.length;i++) 
          if(this.medium_items_status[i])mediums.push(this.label_name.MediumItems[i]);

        for(let i=0;i<this.label_name.SubjectItems.length;i++) 
          if(this.subject_items_status[i])subjects.push(this.label_name.SubjectItems[i]);

        for(let i=0;i<this.label_name.SymbolsItems.length;i++) 
          if(this.symbols_items_status[i])symbols.push(this.label_name.SymbolsItems[i]);

        for(let i=0;i<this.label_name.HistoryItems.length;i++) 
          if(this.history_items_status[i])times.push(this.label_name.HistoryItems[i]);
        // console.log(mediums);
        var result = [];
        for(const feature of this.results){
          var flag = true;
          if(mediums.length != 0)flag = flag && mediums.includes(feature[this.csv_title_names.medium_lv1]);
          if(subjects.length != 0)flag = flag && subjects.includes(feature[this.csv_title_names.subject_lv1]);
          if(symbols.length != 0)flag = flag && symbols.includes(feature[this.csv_title_names.symbol_lv1]);
          if(times.length != 0)flag = flag && times.includes(feature[this.csv_title_names.time_lv1]);
          if(flag){
            result.push(feature);
          }
        }
        this.filtered_data = result;
        // console.log(result);
      },
      switch_language(){
        this.language = (this.language == "English")?"Chinese":"English";
      },
      language_change(){
        if(this.language=="English"){
          this.label_name = GetLabelName_EN();
          this.csv_title_names = GetCSVTitleName_EN();
        }
        else if(this.language=="Chinese"){
          this.label_name = GetLabelName_CN();
          this.csv_title_names = GetCSVTitleName_CN();
        }
      }
    },
    watch:{
      medium_items_status:{
        handler(newVal, oldVal){
          this.filter();
        },
        deep: true,
      },
      subject_items_status:{
        handler(newVal, oldVal){
          this.filter();
        },
        deep: true,
      },
      symbols_items_status:{
        handler(newVal, oldVal){
          this.filter();
        },
        deep: true,
      },
      history_items_status:{
        handler(newVal, oldVal){
          this.filter();
        },
        deep: true,
      },
      language:{
        handler(newVal, oldVal){
          this.language_change();
        }
      }
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
  height: 95vh;
  top: 5vh;
  left: 0%;
  background-color: #00000040;
  z-index: 3;
}
</style>


