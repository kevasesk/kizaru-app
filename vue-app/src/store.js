import {createStore} from 'vuex'

const store = createStore({
    state: {
        isLoggedIn: false,
        username: '',
        worksheets: [],
        loadingModalHidden: true
    },
    mutations: {
        addWorksheet (state, worksheet) {
            state.worksheets.push(worksheet);
        },
        updateWorksheet (state, worksheet) {
            const index = state.worksheets.findIndex((el) => el.id === worksheet.id);
            console.log(worksheet.id);
            if (index > -1){
                state.worksheets[index] = worksheet;
            }
        },
        removeWorksheet (state, worksheet) {
            const index = state.worksheets.findIndex((el) => el.id === worksheet.id);
            if (index > -1) state.worksheets.splice(index, 1);
        },
     },
     getters: {
        getWorksheet: (state) => (worksheetId) => {
            return state.worksheets.find(worksheet => worksheet.id === worksheetId)
        }
     }
})

export default store;