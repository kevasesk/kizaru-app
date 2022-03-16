<template>
  <div>
    <LoginForm v-if="showLoginForm" :loginData="loginData" />
    <LoadingModal/>
  </div>
</template>

<script>
import LoginForm from "./LoginForm.vue";
import LoadingModal from "./modals/LoadingModal.vue";

export default {
  name: "IndexComponent",
  components: {
    LoginForm,
    LoadingModal
  },
  data() {
    return {
      showLoginForm: false,
      loginData: {},
    };
  },
  methods: {
    async getAuth() {
      await window.eel.get_login_details()((login_details) => {
        if (login_details != null) {
          this.loginData.username = login_details["username"];
          this.loginData.password = login_details["password"];
          this.loginData.remember = true;
        }
        this.showLoginForm = true;
      });
    },
  },
  mounted() {
    this.getAuth();
  },
};
</script>
