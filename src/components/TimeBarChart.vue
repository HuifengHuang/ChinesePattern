<template>
  <div class="donut-chart" :style="div_size" ref="chartContainer"></div>
</template>

<script>
import * as d3 from 'd3';

export default {
  name: 'TimeBarChart',
  props: {
    size: {
      type: Number,
      default: [1800, 120]
    },
    dataset: {
      type: Array,
      default: [
        {value:341, start:-2270,  end:-2070,    status:false},
        {value:321, start:-1600,  end:-1046,    status:false},
        {value:467, start:-1046,  end:-771,     status:false},
        {value:350, start:-771,   end:-476,     status:true},
        {value:466, start:-476,   end:-221,     status:true},
        {value:231, start:-221,   end:-206,     status:false},
        {value:501, start:-202,   end:220,      status:false},
        {value:221, start:220,    end:420,      status:false},
        {value:121, start:420,    end:589,      status:false},
        {value:654, start:589,    end:960,      status:false},
        {value:432, start:960,    end:1279,     status:false},
        {value:321, start:1279,   end:1368,     status:false},
        {value:400, start:1368,   end:1644,     status:false},
        {value:300, start:1644,   end:1912,     status:false},
      ]
    }
  },
  data() {
    return {
      svg: null,
      padding: 10,
      div_size:{
        width: this.size[0] + 'px',
        height: this.size[1] + 'px'
      },
      total_span:[-2270, 1950],
      period_span:[
        {name_cn:"石器时代", name_en:"Stone Age",       start:-2270,  end:-2070},
        {name_cn:"夏",      name_en:"Xia",              start:-2070,  end:-1600},
        {name_cn:"商 ",     name_en:"Shang",            start:-1600,  end:-1046},
        {name_cn:"西周",    name_en:"West Zhou",        start:-1046,  end:-771},
        {name_cn:"春秋",    name_en:"Spring and Autumn",start:-771,   end:-476},
        {name_cn:"战国",    name_en:"Warring States",   start:-476,   end:-221},
        {name_cn:"秦",      name_en:"Qin",              start:-221,   end:-206},
        {name_cn:"西汉",    name_en:"West Han",         start:-202,   end:8},
        {name_cn:"东汉",    name_en:"East Han",         start:25,     end:220},
        {name_cn:"魏",      name_en:"Wei",              start:220,    end:265},
        {name_cn:"两晋",    name_en:"Two Jins",         start:265,    end:420},
        {name_cn:"南北朝",  name_en:"North-South",      start:420,    end:589},
        {name_cn:"隋",      name_en:"Sui",              start:589,    end:618},
        {name_cn:"唐",      name_en:"Tang",             start:618,    end:907},
        {name_cn:"五代十国", name_en:"Five Dyns",       start:907,    end:960},
        {name_cn:"宋",      name_en:"Song",             start:960,    end:1279},
        {name_cn:"元",      name_en:"Yuan",             start:1279,   end:1368},
        {name_cn:"明",      name_en:"Ming",             start:1368,   end:1644},
        {name_cn:"清",      name_en:"Qing",             start:1644,   end:1912},
      ],
      span_bar:[-2070, -1600, -1046, -771, -476, -221, -206, -202, 8, 25, 220, 265, 420, 589, 618, 907, 960, 1279, 1368, 1644, 1912]
    };
  },
  mounted() {
    this.initChart();
    this.bars_refresh();
    // this.text_show();
  },
  methods: {
    initChart(){
      if (this.svg) {
        this.svg = null;
      }

      const container = this.$refs.chartContainer;
      const width = this.size[0] - 2 * this.padding;
      const height = this.size[1] - 2 * this.padding;

      // 创建 SVG
      this.svg = d3.select(container)
        .append('svg')
        .attr('width', width)
        .attr('height', height);

      var xScale = d3.scaleLinear()
        .domain(this.total_span)
        .range([0, width]);

      var ticks = [];
      for(let i=-2100;i<=1900;i+=100)ticks.push(i);
      var axis = d3.axisBottom(xScale)
          .tickValues(ticks)
          .tickFormat(d3.format(""))
          .tickSizeOuter(0);


      // 添加刻度尺
      this.svg.append("g")
        .attr("transform", `translate(0, 60)`)
        .call(axis);

      // console.log(this.span_bar);

      //  添加朝代分割线
      this.svg.append("g")
        .attr("fill", "black")
        .selectAll()
        .data(this.span_bar)
        .join("rect")
        .attr("x", (d)=>xScale(d))
        .attr("y", 80)
        .attr("width", 1)
        .attr("height", 20);
      
      //  添加朝代文字
      this.svg.append("g")
        .selectAll()
        .data(this.period_span)
        .join("text")
        .attr("text-anchor", "middle")
        .attr("x", (d)=>xScale((d.end + d.start) / 2))
        .attr("y", 80 + 10)
        .attr("dominant-baseline", "middle")  // 垂直居中
        .text((d)=>d.name_en)
        .attr("font-size", (d)=>{
            if(d.end - d.start < 80)return "8px"
            else return "12px"
        })
    },
    bars_refresh(){
      d3.select("#g-bar").remove();
      d3.select("#g-text").remove();

      const width = this.size[0] - 2 * this.padding;
      const height = this.size[1] - 2 * this.padding;
      const index = d3.local();
      const that = this;

      var xScale = d3.scaleLinear()
        .domain(this.total_span)
        .range([0, width]);
      
      var xSpanScale = d3.scaleLinear()
        .domain([0, this.total_span[1]-this.total_span[0]])
        .range([0, width]);

      var yScale = d3.scaleLinear()
        .domain([0, d3.max(this.dataset, d=>d.value)])
        .range([0, 60 - 12]);

      // 添加bar
      this.svg.append("g")
        .attr("id", "g-bar")
        .selectAll()
        .data(this.dataset)
        .join("rect")
        .attr("x", (d)=>xScale(d.start))
        .attr("y", (d)=>60-yScale(d.value))
        .attr("width", (d)=>xSpanScale(d.end - d.start))
        .attr("height", (d)=>yScale(d.value))
        .style("fill", (d)=>{
          if(d.status)return "#FAC63280";
          else return "#8BB1FF80";
        })
        .style("stroke", (d)=>{
          if(d.status)return "#FAC632";
          else return "#8BB1FF";
        })
        .style("stroke-width", 1)
        .each(function(d,i){
          index.set(this, i);
        })
        .on("click", function(event, d){
          console.log(that.dataset[index.get(this)].status);
          that.dataset[index.get(this)].status = (d.status)?false:true
        });
      
      // 添加bar文字
      this.svg.append("g")
        .attr("id", "g-text")
        .selectAll()
        .data(this.dataset)
        .join("text")
        .attr("text-anchor", "middle")
        .attr("x", (d)=>xScale((d.end + d.start) / 2))
        .attr("y", (d)=>60-yScale(d.value)-5)
        .attr("dominant-baseline", "middle")  // 垂直居中
        .text((d)=>d.value)
        .attr("font-size", 12);


      var ticks = [];
      for(let i=-2100;i<=1900;i+=100)ticks.push(i);
      var axis = d3.axisBottom(xScale)
          .tickValues(ticks)
          .tickFormat(d3.format(""))
          .tickSizeOuter(0);
      // 添加刻度尺
      this.svg.append("g")
        .attr("transform", `translate(0, 60)`)
        .call(axis);
      
      
    },
  },
  watch: {
    dataset:{
      handler(newVal, oldVal){
        console.log("bars_refresh")
        this.bars_refresh();
      },
      deep: true,
    },
  }
};
</script>

<style scoped>
.chart-container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
}

.donut-chart {
  display: flex;
  justify-content: center;
  align-items: center;
  background: rgb(217, 208, 208);
}

</style>