package bank.management.system;

/**
 *
 * @author vansh
 */

import java.sql.*;

public class Conn {
    
    Connection c;
    Statement s;
    
    public Conn() {
        try {
            c = DriverManager.getConnection("jdbc:mysql://localhost:3306/bankmanagementsystem", "root","9760270722");
            s = c.createStatement();
        }catch (Exception e){
            System.out.println(e);
        }
    }
}
