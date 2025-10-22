<template>
  <div class="selector" :style="selector_style"> 
    <div class="title" :style="title_style">
      <div class="panel">
        <span style="font-size: 2vh;">{{ this.title }}</span>
        <el-checkbox class="panel_checkbox" v-for="item in status_lists" 
            v-model="item['status']" :label="item['text']" size="large" v-show="item['status']"/>
      </div>
      
      <el-image :src="icon_arrow_up" :style="image_style" fit="fill"/>
    </div>
    <div class="options">
      <el-checkbox v-for="item in status_lists" 
          v-model="item['status']" :label="item['text']" size="large" />
    </div>
  </div>
</template> 

<script>
import icon_arrow_up from '../assets/images/arrow_up.png';

export default {
  name: 'MutipleSelector',
  props: {
    title:{
      type: String,
      default: "Medium",
    },
    item_list:{
      type: Array,
      default: [
        "Utensil & Vessel",
        "Sculpture",
        "Textile",
        "Adornment & Ornament",
        "Pictorial work",
        "Architecture",
      ]
    },
    size:{
      type: Number,
      default: 300,
    }
  },
  data() {
    return {
      icon_arrow_up: icon_arrow_up,
      isActive: true,
      selector_style: null,
      title_style: null,
      image_style:{
        width: 0.1 * this.size  + 'px',
        height: 0.05 * this.size + 'px'
      },
      status_lists:[],
    }
  },
  created(){
      this.selector_style = {
          width: this.size + 'px',
          "border": (this.isActive)?"1px solid rgba(185, 185, 185, 1)":"none"
        }
      this.title_style = {
          "backgound-color": (this.isActive)?"#5F9DDA40":"none"
        }
  },
  mounted() {
    this.init();
  },
  methods: {
    init(){
      for(const item of this.item_list){
        this.status_lists.push({
          "text": item,
          "status": false
        })
      }
    }
  }
}

</script>

<style scoped>
.selector{
  min-height: 5vh;
  display: flex;
  flex-direction: column;
  border-radius: 5px;
  box-sizing: border-box;
  border: 1px solid #B9B9B9;
}
.selector .title{
  /* width: 100%; */
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 0.5vw;
  background-color: #5F9DDA40;
}
.panel{
  display: flex;
  flex-wrap: wrap;
}
.panel_checkbox{
  border: 1px solid #B9B9B9;
  background-color: #F3F3F3;
  padding: 0 0.3vw 0 0.1vw;
  margin: 0.1vh 0.1vw 0 0;
  border-radius: 5px;
}

.selector .options{
  width: 100%;
  display: flex;
  flex-direction: column;
  background-color: #F3F3F3;
  border-top: 1px solid rgba(185, 185, 185, 1);
}
</style>