<template>
  <div class="container">
    <!-- 顶部栏 -->
    <div class="Header">
        <div class="title">
          <el-image :src="icon_mark" style="width: 3vw;height: 3vh;" fit="fill"/>
          <span style="font-size: 3vh;">{{ label_name.SystemName }}</span>
        </div>
        <div class="search-box">
          <el-input class="no-border-input" v-model="input_value" style="width: 35vw" :placeholder=label_name.InputHolder  v-on:keyup.enter="search()"/>
          <el-image :src="icon_search" style="width: 2vw;height: 2vh;cursor: pointer;" fit="fill" v-on:click="search()"/>
        </div>
        <div class="Personalization">
          <el-image :src="icon_like" style="width: 2.5vw;height: 2.5vh;" fit="fill"/>
          <el-image :src="icon_trans" style="width: 2.5vw;height: 2.5vh;cursor: pointer;" fit="fill" v-on:click="switch_language()"/>
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
        <Card :size="cardSize" v-for="value in filtered_data" :dataset="value" :language=language v-on:click="set_detail(value)"
            style="margin: 0.5vw 0.5vw;cursor: pointer;"/>
      </div>
    </div>

    <!-- 底部栏 -->
    <div class="Footer">
      <div class="History_period">
        <div class="selector">
          <span>{{ label_name.HistoryName }}</span>
          <div class="icon_arrow">
            <img :src="icon_arrow" v-on:click="showHistorySelector"/>
          </div>
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

  <!-- 遮罩层 -->
  <div class="mask" v-show="is_detail_show"></div>

  <!-- Details 详细栏 -->
  <div class="details" v-if="is_detail_show">
    <Details style="width: 100%;height: 100%;" :language="language" :dataset="detail_value"/>
    <div class="button" v-on:click="close_detail()">
      <img :src="icon_close" style="width: 100%;height: 100%;object-fit: fill;"></img>
    </div>
  </div>
  
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
import icon_arrow_down from '../assets/images/arrow_down.png'
import icon_close from '../assets/images/close.png'

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
        icon_arrow_down: icon_arrow_down,
        icon_arrow: icon_arrow_up,
        icon_close: icon_close,
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
        is_detail_show: false,
        detail_value: null,

        medium_items_status: [false,false,false,false,false,false],
        subject_items_status: [false,false,false,false],
        symbols_items_status: [false,false,false,false],
        struture_items_status: [false,false,false,false,false],
        style_items_status: [false,false],
        history_items_status: [false,false,false,false,false,false,false,false,false,false,false,false],

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
        this.icon_arrow = (this.history_selector_show)?this.icon_arrow_down:this.icon_arrow_up;
      },
      async getAllCards(){
        const response = await axios.get(this.$BackendUrl + '/all_cards');
        this.results = response.data;
        this.filter();
      },
      async search(){
        if(this.input_value.length==0)return;
        axios.post(this.$BackendUrl + '/search', {
          "key_word": this.input_value,
        }).then(response => {
          this.results = response.data;
          this.filter();
          // console.log(this.results[0]);
        });
      },
      set_detail(value){
        this.detail_value = value;
        this.is_detail_show = true;
      },
      close_detail(){
        this.is_detail_show = false;
      },
      filter(){           // 过滤器
        const mediums = [], subjects = [], symbols = [], times = [], structures = [], styles = [];
        
        for(let i=0;i<this.label_name.MediumItems.length;i++) 
          if(this.medium_items_status[i])mediums.push(this.label_name.MediumItems[i]);

        for(let i=0;i<this.label_name.SubjectItems.length;i++) 
          if(this.subject_items_status[i])subjects.push(this.label_name.SubjectItems[i]);

        for(let i=0;i<this.label_name.SymbolsItems.length;i++) 
          if(this.symbols_items_status[i])symbols.push(this.label_name.SymbolsItems[i]);

        for(let i=0;i<this.label_name.StructureItems.length;i++) 
          if(this.struture_items_status[i])structures.push(this.label_name.StructureItems[i]);

        for(let i=0;i<this.label_name.StyleItems.length;i++) 
          if(this.style_items_status[i])styles.push(this.label_name.StyleItems[i]);

        for(let i=0;i<this.label_name.HistoryItems.length;i++) 
          if(this.history_items_status[i])times.push(this.label_name.HistoryItems[i]);
        // console.log(mediums);
        var result = [];
        for(const feature of this.results){
          var flag = true;
          if(mediums.length != 0)flag = flag && mediums.includes(feature[this.csv_title_names.medium_lv1]);
          if(subjects.length != 0)flag = flag && subjects.includes(feature[this.csv_title_names.subject_lv1]);
          if(symbols.length != 0)flag = flag && symbols.includes(feature[this.csv_title_names.symbol_lv1]);
          if(structures.length != 0)flag = flag && structures.includes(feature[this.csv_title_names.structure]);
          if(styles.length != 0)flag = flag && styles.includes(feature[this.csv_title_names.style]);
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
    watch: {
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
      struture_items_status:{
        handler(newVal, oldVal){
          this.filter();
        },
        deep: true,
      },
      style_items_status:{
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
  width: 60vw;
  height: 70vh;
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
.button{
  position: relative;
  width: 2.1vw;
  height: 2vw;
  top: -0.8vw;
  left: -1.2vw;
  z-index: 3;
  cursor: pointer;
}
</style>


