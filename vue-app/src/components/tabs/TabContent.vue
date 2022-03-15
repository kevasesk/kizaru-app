<template>
   <div class="tab-pane fade" :id="id">
        <div class="row align-items-center">
            <div class="col-2">
                <img data-role="profile-pic" :src="image">
            </div>
            <div class="col-4">
                <input type="text" class="custom-input form-control form-control-sm" data-role="profile-username" placeholder="Логин" v-model="username">
            </div>
            <div class="col-4">
                <input type="password" class="custom-input form-control form-control-sm" data-role="profile-password" placeholder="Пароль" v-model="password">
            </div>
            <div class="col-2">
                <button data-role="profile-login-btn" type="button" class="btn btn-dark float-right" @click="loginOnSite()">Вход</button>
            </div>
        </div>
        <div class="row">
            <div class="col-10">
                <div class="input-group input-group-sm" id="ua-block">
                    <input type="text" class="custom-input form-control" placeholder="User-Agent" data-role="ua" aria-describedby="basic-addon1" v-model="ua">
                </div>
            </div>
            <div class="col-2">
                <button class="btn btn-dark float-right" type="button" @click="setUserAgent()">Сохранить</button>
            </div>
        </div>
        <div class="row">
            <div class="col-2">
                <span class="block-head">Список ссылок</span>
            </div>
            <div class="col-10">
                <button class="btn btn-dark float-right" type="button" @click="saveLinks()">Сохранить ссылки</button>
                <button class="btn btn-dark float-right" type="button" @click="loadLinks()" style="margin-right:5px;">Загрузить ссылки</button>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <textarea class="block" v-model="links"></textarea>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <h6 class="block-head">Текст рассылки</h6>
                <textarea class="block" data-role="mail-text"></textarea>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <input type="hidden" data-role="gallery-image-data-id"/>
                <img src="img/userpic.jpg" data-role="gallery-image-src" width="70" height="100"/>
                <button type="button" class="btn btn-dark" @click="openGallery()">Выбрать картинку</button>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <button data-role="start-btn" type="button" class="btn btn-block btn-dark start-btn" @click="start()">Начать работу</button>
            </div>
        </div>
    <!-- Modal -->

    </div>
</template>

<script>
export default {
    name: "TabContent",
    props: ["worksheet"],
    data() {
        return {
            id: this.worksheet.id,
            username: this.worksheet.username,
            password: this.worksheet.password,
            image: this.worksheet.image,
            ua: this.worksheet.ua,
            links: ''
        }
    },
    methods:{
        async loginOnSite(){
            if(this.username == '' || this.password == '' || this.ua == ''){
                this.toast('Пожалуйста, введите логин, пароль и User-Agent вашего браузера', 'warning')
            }else{
                this.$store.state.loadingModalHidden = false;
                let result = await window.eel.login_on_site(this.id, this.username, this.password, this.ua)()
                if(result != null){
                    //this.image = result;
                    this.$store.commit('updateWorksheet', {
                        id: this.id,
                        username: this.username,
                        password: this.password,
                        image: result,
                        ua: this.ua,
                    })
                    this.image = this.$store.getters.getWorksheet(this.worksheet.id).image;
                }else{
                    this.toast('Не удалось войти', 'error');
                }
                this.$store.state.loadingModalHidden = true;
              
            }
            
        },
        setUserAgent(){
            console.log('setUserAgent');
        },
        async saveLinks(){
            var username = this.username;
            var links = this.links;
            if(username && links){
                var confirmResult = confirm('Вы уверенны что хотите сохранить текущий список ссылок? Сохранённый будет перезаписан.');
                if(confirmResult){
                    links = links.split('\n');
                    let result = await window.eel.save_links(username, links)()
                    if(result === true){
                        this.toast('Ссылки сохранены', 'success')
                    }else{
                        this.toast('Что-то пошло не так при сохранении ссылок.', 'error')
                    }
                }
            }else{
                this.toast('Вам нужно сначало залогинится в анкету и ввести ссылки', 'warning')
            }
            return true;

        },
        async loadLinks(){
            var username = this.username;
            if(username){
                var confirmResult = confirm('Вы уверенны что хотите загрузить сохраненный список ссылок? Текущий будет утерян.');
                if(confirmResult){
                    let result = await window.eel.load_links(username)()
                    if(Array.isArray(result)){
                        var links = '';
                        for(var i=0;i< result.length ;i++){
                            links += result[i] + '\n';
                        }
                        this.links = links 
                        this.toast('Ссылки загруженны', 'success')
                    }else{
                        this.toast('Что-то пошло не так загрузке ссылок.', 'error')
                    }
                }
            }else{
                this.toast('Вам нужно сначало залогинится в анкету', 'warning')
            }
            return true;

        },
        openGallery(){

        },
        start(){
            
        }
    }
};
</script>

<style>
</style>