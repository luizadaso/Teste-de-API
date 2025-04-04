<template>
  <div id="app">
    <input v-model="query" @input="search" placeholder="Search for operators">
    <ul>
      <li v-for="operator in operators" :key="operator['Registro ANS']">{{ operator['Nome Fantasia'] }}</li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      query: '',
      operators: []
    };
  },
  methods: {
    async search() {
      if (this.query) {
        const response = await axios.get(`http://localhost:5000/search?query=${this.query}`);
        this.operators = response.data;
      } else {
        this.operators = [];
      }
    }
  }
};
</script>

<style>
/* Adicione estilos conforme necessário */
</style>