package com.example.aisports

import ai.fritz.core.Fritz
import ai.fritz.vision.poseestimation.Skeleton
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.aisports.ui.login.LoginActivity
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        SignUp.setOnClickListener {
            val intent = Intent(this, SignUpActivity :: class.java)
            startActivity(intent)
        }

        Login.setOnClickListener {
            val intent = Intent(this, LoginActivity :: class.java)
            startActivity(intent)
        }

        //Fritz.configure(this, "5a584f0dceb94048803c928e82c2432f")
    }


}