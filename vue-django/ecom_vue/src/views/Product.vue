<template>
    <div class="page-product">
        <div class ='columns is-multiline' >
            <div class="column is-9">
                <figure class='image mb-6'>
                    <img v-bind:src="product.get_image" alt="">
                </figure>

                <h1>{{ product.name }}</h1>
                <h1>{{ product.descriprion }}</h1>
            </div>
    </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Product',
    data() {
        return {
            product: {},
            
        }
    },
    mounted() {
        this.getProduct() 
    },
    methods: {
        getProduct(){
            const category_slug = this.$route.params.category_slug
            const product_slug = this.$route.params.product_slug

            axios
                 .get(`/api/v1/products/${category_slug}/${product_slug}`)
                 .then(response => {
                     this.product = response.data

                 })
            
            .catch(error => {
                    console.log(error)
                })
            
         
        },
        
    }
}
</script>