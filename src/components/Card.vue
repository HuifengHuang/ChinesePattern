<template>
  <div class="container" :style="container_style">
    <div class="img">
      <div class="name"><span :style="name_size">{{ dataset.name }}</span></div>
      <div class="image">
        <img :src="image_path" style="object-fit: fill;"></img>
      </div>
      <div class="symbol">
        <span class="symbol_span" v-for="symbol in dataset.symbols" :style="text_size">{{ symbol }}</span>
      </div>
    </div>
    <div class="desc">
      <div class="info">
        <div class="time">
          <span :style="text_size">{{ dataset.time.first_time }}</span>
          <span :style="second_size">{{ dataset.time.second_time }}</span>
          <span :style="second_size">{{ dataset.time.third_time }}</span>
        </div>
        <div class="medium">
          <span :style="text_size">{{ dataset.medium.first_medium }}</span>
          <span :style="second_size">{{ dataset.medium.second_medium }}</span>
          <span :style="second_size">{{ dataset.medium.third_medium }}</span>
        </div>
      </div>
      <div class="interact">
        <div class="btn">
          <span class="span" :style="text_size">Identity</span>
          <span class="span" :style="text_size">Power</span>
        </div>
        <div class="icon">

        </div>
      </div>
    </div>
  </div>
</template>

<script> 
import dragon_image from '../assets/images/test/龙_001 (1).png'

export default {
  name: 'Card',
  props: {
    size:{    // 这里是卡片size
      type: Array,
      default: [300, 450]
    },
    dataset:{
      type: Object,
      default:{
        name: "Dragon",
        time: {
          first_time: "Ming Dyn.",
          second_time: "Dingling Mausoleum,",
          third_time: "Beijing"
        },
        medium: {
          first_medium: "Textile-Emroidery",
          second_medium: "Gold-threaded",
          third_medium: "Zhuanghua Satin"
        },
        symbols: ["Long", "Cloud", "Rock", "Wave"],
        image_path: "test/龙_001 (1).png",
      }
    }
  },
  data(){
    return {
      container_style: {
        width: this.size[0] + 'px',
        height: this.size[1] + 'px'
      },
      image_path: dragon_image,
      name_size:{
        'font-size' : this.size[1] * 0.7 * 0.1 * 0.6 + 'px',
      },
      text_size: {
        'font-size' : this.size[1] * 0.7 * 0.1 * 0.5 + 'px',
        'margin-left': '5px'
      },
      second_size:{
        'font-size' : this.size[1] * 0.7 * 0.1 * 0.4 + 'px',
        'color': '#8B8B8B',
        'margin-left': '5px'
      },
    }
  }
}
</script>

<style scoped>
div{
  display: flex;
}

.container{
  box-sizing: border-box;
  border-radius: 6px;
  border: 1px solid #8B8B8B;
  background: #FFF;
  flex-direction: column;
}
.img{
  height: 70%;
  width: 100%;
  flex-direction: column;
  box-sizing: border-box;
  border-bottom: 1px solid #8B8B8B;
}
.img .name{
  width: auto;
  height: 10%;
  align-items: center;
  padding-left: 5px;
}
.img .image{
  width: 100% ;
  height: 80%;
  justify-content: center;
}
.img .image img{
  width: 100%;
  height: 100%;
}
.img .symbol{
  height: 10%;
  width: auto;
  align-items: center;
  justify-content: flex-end;
}
.img .symbol .symbol_span{
  color: #000;
  font-family: Inter;
  font-style: normal;
  line-height: normal;
  letter-spacing: -0.24px;
  margin: 0 5px;
  padding: 0 5px;
  box-sizing: border-box;
  border-radius: 5px;
  border: 1px solid #8B8B8B;
}
.desc{
  width: 100%;
  height: 30%;
  flex-direction: column;
}
.desc .info{
  height: 60%;
  width: 100%;
  flex-direction: column;
}
.desc .info .time{
  height: 50%;
  width: 100%;
  align-items: center;
  flex-wrap: wrap;
}
.desc .info .medium{
  height: 50%;
  width: 100%;
  align-items: end;
  flex-wrap: wrap;
}
.desc .interact{
  height: 40%;
  width: 100%;
  justify-content: space-between;
}
.desc .interact .btn{
  height: auto;
  width: 50%;
  align-items: end;
  padding-bottom: 5px;
}
.desc .interact .btn .span{
  color: #000;
  font-family: Inter;
  font-style: normal;
  line-height: normal;
  letter-spacing: -0.24px;
  margin: 0 5px;
  padding: 0 5px;
  box-sizing: border-box;
  border-radius: 5px;
  border: 1px solid #8B8B8B;
}
</style>

