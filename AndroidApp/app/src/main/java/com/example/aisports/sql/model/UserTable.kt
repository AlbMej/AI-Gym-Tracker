package com.example.aisports.sql.model


import org.jetbrains.exposed.sql.Table
import org.joda.time.DateTime
import org.jetbrains.exposed.sql.jodatime.datetime

//TODO: delete class when API has been implemented and accessed for user management
//          maybe can use this model for future use????
class UserTable {
    object Users: Table("auth_user") {
        val id = integer("id")
        val password = varchar("password", 128)
        val last_login = datetime("last_login").clientDefault{ DateTime.now() }
        val is_superuser = bool("is_superuser")
        val username = varchar("username", length = 50)
        val first_name = varchar("first_name", 30)
        val last_name = varchar("last_name", 150)
        val email = varchar("email", 254)
        val is_staff = bool("is_staff")
        val is_active = bool("is_active")
        val date_joined = datetime("date_joined").clientDefault{ DateTime.now() }
    }

    data class User(
        val id: Int,
        val password: String,
        val last_login: DateTime,
        val is_superuser: Boolean,
        val username: String,
        val first_name: String,
        val last_name: String,
        val email: String,
        val is_staff: Boolean,
        val is_active: Boolean,
        val date_joined: DateTime
    )
}