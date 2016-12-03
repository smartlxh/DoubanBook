package com.example.smartlxh;

import java.util.LinkedList;

/**
 * Created by lixianhai on 30/11/2016.
 */
public class ResultJson {
    private int code;
    private LinkedList<Book> items;

    public void setCode(int code){
        this.code = code;

    }

    public int getCode(){
        return code;
    }
    public void setList(LinkedList<Book> items){
        this.items = items;
    }

    public LinkedList<Book> getItems(){
        return items;
    }

    public ResultJson(int code ,LinkedList<Book> items){
        this.code = code;
        this.items = items;
    }
}
