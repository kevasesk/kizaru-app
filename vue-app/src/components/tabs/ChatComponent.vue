<template>
<div>
    <div class="row">
        <div class="col-7">
             <h6 class="block-head">Сообщения для чатов:</h6>
        </div>
        <div class="col-5">
            <button type="button" class="btn btn-dark" @click="loadMessages()" style="float:right;">Загрузить сообщения</button>
            <button type="button" class="btn btn-dark" @click="saveMessages()" style="margin-right: 5px; float:right;">Сохранить сообщения</button>
        </div>
    </div>
    <div class="row">
        <div class="col">
            
            <textarea class="block" data-role="mail-text" v-model="messages_one" placeholder="Сообщения от сайта"></textarea>
            <textarea class="block" data-role="mail-text" v-model="messages_two" placeholder="Сообщения от расшерения"></textarea>
           
            <button type="button" class="btn btn-dark" @click="siteStart()" style="margin-right: 5px;">Начать отправку от сайта</button>
            <button type="button" class="btn btn-dark" @click="extentionStart()">Начать отправку от расшерения</button>
        </div>
    </div>
    
</div>
</template>
<script>
export default {
    props: ["worksheet"],
    data(){
        return {
            messages_one: "",
            messages_two: ""
        }
    },
    methods:{
        siteStart(){
            console.log(this.messages_one);

        },
        extentionStart(){
            console.log(this.messages_two);
        },
        async saveMessages(){
            var username =  this.worksheet.username;
            var messages_one = this.messages_one;
            var messages_two = this.messages_two;
            if(username && (messages_one || messages_two)){
                var confirmResult = confirm('Вы уверенны что хотите сохранить текущий список сообщений? Сохранённый будет перезаписан.');
                if(confirmResult){
                    messages_one = messages_one.split('\n');
                    messages_two = messages_two.split('\n');
                    let result = await window.eel.save_chat_messages(username, messages_one, messages_two)()
                    if(result === true){
                        this.toast('Сообщения сохранены', 'success')
                    }else{
                        this.toast('Что-то пошло не так при сохранении сообщений.', 'error')
                    }
                }
            }else{
                this.toast('Вам нужно сначало залогинится в анкету и ввести сообщения', 'warning')
            }
            return true;

        },
        async loadMessages(){
            var username =  this.worksheet.username;
            if(username){
                var confirmResult = confirm('Вы уверенны что хотите загрузить сохраненный список сообщений? Текущий будет утерян.');
                if(confirmResult){
                    let result = await window.eel.load_chat_messages(username)()
                    console.log(result);
                    if(Array.isArray(result['messages_one']) || Array.isArray(result['messages_two'])){
                        var messages_one = '';
                        var messages_two = '';
                        for(var i=0;i< result['messages_one'].length ;i++){
                            if(result['messages_one'][i]){
                                messages_one += result['messages_one'][i] + '\n';
                            }
                        }
                        for(var j=0;j< result['messages_two'].length ;j++){
                            if(result['messages_two'][j]){
                                messages_two += result['messages_two'][j] + '\n';
                            }
                        }
                        this.messages_one = messages_one 
                        this.messages_two = messages_two
                        this.toast('Сообщения загруженны', 'success')
                    }else{
                        this.toast('Что-то пошло не так при загрузке сообщений.', 'error')
                    }
                }
            }else{
                this.toast('Вам нужно сначало залогинится в анкету', 'warning')
            }
            return true;

        },
    }

}
</script>