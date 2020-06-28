<template>
  <div id="app">
    <b-modal id="bv-modal-heart-attack" hide-footer>
      <template v-slot:modal-title>Heart attack prediction result</template>
      <div class="d-block text-center">
        <h3>{{result}}</h3>
        <h5>Porcentaje de precision: {{accuracy}}%</h5>
      </div>
      <b-button class="mt-3" block @click="$bvModal.hide('bv-modal-heart-attack')">Ok</b-button>
    </b-modal>
    <nav class="navbar navbar-light bg-light">
      <a class="navbar-brand" href="#">
        <img
          src="../assets/minsa.png"
          height="30"
          class="d-inline-block align-top"
          alt
          loading="lazy"
        />
        SI404:Analisis de sentimientos para tweets
      </a>
    </nav>
    <div class="container">
      <p class="d-inline-block">Calcular los últimos</p>
      <b-form-input class="d-inline-block" v-model="age" type="number" />
      <b-button
        block
        pill
        id="predict-btn"
        variant="primary"
        @click="requestSentimentAnalysis"
      >CALCULAR</b-button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "App",
  data() {
    return {
      result: "NO RESULT",
      accuracy: 0
    };
  },
  methods: {
    requestSentimentAnalysis() {
      var data = {
        number_tweets: 10
      };
      axios({
        method: "POST",
        url: " http://localhost:5000/predict",
        data: data
      }).then(
        result => {
          this.result = result.data.response;
          this.accuracy = result.data.accuracy;
          this.$bvModal.show("bv-modal-heart-attack");
          this.results = result.data;
        },
        error => {
          console.error(error);
        }
      );
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
