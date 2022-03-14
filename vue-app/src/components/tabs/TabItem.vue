<template>
    <li class="nav-item username" :id=" 'parent'+this.worksheet.id ">
        <button class="nav-link block-head" data-bs-toggle="tab" :data-bs-target=" '#'+worksheet.id " type="button">
            <img class="profile-pic-small" :src="worksheet.image">
            <span>{{worksheet.username}}</span>
        </button>
        <button class="btn btn-danger close" type="button" @click="closeTab()">X</button>
    </li>
</template>

<script>
export default {
 name: "TabItem",
 props:['worksheet'],
 methods:{
     closeTab(){
         console.log('closeTab:' + this.worksheet.id);

     }
 }
}
</script>