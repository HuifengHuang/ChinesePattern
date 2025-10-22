<script>
import PieChart from './piechart.vue';
import WordCloud from './WordCloud.vue';

import {ref} from 'vue'
import icon_mark from '../assets/images/mark.png';
import icon_search from '../assets/images/search.png';
import icon_like from '../assets/images/icon_like.png';
import icon_trans from '../assets/images/icon_trans.png';
import icon_arrow_up from '../assets/images/arrow_up.png';

const activeNames = ref(['1']);

export default {
  name: 'Main',
  components:{
    PieChart,
    WordCloud
  },
  data() {
      return {
        icon_mark: icon_mark,
        icon_search: icon_search,
        icon_like: icon_like,
        icon_trans: icon_trans,
        icon_arrow_up: icon_arrow_up,
        input_value: '',

        piechartSize: 12 * window.innerHeight / 100,
        wordcloutSize: [18 * window.innerHeight / 100 ,10 * window.innerHeight / 100],

        medium_list:[
          "Utensil & Vessel",
          "Sculpture",
          "Textile",
          "Adornment & Ornament",
          "Pictorial work",
          "Architecture"
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

          <div class="selector"> 
            <div class="title_m">
              <span  style="font-size: 2vh;">Medium</span>
              <el-image :src="icon_arrow_up" style="width: 1.1vw;height: 1.1vh;" fit="fill"/>
            </div>
            <div class="options">
              <el-checkbox v-for="item in medium_list" v-model="checked1" :label="item" size="large" />
            </div>
          </div>
          <div class="graph">
            <PieChart :size="piechartSize" />
            <WordCloud :size="wordcloutSize" />
          </div>
          <div class="legend">

          </div>
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
  overflow: auto;
}
.Main .controller .Medium_block{
  margin: 2vh 1vw 0 1vw;
  width: 100%;
  overflow: auto;
  /* background-color: aqua; */
  display: flex;
  flex-direction: column;
}
.Main .controller .Medium_block .selector{
  width: 100%;
  min-height: 5vh;
  display: flex;
  flex-direction: column;
  border-radius: 5px;
  box-sizing: border-box;
  border: 1px solid rgba(185, 185, 185, 1);
}
.Main .controller .Medium_block .selector .title_m{
  /* width: 100%; */
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 0.5vw;
  background-color: #5F9DDA40;
}
.Main .controller .Medium_block .selector .options{
  width: 100%;
  display: flex;
  flex-direction: column;
  background-color: #F3F3F3;
  border-top: 1px solid rgba(185, 185, 185, 1);
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
  height: 10vh;
  box-sizing: border-box;
  border: 1px solid #000;
  display: flex;
}
.Main .viewer {
  height: 100%;
  width: 85vw;
  background-color: #F5F5F5;
  overflow: auto;
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


