<template>
<div style="margin-bottom:10px;">
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
           
           <template v-if="!siteProcessed">
                <button type="button" class="btn btn-dark" @click="siteStart()" style="margin-right: 5px;">Начать отправку от сайта</button>
           </template>
           <template v-else>
                <button type="button" class="btn btn-danger" @click="siteStop()" style="margin-right: 5px;">Закончить отправку от сайта <img class="modal-loader" src="img/loader_4.gif" width="30" height="30" /></button>
           </template>

            <template v-if="!extentionProcessed">
                <button type="button" class="btn btn-dark" @click="extentionStart()">Начать отправку от расшерения</button>
           </template>
           <template v-else>
                <button type="button" class="btn btn-danger" @click="siteStop()">Закончить отправку от расшерения <img class="modal-loader" src="img/loader_4.gif" width="30" height="30" /></button>
           </template>
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
            messages_two: "",
            siteProcessed: false,
            extentionProcessed: false
        }
    },
    created() {
        if(typeof window.socketConnection == 'undefined'){ 
            var socketServerUrl = 'ws://localhost:8081'; // 'wss://ws.dream-singles.com/ws' //TODO
            window.socketConnection = new WebSocket(socketServerUrl);
            window.socketConnection.onopen = function() {
                console.log("Connection to socket " + socketServerUrl + " opened!");
            };
            window.socketConnection.onmessage = function(e) {
                 console.log(e.data);
            };
        }
    },

    methods:{
        sendMessage(messageObject){
            window.socketConnection.send(JSON.stringify(messageObject))
        },
        sendMessages(messages, type){
            var self = this;
            var number = 0;
            var intevalTime = 1000; // 30 * 1000 // TODO
            messages = messages.split('\n');
            messages = messages.filter(n => n);
            if(messages.length > 0 ){
                if(type == 'site'){
                    self.siteProcessed = true;
                }else{
                    self.extentionProcessed = true;
                }
                var inteval = setInterval(function(){
                    self.sendMessage({
                        type: 'start-auto-invite',
                        payload: messages[number],
                        block: true,
                        ignore: true
                    });
                    number++;
                    if(number == messages.length){
                        clearInterval(inteval);
                        if(type == 'site'){
                            self.siteProcessed = false;
                        }else{
                            self.extentionProcessed = false;
                        }
                    }
                }, intevalTime);
            }
            
        },
        siteStart(){
            this.sendMessages(this.messages_one, 'site');
        },
        extentionStart(){
            this.sendMessages(this.messages_two, 'extention');
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