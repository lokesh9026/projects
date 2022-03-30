<template>
<div>
  <div class="home">Home</div>

  <section class="hero is-medium is-dark mb-6">
    <div class="hero-body has-text-centered">
      <p class="title mb-6">Welcome to Djacket</p>
      <p class="subtitle">The best jacket store online</p>
    </div>
  </section>

  <div class="columns is-multiline">
    <div class="column is-12">
      <h2 class="is-size-2 has-text-centered">Latest products</h2>
      
      <div
        class="column is-3"
          v-for="product in latestProducts"
          v-bind:key="product.id"
      >
        <div class="box">
          <figure class="image mb-4">
            <img :src="product.get_thumbnail" />
          </figure>

          <h3>{{ product.name }}</h3>
          <h3>{{ product.price }}</h3>
          <router-link v-bind:to="product.get_absolute_url" class='button is-dark mt-4'>View Details</router-link>
        </div>
      </div>
    </div>
  </div>
  
  
</div>
</template>

<script>
import axios from "axios";
export default {
  name: "Home",

  data() {
    return {
      latestProducts: [],
    };
  },
  components: {},
  mounted() {
    this.getLatestProducts();
  },
  methods: {
    getLatestProducts() {
      axios
        .get("/api/v1/latest-products/")
        .then((response) => {
          this.latestProducts = response.data;
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
