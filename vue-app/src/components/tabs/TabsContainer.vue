<template>
  <div id="dashboard-wrapper">
    <div class="container">
      <div class="row">
        <div class="col">
          <ul class="nav nav-tabs" id="accountsTablist">
            <template v-for="worksheet in getWorksheets()" :key="worksheet.id" >
              <TabItem :worksheet="worksheet" />
            </template>
            <NewItem />
          </ul>
        </div>
      </div>
      <div class="tab-content" id="tabContent">
        <template v-for="worksheet in getWorksheets()" :key="worksheet.id" >
            <TabContent  :worksheet="worksheet" />
            <!-- <TabProgress :worksheet="worksheet" /> -->
        </template>
      </div>
      <!-- <script>
                initAccounts();
            </script> -->
    </div>
  </div>
</template>

<script>
import NewItem from "./NewItem.vue";
import TabItem from "./TabItem.vue";
import TabContent from "./TabContent.vue";
// import TabProgress from "./TabProgress.vue";

export default {
  name: "WorksheetsContainer",
  components: {
    NewItem,
    TabItem,
    TabContent,
    // TabProgress
  },
  methods: {
    async initWorksheets(){
        let accounts = await window.eel.load_accounts()();
        for (var account in accounts) {
          this.$store.commit('addWorksheet', accounts[account]);
        }
    },
    getWorksheets() {
      return this.$store.state.worksheets;
    },
  },
  mounted(){
    this.initWorksheets();
  }
};
</script>