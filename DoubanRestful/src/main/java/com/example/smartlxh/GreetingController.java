package com.example.smartlxh;

/**
 * Created by lixianhai on 09/11/2016.
 */


import java.util.LinkedList;
import java.util.concurrent.atomic.AtomicLong;

import org.junit.runner.Result;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import sun.awt.image.ImageWatched;

@RestController
public class GreetingController {

    private static final String template = "Hello, %s!";
    private final AtomicLong counter = new AtomicLong();

    @RequestMapping("/book")
    public ResultJson queryByBookName(@RequestParam(value="name") String name) {

        if(name==""){
            return new ResultJson(200,new LinkedList<Book>());
        }
        dataPersitence p = new dataPersitence();
        return new ResultJson(200,p.getByKey("bookName",name));

    }

    @RequestMapping("/author")
    public ResultJson queryByAuthor(@RequestParam(value="name",defaultValue = "") String author){
        dataPersitence p = new dataPersitence();
        if(author ==""){
            return new ResultJson(200,new LinkedList<Book>());
        }

        return new ResultJson(200,p.getByKey("author",author));
    }
    @RequestMapping("/country")
    public ResultJson queryByCountry(@RequestParam(value="name",defaultValue = "") String country){
        if(country ==""){
            return new ResultJson(200,new LinkedList<Book>());
        }
        dataPersitence p = new dataPersitence();
        return new ResultJson(200,p.getByKey("country",country));

    }
    @RequestMapping("/*")
   public ResultJson getError(){
        return new ResultJson(404,new LinkedList<Book>());
    }
}