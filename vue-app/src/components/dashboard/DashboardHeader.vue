<template>
  <header id="dashboard-header">
    <h5>
      <span class="" id="a-name">{{ username }}</span>
    </h5>
    <div class="exit-btn">
      <button type="button" class="btn btn-sm btn-dark" @click="logout()">
        Выйти
      </button>
    </div>
  </header>
</template>

<script>
export default {
  name: "DashboardHeader",
  props: ["username"],
  methods: {
    async logout() {
      console.log("logout trigger");

      await window.eel.logout()((result) => {
        if(result){
            this.$store.state.isLoggedIn = false;
        }else{
          this.toast('Не удалось выйти', 'error')
          console.log(result);
        }
        
      });
    },
  },
};
</script>