<template>
  <div>
    <LoginForm v-if="showLoginForm" :loginData="loginData"/>
  </div>
</template>

<script>
import LoginForm from './LoginForm.vue'

export default {
  name: "IndexComponent",
  components: {
    LoginForm
  },
  data(){
      return {
        showLoginForm: false,
        loginData:{}
      }
  },
  methods: {
    async getAuth() {
      await window.eel.get_login_details()((login_details) => {
        if (login_details != null) {
          if (login_details["auto_login"]) {
            this.showLoginForm = true;
            this.loginData.username = login_details["username"];
            this.loginData.password = login_details["password"];
            this.loginData.remember = true;
          }
        } else {
          this.showLoginForm = true;
        }
      });
    },
  },
  mounted(){
      this.getAuth();
  }


};
</script>
