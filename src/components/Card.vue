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
          <span :style="second_size" v-for="value in dataset.time.other_time">{{ value }}</span>
        </div>
        <div class="medium">
          <span :style="text_size">{{ dataset.medium.first_medium }}</span>
          <span :style="second_size" v-for="value in dataset.medium.other_medium">{{ value }}</span>
        </div>
      </div>
      <div class="subject">
        <div class="btn">
          <span class="span" :style="text_size">{{ dataset.subject.first_subject }}</span>
          <span class="span" :style="text_size"  v-for="value in dataset.subject.other_subject">{{ value }}</span>
        </div>
        <div class="icon">

        </div>
      </div>
    </div>
  </div>
</template>

<script> 
import dragon_image from '../assets/images/test/龙_001 (1).png'
import axios from 'axios';

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
          other_time: ["Dingling Mausoleum","Beijing"]
        },
        medium: {
          first_medium: "Textile-Emroidery",
          other_medium: ["Gold-threaded","Zhuanghua Satin"]
        },
        subject:{
          first_subject: "Identity",
          other_subject: ["Power"]
        },
        symbols: ["Long", "Cloud", "Rock", "Wave"],
        image: "龙_001 (2).png",
      }
    }
  },
  data(){
    return {
      container_style: {
        width: this.size[0] + 'px',
        height: this.size[1] + 'px'
      },
      image_path: null,
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
  },
  created(){
    this.getImage();
  },
  methods:{
    async getImage(){
      try {
          // 发送GET请求到Flask后端
          const response = await axios.get(this.$BackendUrl + '/images/' + this.dataset.image, {
              responseType: 'blob' // 重要：指定响应类型为blob
          });
          // 将响应数据转换为可显示的URL
          const blob = new Blob([response.data], { type: response.headers['content-type'] });
          this.image_path =  URL.createObjectURL(blob);
      } catch (err) {
          console.error('获取图片失败:', err);
      } 
    }
  },
    watch:{
      dataset:{
        handler(newVal, oldVal){
            this.getImage();
        },
        deep: true,
        },
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
.desc .subject{
  height: 40%;
  width: 100%;
  justify-content: space-between;
}
.desc .subject .btn{
  height: auto;
  /* width: 50%; */
  align-items: end;
  padding-bottom: 5px;
}
.desc .subject .btn .span{
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

