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
            <TabContent :worksheet="worksheet" />
        </template>
      </div>
    </div>
    <GalleryModal/>
  </div>
</template>

<script>
import NewItem from "./NewItem.vue";
import TabItem from "./TabItem.vue";
import TabContent from "./TabContent.vue";
import GalleryModal from "../modals/GalleryModal.vue";

export default {
  name: "WorksheetsContainer",
  components: {
    NewItem,
    TabItem,
    TabContent,
    GalleryModal
  },
  methods: {
    async initWorksheets(){
        this.$store.state.loadingModalHidden = false;
        let accounts = await window.eel.load_accounts()();
        this.$store.commit('clearWorksheets');
        for (var account in accounts) {
          this.$store.commit('addWorksheet', accounts[account]);
        }
        this.$store.state.loadingModalHidden = true;
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