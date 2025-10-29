<script setup>
import Main from './components/Main.vue'
import PieChart from './components/PieChart.vue'
import WordCloud from './components/WordCloud.vue';
import MutipleSelector from './components/MutipleSelector.vue';
import RadialBarChart from './components/RadialBarChart.vue';
import Card from './components/Card.vue';
import Details from './components/Details.vue';
</script>

<template>
  <!-- <Main /> -->
  <!-- <PieChart /> -->
  <!-- <WordCloud /> -->
  <!-- <MutipleSelector /> -->
  <!-- <RadialBarChart /> -->
  <!-- <Card /> -->
  <Details />
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
