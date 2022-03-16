<template>
  <div class="background-modal" id="loading-modal" v-show="!isHidden()">
    <img class="modal-loader" src="img/loader.gif" width="30" height="30" />
  </div>
</template>

<script>
export default {
  methods: {
    isHidden() {
      return this.$store.state.loadingModalHidden;
    },
  },
};
</script>