package io.rcos.gymtracker.data;

import android.os.AsyncTask;
import android.util.Log;

import io.rcos.gymtracker.MainActivity;
import io.rcos.gymtracker.data.model.LoggedInUser;

import java.io.IOException;
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
            URL url = null;
            try {
                url = new URL(Vars.LOGIN_URL);
            } catch (MalformedURLException ex) {
                Log.e(Vars.ETAG_URL_MALFORMED, ex.getMessage());
            }
            HttpURLConnection LoginConnection = null;
            try {
                LoginConnection = (HttpURLConnection) url.openConnection();
                LoginConnection.setRequestMethod("POST");
                
            } catch (IOException | NullPointerException ex) {
                Log.e(Vars.ETAG_LOGIN_CONNECTION, ex.getMessage());
            }
            return null;
        }
    }
}
