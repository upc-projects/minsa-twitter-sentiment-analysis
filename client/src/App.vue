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
      <img :src="getGifUrlPath(result_image_path)" width="175" height="175" />
      <h2>Resultado: {{result}}</h2>
      <h3>Ingresar la cantidad de últimos tweets para analizar</h3>
      <b-form-input class="d-inline-block" v-model="number_tweets" type="number" />
      <br />
      <br />
      <br />
      <b-button block pill id="predict-btn" variant="primary" @click="requestSentimentAnalysis">
        REALIZAR ANALISIS DE SENTIMIENTO
        <div class="d-flex justify-content-center">
          <div class="spinner-border" role="status">
            <span class="sr-only">Loading...</span>
          </div>
        </div>
      </b-button>
      <b-button
        block
        pill
        disabled
        id="predict-btn"
        variant="warning"
        @click="requestSentimentAnalysis"
      >VER DETALLES DE RESULTADOS</b-button>
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
      accuracy: 0,
      number_tweets: 10,
      result_image_path: "neutral"
    };
  },
  methods: {
    getGifUrlPath(gif) {
      var images = require.context("../assets/", false, /\.gif$/);
      return images("./" + gif + ".gif");
    },
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
