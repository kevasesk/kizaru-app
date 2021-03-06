import {createStore} from 'vuex'

const store = createStore({
    state: {
        isLoggedIn: false,
        username: '',
        worksheets: [],
        galleryImages: [],

        loadingModalHidden: true,
        galleryModalHidden: true,

        galleryActiveImageId: [],
        galleryActiveImageSrc: [],
        currentGalleryWorksheetId: null,

        //sending
        sendingWorking: {}
    },
    mutations: {
        clearWorksheets(state){
            state.worksheets = [];
        },
        addWorksheet (state, worksheet) {
            state.worksheets.push(worksheet);
        },
        updateWorksheet (state, worksheet) {
            const index = state.worksheets.findIndex((el) => el.id === worksheet.id);
            if (index > -1){
                state.worksheets[index] = worksheet;
            }
        },
        removeWorksheet (state, worksheet) {
            const index = state.worksheets.findIndex((el) => el.id === worksheet.id);
            if (index > -1) state.worksheets.splice(index, 1);
        },
        
        addGalleryImage (state, image) {
            state.galleryImages.push(image);
        },

     },
     getters: {
        getWorksheet: (state) => (worksheetId) => {
            return state.worksheets.find(worksheet => worksheet.id === worksheetId)
        }
     }
})

export default store;