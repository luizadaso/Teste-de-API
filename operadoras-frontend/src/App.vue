<template>
  <div id="app">
    <h1>Busca de Operadoras de Plano de Saúde</h1>
    <div class="search-container">
      <input v-model="query" @input="search" placeholder="Digite o nome da operadora">
    </div>
    <ul class="results-list">
      <li v-for="operator in operators" :key="operator['Registro ANS']">
        <div class="operator-card">
          <h2>{{ operator['Nome Fantasia'] }}</h2>
          <p><strong>Registro ANS:</strong> {{ operator['Registro ANS'] }}</p>
          <p><strong>CNPJ:</strong> {{ operator['CNPJ'] }}</p>
          <p><strong>Razão Social:</strong> {{ operator['Razão Social'] }}</p>
        </div>
      </li>
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
        try {
          const response = await axios.get(`http://localhost:5000/search?query=${this.query}`);
          this.operators = response.data;
        } catch (error) {
          console.error("Erro ao buscar dados:", error);
        }
      } else {
        this.operators = [];
      }
    }
  }
};
</script>

<style>
body {
  font-family: Arial, sans-serif;
  background-color: #f4f4f4;
  margin: 0;
  padding: 0;
}

#app {
  max-width: 800px;
  margin: 50px auto;
  padding: 20px;
  background: #fff;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
}

h1 {
  text-align: center;
  color: #333;
}

.search-container {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

input {
  width: 100%;
  max-width: 400px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
}

.results-list {
  list-style: none;
  padding: 0;
}

.operator-card {
  background: #f9f9f9;
  margin-bottom: 10px;
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.operator-card h2 {
  margin: 0 0 10px;
  font-size: 20px;
  color: #333;
}

.operator-card p {
  margin: 5px 0;
  color: #666;
}
</style>