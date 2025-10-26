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
          <el-image :src="icon_search" style="width: 1.8vw;height: 1.8vh;" fit="fill"/>
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
          <MutipleSelector :size="selectorSize" />
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
          <MutipleSelector :size="selectorSize" title="Symbols" :item_list="subject_list"/>
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
        <Card :size="cardSize" v-for="value in Card_list" style="margin: 1vh 0.7vw;"/>
      </div>
    </div>

    <!-- 底部栏 -->
    <!-- <div class="Footer">
      Footer
    </div> -->
  </div>
</template>

<script>
import PieChart from './PieChart.vue';
import WordCloud from './WordCloud.vue';
import Legend from './Legend.vue';
import MutipleSelector from './MutipleSelector.vue';
import RadialBarChart from './RadialBarChart.vue';
import Card from './Card.vue';

import {ref} from 'vue'
import icon_mark from '../assets/images/mark.png';
import icon_search from '../assets/images/search.png';
import icon_like from '../assets/images/icon_like.png';
import icon_trans from '../assets/images/icon_trans.png';
import icon_arrow_up from '../assets/images/arrow_up.png';


export default {
  name: 'Main',
  components:{
    PieChart,
    WordCloud,
    Legend,
    MutipleSelector,
    RadialBarChart,
    Card
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
          (82 - 7) * window.innerWidth / 100 / 5 - 3, (82 - 7) * window.innerWidth / 100 / 5 * 1.6, 
        ],

        medium_list:[
          "Utensil & Vessel",
          "Sculpture",
          "Textile",
          "Adornment & Ornament",
          "Pictorial work",
          "Architecture"
        ],
        subject_list:[
          "Auspiciousness",
          "Narrativity",
          "Identity",
          "Ideology"
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
          { color: "#00B88E", text: "Architecture (123)"},
        ],

        Card_list:[
          1,2,3,4,5,6,7,8,9,10,11,12,13,14
        ]
      };
    },
    created(){
      console.log(window.innerWidth);
    }
}

</script>   


<style scoped>
  @import url('../style/main.css');
</style>


