<template>
  <div>
      <navbar/>
      <div class="container">
          <router-view/>
      </div>
  </div>
</template>

<script>
  import Navbar from '@/components/NavBar';

  export default {
    name: 'App',
    components: {
      Navbar,
    },
  };
</script>
