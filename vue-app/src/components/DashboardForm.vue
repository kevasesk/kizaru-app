<template>
    <div>
        <DashboardHeader :username="username"/>
        <TabsContainer/>
    </div>
</template>

<script>
import DashboardHeader from "./dashboard/DashboardHeader.vue";
import TabsContainer from "./dashboard/tabs/TabsContainer.vue";

export default {
  name: "DashboardForm",
  props: ['username'],
  components: {
    DashboardHeader,
    TabsContainer
  },
};
</script>