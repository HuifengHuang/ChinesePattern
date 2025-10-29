<template>
  <div class="container">
    <div class="head"><span class="title_text">{{ dataset.name_cn }}</span></div>
    <div class="body">
      <div class="img_container">
        <img :src="image_path" style="object-fit: fill;"></img>
      </div>
      <div class="info_container"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Legend',
  props: {
    dataset:{
      type: String,
      default: {
        'fileLocation': 'test', 
        'fileName_cn': '龙_001 (1)', 
        'symbol_lv1_cn': '动物,自然', 
        'symbol_lv1_en': 'Creature,Nature', 
        'symbol_lv2_cn': '龙，凤，云', 
        'symbol_lv2_en': 'dragon, phoenix, cloud', 
        'name_cn': '虬龙纹', 
        'name_en': 'Dragon', 
        'preview': ' ', 
        'description_cn': '', 
        'description_en': '', 
        'medium_lv1_cn': '装饰', 
        'medium_lv1_en': 'Adornment & Ornament', 
        'medium_lv2_cn': '玉饰', 
        'medium_lv3_cn': '玉腰带', 
        'time_lv1_cn': '春秋', 
        'time_lv1_en': 'Spring and Autumn', 
        'time_lv2_cn': '', 
        'location_cn': '', 
        'location_en': '', 
        'subject_lv1_cn': '身份', 
        'subject_lv2_cn': '皇权，力量', 
        'subject_lv3_cn': '象征力量与变化，体现战国“蟠螭穿云”的灵动审美', 
        'subject_lv3_en': '', 
        'structure_cn': '单体', 
        'morphology_cn': '对称', 
        'style_cn': '抽象', 
        'quality': '低', 
        'remark': '', '': ''}
    },
  },
  data(){
    return {
      squre: {
        "background-color": this.color,
        width: this.size + 'px',
        height: this.size + 'px'
      },
      word: {
        fontSize: 1.2 * this.size + 'px'
      },
    }
  }
}
</script>

<style scoped>
div{
  display: flex;
}

.container {
  width: 50vw;
  height: 60vh;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  padding: 1vw;
  border-radius: 8px;
  border: 1px solid #000;
  flex-direction: column;
}
.head{
  height: 10%;
  width: auto;
  /* align-items: center; */
}
.head .title_text{
  font-size: x-large;
  color: #000;
  font-weight: bold;
}
.body{
  height: 90%;
  width: auto;
  justify-content: space-between;
}
.body .img_container{
  height: 100%;
  width: 48%;
  box-sizing: border-box;
  border-radius: 6px;
  border: 1px solid #CDCDCD;
}
.body .info_container{
  height: 100%;
  width: 48%;
  box-sizing: border-box;
  border-radius: 6px;
  border: 1px solid #8B8B8B;
}

</style>