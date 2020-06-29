<template>
  <div id="app">
    <b-modal id="bv-modal-sentiment-analysis" size="xl" hide-footer>
      <h3>Detalles de los resultados</h3>
      <div class="row">
        <div class="col">
          <b>Texto del tweet</b>
        </div>
        <div class="col-md-auto">
          <b>Porcentaje de acierto</b>
        </div>
        <div class="col col-lg-2">
          <b>Resultado</b>
        </div>
      </div>
      <div v-for="(tweet,i) in details_data" v-bind:key="i" class="d-block text-center">
        <div class="card">
          <div class="card-body">
            <div class="row">
              <div class="col">{{tweet.text}}</div>
              <div class="col-md-auto">{{tweet.accuracy}}</div>
              <div class="col col-lg-2">{{tweet.result}}</div>
            </div>
          </div>
        </div>
      </div>
      <b-button class="mt-3" block @click="$bvModal.hide('bv-modal-sentiment-analysis')">Ok</b-button>
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
      <img :src="getimageUrlPath(result_image_path)" width="175" height="175" />
      <h2>Resultado: {{result}}</h2>
      <h3>Ingresar la cantidad de últimos tweets para analizar</h3>
      <b-form-input class="d-inline-block" v-model="number_tweets" type="number" />
      <br />
      <br />
      <br />
      <b-button
        :disabled="disable_analysis"
        block
        pill
        id="predict-btn"
        variant="primary"
        @click="requestSentimentAnalysis"
      >
        <div v-if="visible_loading" class="d-flex justify-content-center invisble">
          <div class="spinner-border" role="status">
            <span class="sr-only">Loading...</span>
          </div>
        </div>
        <div v-else>
          <h3>REALIZAR ANALISIS DE SENTIMIENTO</h3>
        </div>
      </b-button>
      <b-button block pill id="detail-btn" variant="warning" @click="showDetailFromAnalysis">
        <h4>VER DETALLES DE RESULTADOS</h4>
      </b-button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "App",
  data() {
    return {
      result: "NO_RESULT",
      accuracy: 0,
      number_tweets: 10,
      result_image_path: "logo.png",
      details_data: [],
      disable_analysis: false,
      visible_loading: false
    };
  },
  methods: {
    getimageUrlPath(gif) {
      var images = require.context("../assets/", false);
      return images("./" + gif);
    },
    requestSentimentAnalysis() {
      var data = {
        number_tweets: this.number_tweets
      };
      this.visible_loading = true;
      this.disable_analysis = true;
      axios({
        method: "POST",
        url: " http://localhost:5000/sentiment-analysis",
        data: data
      }).then(
        result => {
          this.details_data = result.data.details;
          console.log(this.details_data);
          this.result = result.data.mean_text;
          console.log(result.data.mean);
          switch (result.data.mean) {
            case -1:
              this.result_image_path = "disapprove.gif";
              break;
            case -0:
              this.result_image_path = "neutral.gif";
              break;
            case 1:
              this.result_image_path = "approve.gif";
              break;
          }
          this.accuracy = result.data.accuracy;
          this.results = result.data;
          this.visible_loading = false;

          this.disable_analysis = false;
        },
        error => {
          console.error(error);
        }
      );
    },
    showDetailFromAnalysis() {
      this.$bvModal.show("bv-modal-sentiment-analysis");
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
