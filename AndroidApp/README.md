High Level Overview:
- Android application written in Kotlin to receive/send info.
- Front end UI/UX resides in res folder. They layouts of every page are in res/layout. 

3 Pages so Far: 
1) Main Page (welcome page)
    - Layout File: activity_main.xml
2) Signup Page
    - Layout File: activity_signup.xml
3) Login Page
    - Layout File: activity_login.xml


COROUTINES
Coroutines similar to async task. Use for any network activity so it's not handled on main UI thread.  


https://heartbeat.fritz.ai/replacing-asynctask-in-android-with-kotlin-coroutines-to-handle-background-tasks-93108f8f2db  
https://kotlinlang.org/docs/tutorials/coroutines/coroutines-basic-jvm.html  
https://stackoverflow.com/questions/46226518/what-is-the-difference-between-launch-join-and-async-await-in-kotlin-coroutines#46226519  
    - Difference between Launch and Async coroutines


To look at:
https://medium.com/androiddevelopers/coroutines-on-android-part-iii-real-work-2ba8a2ec2f45  
https://auth0.com/blog/authenticating-android-apps-developed-with-kotlin/  Login Form Development  
https://stackoverflow.com/questions/5944987/how-to-create-a-popup-window-popupwindow-in-android Popup message window  


To do:
- Handle user management:
    - Utilize REST API
        - Once we utilize REST API, will need to delete the sql package which includes ConnectionLayer.kt and UserTable.kt classes. 
        - 

- Try to integrate AI Computer Vision
    - https://www.fritz.ai/pose-estimation/
    - https://github.com/fritzlabs/fritz-examples/tree/master/Android/CameraBoilerplateApp (example for Fritz AI)
    - https://github.com/edvardHua/PoseEstimationForMobile

- Chat functionality
    - Use Websockets
    - Will need to write server code of some sort (maybe add it to API)
    - https://github.com/sbearben/chat-backend (potentially can utilize this code to create)
    - Current I have a few layouts written up from this guide: 
        - https://www.scaledrone.com/blog/android-chat-tutorial/
            - Creates:
                - res/drawable/circle.xml
                - res/drawable/my_message.xml
                - res/drawable/their_message.xml
                - res/layout/activity_chat.xml
                - res/layout/my_message.xml
                - res/layout/their_message.xml
        - Should use websockets from server side code to implement the chat using our API
        
- Build off our current pages:
    - Allow for Google/Facebook login
    - Implement a Forgot Password activity and layout


