<template>
  <li class="nav-item add">
    <button
      class="nav-link btn btn-success"
      id="newAccountItem"
      type="button"
      @click="createNewAccount()"
    >+</button>
  </li>
</template>

<script>

export default {
  name: "NewItem",
  methods: {
    createNewAccount() {
      this.$store.commit('addWorksheet', {
        id: 'tab'+Date.now(),
        username: "Новый профиль",
        password: "",
        image: "img/userpic.jpg",
        ua: "",
      });
    },
  },
};
</script>