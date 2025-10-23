<script>
import PieChart from './PieChart.vue';
import WordCloud from './WordCloud.vue';
import Legend from './Legend.vue';
import MutipleSelector from './MutipleSelector.vue';

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
    MutipleSelector
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
        legendSize: 0,
        selectorSize: 15 * window.innerWidth / 100,

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

        legend_list: [
          { color: "#FAC632", text: "Utensil & Vessel (1234)"},
          { color: "#FE7960", text: "Textile (123)"},
          { color: "#18B8EB", text: "Sculpture (123)"},
          { color: "#F38BA6", text: "Adornment & Ornament (123)"},
          { color: "#C8DA55", text: "Pictorial works (123)"},
          { color: "#00B88E", text: "Architecture (123)"},
        ]
      };
    },
}

</script>   

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
            <WordCloud :size="wordcloudSize" />
          </div>
          <div class="legend">
            <Legend v-for="item in legend_list" :text="item['text']" :color="item['color']" />
          </div>
        </div>

        <div class="Subject_block">   <!-- Subject模块 -->
          <MutipleSelector :size="selectorSize" title="Subject" :item_list="subject_list"/>
        </div>
      </div>

      <div class="viewer"></div>
    </div>

    <!-- 底部栏 -->
    <div class="Footer">
      Footer
    </div>
  </div>
</template>

<style scoped>
div {
  display: flex;
}

.container {
  width: 100vw;
  height: 100vh;
  flex-direction: column;
}


.Header {
  width: 100%;
  justify-content: space-between;
  align-items: center;
  flex-grow: 1;
  box-shadow: 0 4px 3px 0 rgba(80, 104, 87, 0.25);
  /* margin-bottom: 8px; */
  z-index: 9999;  /* Header置顶，让阴影置于Main的背景颜色之上 */
}
.Header .title{
  width: 15vw;
  margin-left: 2vw;
  align-items: center;
}
.Header .search-box{
  width: 40vw;
  height: 3.5vh;
  align-items: center;
  justify-content: space-between;
  border-radius: 60px;
  border: 1px solid #8B8B8B;
  background-color: #F0F0F0;
  padding: 0 0.5vw;
}
.Header .Personalization{
  width: 15vw;
  height: 3vh;
  align-items: center;
}


.Main {
  width: 100%;
  display: flex;
  flex-direction: row;
  flex-grow: 30;
}
.Main .controller {
  height: 100%;
  width: 18vw;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
}
.Main .controller .Medium_block{
  padding: 2vh 1vw 2vh 1vw;
  width: auto;
  display: flex;
  flex-direction: column;
}
.Main .controller .Medium_block .graph{
  margin-top: 0.5vh;
  width: 100%;
  height: 12vh;
  display: flex;
  justify-content: space-between;
}
.Main .controller .Medium_block .legend{
  margin-top: 0.5vh;
  width: 100%;
  /* height: 10vh; */
  display: flex;
  flex-wrap: wrap;
}

.Main .controller .Subject_block{
  margin: 2vh 1vw 2vh 1vw;
  width: 100%;
  /* background-color: aqua; */
  display: flex;
  flex-direction: column;
}

.Main .viewer {
  height: 100%;
  width: 85vw;
  background-color: #F5F5F5;
  overflow-y:auto;
}


.Footer {
  width: 100%;
  flex-grow: 2;
}


.no-border-input :deep(.el-input__inner) {
  border: none;
  outline: none;
  box-shadow: none;
  background-color: #F0F0F0;
  padding: 0 2px;
  width: 100%;
  height: 100%;
  font-size: 0.8vw;
}

.no-border-input :deep(.el-input__wrapper) {
  box-shadow: none;
  border: none;
  background-color: #F0F0F0;
  width: 100%;
}
</style>


