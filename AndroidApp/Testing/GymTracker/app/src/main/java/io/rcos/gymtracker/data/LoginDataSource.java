package io.rcos.gymtracker.data;

import android.os.AsyncTask;
import android.util.Log;

import io.rcos.gymtracker.MainActivity;
import io.rcos.gymtracker.data.model.LoggedInUser;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

/**
 * Class that handles authentication w/ login credentials and retrieves user information.
 */
public class LoginDataSource {

    public Result<LoggedInUser> login(String username, String password) {

        try {
            // TODO: handle loggedInUser authentication
            LoggedInUser fakeUser =
                    new LoggedInUser(
                            java.util.UUID.randomUUID().toString(),
                            "Jane Doe");
            LoginUser User = new LoginUser();
            User.execute(username,password);

            return new Result.Success<>(fakeUser);
        } catch (Exception e) {
            return new Result.Error(new IOException("Error logging in", e));
        }
    }

    public void logout() {
        // TODO: revoke authentication
    }


    class LoginUser extends AsyncTask<String, Void, String> {

        @Override
        protected String doInBackground(String... strings) {
            String username = strings[0];
            String password = strings[1];
            String urlLoginParams = "";
            String responseStr = "";
            URL url = null;
            try {
                url = new URL(Vars.LOGIN_URL);
            } catch (MalformedURLException ex) {
                Log.e(Vars.ETAG_URL_MALFORMED, ex.getMessage());
            }
            HttpURLConnection LoginConnection = null;
            try {
                // Setting up the connection
                LoginConnection = (HttpURLConnection) url.openConnection();
                LoginConnection.setRequestMethod("POST");
                Log.d(Vars.DTAG_Login,"Preparing to send data");
                OutputStreamWriter loginWriter = new OutputStreamWriter(LoginConnection.getOutputStream());
                loginWriter.write(urlLoginParams);
                loginWriter.flush();
                loginWriter.close();

                //Creates the connection and sends the data
                LoginConnection.connect();
                if (LoginConnection.getResponseCode() == HttpURLConnection.HTTP_OK){
                    //if connection accepted
                    InputStream responseInStream = LoginConnection.getInputStream();
                    int charCode = 0;
                    while (charCode != 1) {
                        charCode = responseInStream.read();
                        if (charCode == -1) {
                            Log.d(Vars.DTAG_Login,"Input Reading Complete");
                            break;
                        } else
                            responseStr += (char) charCode;
                    }
                }
                else{
                    Log.e(Vars.ETAG_LOGIN_CONNECTION,"Login failed\n" + LoginConnection.getResponseCode() + "\n" + LoginConnection.getResponseMessage());
                }


            } catch (IOException | NullPointerException ex) {
                Log.e(Vars.ETAG_LOGIN_CONNECTION, ex.getMessage());
            }
            return responseStr;
        }

        @Override
        protected void onPostExecute(String response) {
            super.onPostExecute(response);
        }
    }
}
