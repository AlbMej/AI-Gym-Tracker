package com.example.aisports

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import com.example.aisports.ui.login.LoginActivity

class SignUpActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_signup)

        val login : Button = findViewById(R.id.login_account)
        login.setOnClickListener() {
            val intent = Intent(this, LoginActivity :: class.java)
            startActivity(intent)
        }
    }
}