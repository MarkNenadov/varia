/* 

MySQLDemo.java

A demo of how to connect and query a MySQL database through JDBC
in Java.

Note: The MySQL jar file must be in your classpath.

AUTHOR

Mark J. Nenadov (2011)
* Essex, Ontario
* Email: <marknenadov@gmail.com> 

LICENSING

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version

This program is distributed in the hope that it will be useful
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>. 

*/


package jdbcdemo;

import java.util.ArrayList;
import java.util.Properties;
import java.sql.*;

public class MySQLDemo {
            public static Connection conn;
            public static String user_name = "root";
            public static String password = "mypass";

             public static Connection connect_to_db(String url)
             {
                    Properties props = new Properties();
                    props.setProperty("user", user_name);
                    props.setProperty("password", password);

                    try {
                        return DriverManager.getConnection(url, props);
                    }
                    catch (SQLException e) {
                        System.out.println(e);
                        return null;
                    }
             }

            public static ArrayList get_clients(ResultSet rs)
            {
                ArrayList<String> clients = new ArrayList<String>();

                try {
                    while (rs.next())
                    {
                        clients.add(rs.getString("name"));
                    }
                }
                catch (SQLException e) {
                    System.out.println("Attempt to get clients failed.");
                    return null;
                }

                return clients;
            }

             public static void main(String[] args)
             {
                 ResultSet rs;
                 String url = "jdbc:mysql://localhost:3306/pythonbyte";

                 try {
                    Class.forName("com.mysql.jdbc.Driver");
                 }
                 catch (ClassNotFoundException e) {
                     System.out.println("It appears you don't have the MySQL JDBC driver installed");
                 }

                 conn = connect_to_db(url);

                 if (conn == null) {
                     System.out.println("Can't connect to db for some reason");
                 }
                 else {
                     // proceed
                     try {
                        Statement st = conn.createStatement();
                        rs = st.executeQuery("SELECT * FROM clients");
                        ArrayList clients = get_clients(rs);

                        if (clients == null) {
                            System.out.println("Query Error");
                        }
                        else {
                            System.out.println(clients);
                        }
                     }
                     catch (SQLException e) {
                         System.out.println("Query Error: " + e);
                     }


                 }

             }

}




