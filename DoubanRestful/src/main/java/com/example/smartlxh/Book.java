package com.example.smartlxh;

/**
 * Created by lixianhai on 26/11/2016.
 */
public class Book {
    private int  isbn;
    private String name;
    private String author;
    //private String date;
    private String score;
    private String description;
    private String imgUrl;
    private String detailUrl;

    public int getCode(){
        return isbn;
    }

    public void setCode(int code){
        this.isbn = isbn;
    }
    public String getName(){
        return name;
    }

    public void setName(String name){
        this.name =name;
    }

    public String getAuthor(){
        return author;
    }

    public void setAuthor(String author){
        this.author = author;
    }

    public String getScore(){
        return score;
    }

    public void setScore(String date){
        this.score = date;
    }

    public String getDescription(){
        return description;
    }


    public void setDescription(String description){
        this.description = description;
    }

    public String getImgUrl(){
        return imgUrl;
    }

    public void setImgUrl(String imgUrl){
        this.imgUrl = imgUrl;
    }

    public String getDetailUrl(){
        return detailUrl;
    }

    public void setDetailUrl(String detailUrl){
        this.detailUrl = detailUrl;
    }
}
