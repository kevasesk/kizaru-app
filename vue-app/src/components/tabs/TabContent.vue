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
                <textarea class="block" data-role="mail-text" v-model="message"></textarea>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <input type="hidden" data-role="gallery-image-data-id"/>
                <img :src="this.$store.state.galleryActiveImageSrc[this.worksheet.id] ?? 'img/userpic.jpg' " data-role="gallery-image-src" width="70" height="100"/>
                <button type="button" class="btn btn-dark" @click="openGallery()">Выбрать картинку</button>
            </div>
        </div>
        <ChatComponent :worksheet="worksheet" />
        <div class="row">
            <div class="col">
                <button data-role="start-btn" type="button" class="btn btn-block btn-dark start-btn" @click="start(id)">
                    <template v-if="this.isWorking(this.worksheet.id)">
                       Работаем...<img class="modal-loader" src="img/loader_4.gif" width="30" height="30" /> 
                    </template>
                    <template v-else>
                        Начать работу
                    </template>
                </button>
            </div>
        </div>
        <TabProgress :worksheet="worksheet" />
        <ErrorsModal :worksheet="worksheet" /> 
    </div>
</template>

<script>
import TabProgress from "./TabProgress.vue";
import ErrorsModal from "../modals/ErrorsModal.vue";
import ChatComponent from "./ChatComponent.vue";

export default {
    name: "TabContent",
    props: ["worksheet"],
    components:{
        TabProgress,
        ErrorsModal,
        ChatComponent
    },
    data() {
        return {
            id: this.worksheet.id,
            username: this.worksheet.username == 'Новый профиль' ? '' : this.worksheet.username,
            password: this.worksheet.password,
            image: this.worksheet.image,
            ua: this.worksheet.ua,
            links: '',
            message: ''
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
        async setUserAgent(){
            var username = this.username;
            var ua = this.ua;
            if (ua != '' && (/(opera|safari|firefox|(?!chrome))\/?\s*(\.?\d+(\.\d+)*)/i).test(ua) && ua.length >= 16) {
                let result = await window.eel.set_user_agent(ua, username)()
                if(result){
                    this.toast('Успешно', 'success');
                    return true;
                }else{
                     this.toast('Что-то пошло не так с сохранением User-Agent', 'error');
                }
            }
            else {
                this.toast('Пожалуйста, укажите User-Agent вашего браузера', 'warning')
                return false
            }
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
        async openGallery(){
            var ua = this.worksheet.ua;
            var id = this.worksheet.id;
            var username = this.worksheet.username;
            var password = this.worksheet.password;
            window.jQuery('#galleryModal').modal('show');
            this.$store.state.currentGalleryWorksheetId = id;
            this.$store.state.galleryImages = [];
            let images = await window.eel.load_gallery(id, username, password, ua)()
            if(Array.isArray(images) && images.length > 0){
                for (var image in images) {
                    this.$store.commit('addGalleryImage', images[image]);
                }
            }else{
                this.toast('Что-то пошло не так при загрузке галереи.', 'error')
            }
        },
        async start(targetId){
           var self = this;
           var links = window.jQuery.trim(this.links).split('\n')
           if(links != [] && this.message != '' && this.ua != '' && this.$store.state.galleryActiveImageId[this.worksheet.id]){
                window.jQuery('#'+targetId).find('[data-role="progressModal"]').modal('show');
                
                // gallery dataid - this.$store.state.galleryActiveImageId[this.$store.state.currentGalleryWorksheetId]
                if(!this.isWorking(targetId)){
                    
                    await window.eel.add_mailing_messages({
                        id: this.worksheet.id,
                        links: links,
                        message: this.message,
                        ua: this.ua,
                        dataId: this.$store.state.galleryActiveImageId[this.worksheet.id]
                    })()
                    // TODO send all real data to sender
                    this.$store.state.sendingWorking[targetId] = true;

                    this.updateProgressBar(targetId, 0, links.length)
                    let interval = setInterval(async function(){
                        let successCount = await window.eel.get_success_count(targetId)()
                        // stop
                        if (successCount == links.length) {
                            self.updateProgressBar(targetId, successCount, links.length)
                            clearInterval(interval)
                            self.toast('Рассылка завершена ('+self.worksheet.username+')', 'success')
                            window.jQuery('#'+targetId).find('[data-role="progressModal"]').modal('hide');
                            self.$store.state.sendingWorking[targetId] = false;

                            let errorLinks = await window.eel.get_errors_list(targetId)()
                            if(errorLinks && errorLinks.length > 0){
                                //window.jQuery('#'+targetId).find('[data-role="errorsModal"]').modal({backdrop: false});
                                //window.jQuery('#'+targetId).find('[data-role="errorsModal"]').draggable({handle: ".modal-header"});
                                window.jQuery('#'+targetId).find('[data-role="errorsModal"]').modal('show');
                                var text = '';
                                for(var i = 0; i < errorLinks.length; i++){
                                    text += errorLinks[i] + '\n';
                                }
                                window.jQuery('#'+targetId).find('[data-role="errorLinks"]').val(text);
                            }
                        }
                        self.updateProgressBar(targetId, successCount, links.length)
                    }, 1000)
                    //window.jQuery('#'+targetId+' [data-role="start-btn"]').html('Работаем...')
                } else {
                    window.jQuery('#'+targetId).find('[data-role="progressModal"]').modal('show');
                }
           }else{
               this.toast('Пожалуйста, укажите всю необходимую информацию для запуска рассылки', 'warning')
           }
    
 
            
        },
        isWorking(targetId){
            return this.$store.state.sendingWorking[targetId];
        },
        updateProgressBar(targetId, now, max) {
            window.jQuery('#'+targetId+' .progress-text').html(now + ' из ' + max)
            window.jQuery('#'+targetId+' [data-role="progress"]').css('width', (now/max*100) + '%')
        }
    }
};
</script>

<style>
</style>