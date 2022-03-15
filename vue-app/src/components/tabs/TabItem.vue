<template>
    <li class="nav-item username" :id=" 'parent'+this.worksheet.id ">
        <button class="nav-link block-head" data-bs-toggle="tab" :data-bs-target=" '#'+this.worksheet.id " type="button">
            <img class="profile-pic-small" :src="this.worksheet.image">
            <span>{{this.worksheet.username}}</span>
        </button>
        <button class="btn btn-danger close" type="button" @click="closeTab()">X</button>
    </li>
</template>

<script>
export default {
 name: "TabItem",
 props:['worksheet'],
 methods:{
     async closeTab(){
         console.log('closeTab:' + this.worksheet.id);

        var confirmResult = confirm('Вы уверенны что хотите закрыть эту анкету?');
        if(confirmResult){
            var username = this.worksheet.username;
            let result = await window.eel.closeTab(username)()
            if(result === true){
                this.$store.commit('removeWorksheet', this.worksheet);
                this.toast('Вы вышли из анкеты', 'success');
            }else{
                this.toast('Что-то пошло не так при закрытии вкладки.', 'error');
            }
        }

     }
 }
}
</script>