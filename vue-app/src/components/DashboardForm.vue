<template>
    <div>
        <DashboardHeader/>
        <TabsContainer/>
    </div>
</template>

<script>
import DashboardHeader from "./dashboard/DashboardHeader.vue";
import TabsContainer from "./tabs/TabsContainer.vue";

export default {
  name: "DashboardForm",
  components: {
    DashboardHeader,
    TabsContainer
  },
};
</script>