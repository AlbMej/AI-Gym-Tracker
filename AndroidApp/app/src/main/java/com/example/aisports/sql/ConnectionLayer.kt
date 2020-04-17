package com.example.aisports.sql

import com.example.aisports.sql.model.UserTable
import android.util.Log
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import org.jetbrains.exposed.sql.*
import org.jetbrains.exposed.sql.transactions.transaction


//TODO: delete class when API has been implemented and accessed for user management
class ConnectionLayer {
    //simple connection string builder to connect to the database
    class ConnectionStringBuilder constructor(api: String = "jdbc", databaseType : String, host: String, port: String = "5432", database : String, user: String, password: String, properties: Map<String,String> = emptyMap()) {
        var connectionString: String = "$api:$databaseType://$host:$port/$database?user=$user&password=$password&"
        init {
            for ((k,v) in properties) {
                connectionString += "$k=$v&"
            }
            connectionString.trimEnd('&')
            Log.d("CONNECTION STRING", connectionString)
        }
    }

    //function to map userQuery results to User data class object
    private fun ResultRow.toUser() = UserTable.User(
        id = this[UserTable.Users.id],
        password = this[UserTable.Users.password],
        last_login = this[UserTable.Users.last_login],
        is_superuser = this[UserTable.Users.is_superuser],
        username = this[UserTable.Users.username],
        first_name = this[UserTable.Users.first_name],
        last_name = this[UserTable.Users.last_name],
        email = this[UserTable.Users.email],
        is_staff = this[UserTable.Users.is_staff],
        is_active = this[UserTable.Users.is_active],
        date_joined = this[UserTable.Users.date_joined]
    )

    //suspended function (part of coroutine) used to perform a query for user given username/password
    suspend fun userQuery(username : String, password: String) : String {
        var searching = ""
        searching = getUser(username, password).username
        Log.d("HELLO", searching)
        return searching
    }

    //private suspended function (part of coroutine) used to actually connnect to database and perform query
    private suspend fun getUser(username : String, password : String) : UserTable.User {
        val properties = mapOf("sslmode" to "require")      //need SSL authentication to access PostgreSQL database thru Heroku
        val connect = ConnectionStringBuilder(
            "jdbc",
            "postgresql",
            "ec2-23-21-225-251.compute-1.amazonaws.com",
            "5432",
            "d4tefl2m5ii7b7",
            "lruthoqamfsgna",
            "5490aebc5c8ccdd3a97f0c287d00e55f3d702b4413d8ee1802a967d6c8706f10",
            properties
        ).connectionString

        val user : UserTable.User = withContext(Dispatchers.Default) {
            val db = Database.connect(connect)
            val name = "YOU SUCK " + db.name
            Log.d("DATABASE CONNECTION",name)

            val returnValue = transaction {
                UserTable.Users.select{ (UserTable.Users.username eq username) and (UserTable.Users.password eq password) }.map{ it.toUser() }
            }
            assert(returnValue.count() == 1)      //making sure we return ONLY 1 user
            return@withContext returnValue[0]
        }
        return user
    }

}