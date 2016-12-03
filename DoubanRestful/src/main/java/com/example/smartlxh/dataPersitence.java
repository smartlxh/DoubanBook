package com.example.smartlxh;

import java.io.*;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Properties;
import com.example.smartlxh.dataPersitence;
import com.example.smartlxh.Book;
/**
 * Created by lixianhai on 26/11/2016.
 */
public class dataPersitence {

    String username ;
    String userPasswd;
    String url ;
    String driver ;

    public dataPersitence(){
        try {

            /*Properties prop = new Properties();
            FileInputStream fi = new FileInputStream("src/main/Resources/db.properties");
            prop.load(fi);
            username = prop.getProperty("userName");
            userPasswd = prop.getProperty("userPasswd");
            url = prop.getProperty("url");
            driver = prop.getProperty("driver");*/
            username = "root";
            userPasswd ="32784744li";
            url = "jdbc:mysql://localhost:3306/douban?useUnicode=true&characterEncoding=UTF-8";
            driver = "com.mysql.jdbc.Driver";

        }catch(Exception e){
            e.printStackTrace();
        }
    }


    public Connection getConnection(){
        Connection conn=null;
        try {

            Class.forName(driver);

            conn = DriverManager.getConnection(url, username, userPasswd);
        }catch(Exception e){
            e.printStackTrace();
        }

        return conn;

    }



    public LinkedList<Book> getByKey(String key,String value){

        LinkedList list = new LinkedList<Book>();
        try{


            Connection conn = getConnection();
            Statement state= conn.createStatement();
            String sql = "select * from bookInfo where %s like \"%s\"";
            sql = String.format(sql,key,value);

            ResultSet result = state.executeQuery(sql);
            Book book = new Book();
            while(result.next()){

                book.setName(result.getString(1).trim());
                book.setAuthor(result.getString(2).trim());
                book.setScore(result.getString(3).trim());
                book.setImgUrl(result.getString(4).trim());
                book.setDetailUrl(result.getString(5).trim());
                book.setDescription(result.getString(6).trim());
                list.add(book);
            }

        }catch (Exception e){
            e.printStackTrace();
        }
        return list;

    }



}
