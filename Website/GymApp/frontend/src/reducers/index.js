import { combineReducers } from 'redux';
import exercises from "./exercises";
import auth from "./auth";


const gymApp = combineReducers({
    exercises, auth,
})

export default gymApp;
